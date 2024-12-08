# GCP SQL Commands

This document contains all the code we ran on GCP for Stage 4 Checkpoint 2.

- - -

<sup> Table of Contents

[1. DeleteDuplicateSessions](#deleteduplicatesessions)

[2. set_rerun](#set_rerun)

[3. Transaction](#transaction)

[4. GetNaturalDisasterData](#getnaturaldisasterdata)

[5. GetOceanSpeciesByRegion](#getoceanspeciesbyregion)

[6. Sessions](#sessions)

## DeleteDuplicateSessions
Procedure. Deletes duplicate sessions according to whether or not the query has been rerun. 

```sql
DELIMITER $$
CREATE PROCEDURE DeleteDuplicateSessions()
BEGIN
    CREATE TEMPORARY TABLE TempSessionsToDelete AS
    SELECT a.session_id
    FROM Sessions a
    INNER JOIN (
        SELECT min_lat, max_lat, min_long, max_long, COUNT(*) AS ct
        FROM Sessions
        GROUP BY min_lat, max_lat, min_long, max_long
        HAVING ct > 1
    ) b
    ON a.min_lat = b.min_lat 
    AND a.max_lat = b.max_lat 
    AND a.min_long = b.min_long 
    AND a.max_long = b.max_long
    WHERE a.rerun = 0 
    OR a.timestamp < (SELECT MAX(c.timestamp) FROM Sessions c);

    DELETE FROM Sessions
    WHERE session_id IN (SELECT session_id FROM TempSessionsToDelete);
    
    DROP TEMPORARY TABLE TempSessionsToDelete;
 END$$
```

## set_rerun
Trigger. Sets a previously run query as rerun. 

```sql
DELIMITER $$
    CREATE TRIGGER set_rerun
    BEFORE INSERT ON Sessions
    FOR EACH ROW
    BEGIN
        DECLARE active_session INT;
        
        SELECT session_id INTO active_session
        FROM Sessions
        WHERE min_lat = NEW.min_lat 
        AND max_lat = NEW.max_lat 
        AND min_long = NEW.min_long 
        AND max_long = NEW.max_long
        LIMIT 1;
    
        IF active_session IS NOT NULL THEN
            SET NEW.rerun = TRUE;
        ELSE
            SET NEW.rerun = FALSE;
        END IF;
    END $$
DELIMITER ;
```

## Transaction

This code from `db.py` (path to file in repository: `currents/server/db.py`) models how the trigger and procedure work in the transaction.

```python
insert_session_query = f'INSERT INTO Sessions (session_id, min_lat, max_lat, min_long, max_long, rerun, timestamp) VALUES ({new_session_id}, {min_lat}, {max_lat}, {min_long}, {max_long}, FALSE, {timestamp});'
del_proc = f'CALL DeleteDuplicateSessions();'
# START TRANSACTION 1:
        # WRITE 1:
        db_conn.execute(sqlalchemy.text(insert_session_query))
	    # WRITE 1:
        db_conn.execute(sqlalchemy.text(del_proc))
	    # COMMIT 1:
        db_conn.commit()
```

## GetNaturalDisasterData
Procedure. Gets all the information about natural disasters occurring in the regions inside the provided latitude/longitude bounds. 

```sql
DELIMITER $$
CREATE PROCEDURE GetNaturalDisasterData(
    IN min_lat INT,
    IN max_lat INT,
    IN min_long INT,
    IN max_long INT
)
BEGIN
    SELECT 
        nd.region_id, 
        nd.date, 
        nd.name, 
        nd.max_wind, 
        nd.min_pressure
    FROM 
        NaturalDisaster nd 
    JOIN 
        Regions r 
    ON 
        nd.region_id = r.region_id
    WHERE 
        (r.min_latitude >= min_lat AND r.max_latitude <= max_lat)
        AND 
        (r.min_longitude >= min_long AND r.max_longitude <= max_long)	
ORDER BY nd.region_id    
LIMIT 100;
END $$
DELIMITER ;
```


## GetOceanSpeciesByRegion
Procedure. Gets all the information about ocean species whose habitats are in the regions inside the provided latitude/longitude bounds. 

```sql
DELIMITER $$
CREATE PROCEDURE GetOceanSpeciesByRegion(
    IN min_lat INT,
    IN max_lat INT,
    IN min_long INT,
    IN max_long INT
)
BEGIN
    SELECT 
        o.region_id, 
        o.scientific_name, 
        o.year_first_seen, 
        o.year_last_seen, 
        o.minimumDepthInMeters, 
        o.maximumDepthInMeters
    FROM 
        OceanSpecies o
    JOIN 
        Regions r 
    ON 
        o.region_id = r.region_id
    WHERE 
        (r.min_latitude >= min_lat AND r.max_latitude <= max_lat)
        AND 
        (r.min_longitude >= min_long AND r.max_longitude <= max_long)
    ORDER BY 
        o.region_id
 LIMIT 100;
END $$

DELIMITER ;
```

## Sessions
Table creation. (This has only been run once in our project to create the table). Creates the Sessions table appropriately. 

```sql
CREATE TABLE Sessions(
session_id INT PRIMARY KEY,
min_lat INT,
max_lat INT,
min_long INT,
max_long INT,
rerun BOOLEAN,
timestamp INT);
```