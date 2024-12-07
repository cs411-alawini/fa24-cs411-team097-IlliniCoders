import os
from flask import Flask, jsonify
from google.cloud.sql.connector import Connector
import pymysql
import sqlalchemy
import datetime
from datetime import timezone, datetime

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

connector = Connector()

def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "cs411project-439519:us-central1:db-currents",
        "pymysql",
        user="demo",
        password="currents",
        db="Currents"
    )
    print('conn successful')

    return conn 

pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

# sessions:
# session ID, query (as a string), timestamp (int) (HHMMSS)
'''
CREATE TABLE Sessions(
session_id INT PRIMARY KEY,
min_lat INT,
max_lat INT,
min_long INT,
max_long INT,
timestamp INT);

CREATE TABLE SessionsHistory(
session_id INT PRIMARY KEY,
min_lat INT,
max_lat INT,
min_long INT,
max_long INT,
timestamp INT);

'''

def get_natural_disaster(min_lat, max_lat, min_long, max_long):
    x = 1
    print(x)
    # now = datetime.datetime.now()
    # timestamp = int(now.strftime("%H%M%S"))

    # with pool.connect() as db_conn:
    #     print(input)
    #     min_lat = int(min_lat)
    #     max_lat = int(max_lat)
    #     min_long = int(min_long)
    #     max_long = int(max_long)
    #     print(min_lat, max_lat, min_long, max_long)
    #     # query1 = f'SELECT nd.region_id, date, name, max_wind, min_pressure FROM NaturalDisaster nd JOIN Regions r on nd.region_id = r.region_id WHERE ((r.min_latitude >= {min_lat}) AND (r.max_latitude <= {max_lat})) AND ((r.min_longitude >= {min_long}) AND (r.max_longitude <= {max_long})) ORDER BY nd.region_id LIMIT 15;'
    #     natural_disaster_proc = f'CALL GetNaturalDisasterData({min_lat}, {max_lat}, {min_long}, {max_long});'
    #     # query2 = f'SELECT o.region_id, o.scientific_name, o.year_first_seen, o.year_last_seen, o.minimumDepthInMeters, o.maximumDepthInMeters From OceanSpecies o JOIN Regions r ON o.region_id = r.region_id WHERE ((r.min_latitude >= {min_lat}) AND (r.max_latitude <= {max_lat})) AND ((r.min_longitude >= {min_long}) AND (r.max_longitude <= {max_long})) ORDER BY o.region_id LIMIT 15;'
    #     ocean_species_proc = f'CALL GetOceanSpeciesByRegion({min_lat}, {max_lat}, {min_long}, {max_long});'
    #     # del_query = f'DELETE FROM Sessions WHERE TIMESTAMPDIFF(SECOND, FROM_UNIXTIME({timestamp}), NOW()) > 60;'
    #     query_max_session_id = f'SELECT MAX(session_id) FROM Sessions;'
    #     max_session_id_result = db_conn.execute(sqlalchemy.text(query_max_session_id)).fetchone()
    #     max_session_id = max_session_id_result[0] if max_session_id_result[0] is not None else 0
    #     new_session_id = max_session_id + 1
    #     insert_session_query = f'INSERT INTO Sessions (session_id, min_lat, max_lat, min_long, max_long, timestamp) VALUES ({new_session_id}, {min_lat}, {max_lat}, {min_long}, {max_long}, {timestamp});'
    #     # db_conn.execute(sqlalchemy.text(del_query))
    #     db_conn.execute(sqlalchemy.text(insert_session_query))
    #     db_conn.commit()

    #     disasters = db_conn.execute(sqlalchemy.text(natural_disaster_proc)).fetchall()
    #     species = db_conn.execute(sqlalchemy.text(ocean_species_proc)).fetchall()

    #     out1 = []
    #     for row in disasters:
    #         tmp = []
    #         for idx, i in enumerate(row):
    #             if idx == 1:
    #                 tmp.append(datetime.datetime.strptime(i, '%Y%m%d').strftime('%Y-%m-%d'))
    #             elif idx == 3 or idx == 4:
    #                 tmp.append(float(i))
    #             elif idx == 2:
    #                 tmp.append(i.rstrip('\r').lower().capitalize())
    #             else:
    #                 tmp.append(i)
    #         out1.append(tmp)

    #     out2 = []
    #     for row in species:
    #         tmp = []
    #         for idx, i in enumerate(row):
    #             if idx == 2 or idx == 3:
    #                 date_utc = datetime.datetime.fromtimestamp(timestamp, tz=timezone.utc)
    #                 tmp.append(date_utc.strftime('%Y-%m-%d %H:%M:%S'))
    #             elif idx == 4 or idx == 5:
    #                 tmp.append(float(i))
    #             else:
    #                 tmp.append(i)
    #         out2.append(tmp)

    # print(out1)
    connector.close()
    # return out1, out2

def format_date(date_string):
    year = date_string[:4]
    month = date_string[4:6]
    day = date_string[6:]
    return f"{year}-{month}-{day}"

def get_advanced_query1():
    print("here")
    with pool.connect() as db_conn:
        query1 = f'SELECT Weather.region_id, Weather.date, AVG(Weather.max_temperature) AS avg_max_temperature, AVG(Weather.precipitation) AS avg_percipitation, AVG(Weather.min_temperature ) AS avg_min_temperature FROM Weather JOIN NaturalDisaster ON Weather.region_id = NaturalDisaster.region_id GROUP BY Weather.region_id, date LIMIT 100;'

        result = db_conn.execute(sqlalchemy.text(query1)).fetchall()
        print("db results:",result)
        out = []
        for row in result:
            tmp = []
            for idx, i in enumerate(row):
                if idx == 1:
                    print(i)
                    tmp.append(format_date(str(i)))
                elif idx == 3 or idx == 4 or idx == 2:
                    tmp.append(int(i))
                else:
                    tmp.append(i)
            out.append(tmp)

    print(out)
    connector.close()
    return out

def get_advanced_query2():
    print("here")
    with pool.connect() as db_conn:
        query1 = f'SELECT region_avg.region_id, avg_precipitation FROM ( SELECT w.region_id, AVG(w.precipitation) AS avg_precipitation FROM Weather w JOIN NaturalDisaster nd ON w.region_id = nd.region_id AND w.date = nd.date GROUP BY w.region_id ) AS region_avg WHERE region_avg.avg_precipitation > (SELECT AVG(precipitation) FROM Weather) LIMIT 100;'

        result = db_conn.execute(sqlalchemy.text(query1)).fetchall()
        print("db results:",result)
        out = []
        for row in result:
            tmp = []
            for idx, i in enumerate(row):
                if idx == 2:
                    tmp.append(int(i))
                else:
                    tmp.append(i)
            out.append(tmp)

    print(out)
    connector.close()
    return out

def get_advanced_query3():
    print("here")
    with pool.connect() as db_conn:
        query1 = f'SELECT OceanSpecies.region_id, OceanSpecies.scientific_name FROM OceanSpecies JOIN NaturalDisaster ON OceanSpecies.region_id = NaturalDisaster.region_id WHERE NaturalDisaster.max_wind > 80 OR NaturalDisaster.min_pressure  < 950 GROUP BY OceanSpecies.region_id, OceanSpecies.scientific_name ORDER BY OceanSpecies.region_id LIMIT 100;'

        result = db_conn.execute(sqlalchemy.text(query1)).fetchall()
        print("db results:",result)
        out = []
        for row in result:
            tmp = []
            for i in row:
                tmp.append(i)
            out.append(tmp)

    print(out)
    connector.close()
    return out

def get_advanced_query4():
    print("here")
    with pool.connect() as db_conn:
        query1 = f'SELECT OceanSpecies.region_id, OceanSpecies.scientific_name FROM OceanSpecies WHERE OceanSpecies.region_id IN ( SELECT region_id FROM Weather WHERE precipitation> 100 GROUP BY region_id HAVING COUNT(*) > 5 ) ORDER BY OceanSpecies.region_id LIMIT 100;'

        result = db_conn.execute(sqlalchemy.text(query1)).fetchall()
        print("db results:",result)
        out = []
        for row in result:
            tmp = []
            for elem in (row):
                tmp.append(elem)
            out.append(tmp)

    print(out)
    connector.close()
    return out


# DELIMITER $$

# CREATE TRIGGER delete_old_sessions
# BEFORE INSERT ON Sessions
# FOR EACH ROW
# BEGIN
#     DECLARE current_time_int INT;

#     SET current_time_int = CURRENT_TIME() + 0;

#     DELETE FROM Sessions
#     WHERE (current_time_int - timestamp) > 100;
# END$$

# DELIMITER ;

# DELIMITER $$

# CREATE TRIGGER update_session_ids
# AFTER DELETE ON Sessions
# FOR EACH ROW
# BEGIN
#     DECLARE max_id INT;
#     SELECT MAX(session_id) INTO max_id FROM Sessions;
#     UPDATE Sessions
#     SET session_id = max_id + 1
#     WHERE session_id = OLD.session_id;
# END$$

# DELIMITER ;
