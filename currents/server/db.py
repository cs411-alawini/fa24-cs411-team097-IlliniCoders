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

def format_date(date_string):
    year = date_string[:4]
    month = date_string[4:6]
    day = date_string[6:]
    return f"{year}-{month}-{day}"

def get_natural_disaster(min_lat, max_lat, min_long, max_long):
    now = datetime.datetime.now()
    timestamp = int(now.strftime("%H%M%S"))

    with pool.connect() as db_conn:
        print(input)
        min_lat = int(min_lat)
        max_lat = int(max_lat)
        min_long = int(min_long)
        max_long = int(max_long)
        print(min_lat, max_lat, min_long, max_long)
        natural_disaster_proc = f'CALL GetNaturalDisasterData({min_lat}, {max_lat}, {min_long}, {max_long});'
        ocean_species_proc = f'CALL GetOceanSpeciesByRegion({min_lat}, {max_lat}, {min_long}, {max_long});'
        query_max_session_id = f'SELECT MAX(session_id) FROM Sessions;'
        max_session_id_result = db_conn.execute(sqlalchemy.text(query_max_session_id)).fetchone()
        max_session_id = max_session_id_result[0] if max_session_id_result[0] is not None else 0
        new_session_id = max_session_id + 1
        insert_session_query = f'INSERT INTO Sessions (session_id, min_lat, max_lat, min_long, max_long, rerun, timestamp) VALUES ({new_session_id}, {min_lat}, {max_lat}, {min_long}, {max_long}, FALSE, {timestamp});'
        del_proc = f'CALL DeleteDuplicateSessions();'
        db_conn.execute(sqlalchemy.text(insert_session_query))
        db_conn.execute(sqlalchemy.text(del_proc))
        db_conn.commit()

        disasters = db_conn.execute(sqlalchemy.text(natural_disaster_proc)).fetchall()
        species = db_conn.execute(sqlalchemy.text(ocean_species_proc)).fetchall()

        out1 = []
        for row in disasters:
            tmp = []
            for idx, i in enumerate(row):
                if idx == 1:
                    tmp.append(datetime.datetime.strptime(i, '%Y%m%d').strftime('%Y-%m-%d'))
                elif idx == 3 or idx == 4:
                    tmp.append(float(i))
                elif idx == 2:
                    tmp.append(i.rstrip('\r').lower().capitalize())
                else:
                    tmp.append(i)
            out1.append(tmp)

        out2 = []
        for row in species:
            tmp = []
            for idx, i in enumerate(row):
                if idx == 2 or idx == 3:
                    date_utc = datetime.datetime.fromtimestamp(timestamp, tz=timezone.utc)
                    tmp.append(date_utc.strftime('%Y-%m-%d %H:%M:%S'))
                elif idx == 4 or idx == 5:
                    tmp.append(float(i))
                else:
                    tmp.append(i)
            out2.append(tmp)

    print(out1)
    connector.close()
    return out1, out2

def get_advanced_query1():
    with pool.connect() as db_conn:
        query1 = f'SELECT Weather.region_id, Weather.date, AVG(Weather.max_temperature) AS avg_max_temperature, AVG(Weather.precipitation) AS avg_percipitation, AVG(Weather.min_temperature ) AS avg_min_temperature FROM Weather JOIN NaturalDisaster ON Weather.region_id = NaturalDisaster.region_id GROUP BY Weather.region_id, date LIMIT 20;'

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
                    tmp.append((i)) 
                out.append(tmp)
    print(out)
    connector.close()
    return out

def get_advanced_query2():
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