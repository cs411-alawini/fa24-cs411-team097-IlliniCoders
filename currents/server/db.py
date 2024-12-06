import os
from flask import Flask, jsonify
from google.cloud.sql.connector import Connector
import pymysql
import sqlalchemy
from datetime import datetime

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

# def get_natural_disaster(input):
    
#     with pool.connect() as db_conn:
#         print(input)
#         d_name = str.upper(input) + "\r"
#         query = f'SELECT region_id, date, name, max_wind, min_pressure FROM NaturalDisaster WHERE name = "{d_name}" LIMIT 15;'

#         disasters = db_conn.execute(sqlalchemy.text(query)).fetchall()
#         out = []
#         for row in disasters:
#             tmp = []
#             for idx, i in enumerate(row):
#                 if idx == 1:
#                     tmp.append(datetime.strptime(i, '%Y%m%d').strftime('%Y-%m-%d'))
#                 elif idx == 3 or idx == 4:
#                     tmp.append(float(i))
#                 elif idx == 2:
#                     tmp.append(i.rstrip('\r').lower().capitalize())
#                 else:
#                     tmp.append(i)
#             out.append(tmp)

#     print(out)
#     connector.close()
#     return out

def get_natural_disaster(min_lat, max_lat, min_long, max_long):
    with pool.connect() as db_conn:
        print(input)
        min_lat = int(min_lat)
        max_lat = int(max_lat)
        min_long = int(min_long)
        max_long = int(max_long)
        print(min_lat, max_lat, min_long, max_long)
        query = f'SELECT nd.region_id, date, name, max_wind, min_pressure FROM NaturalDisaster nd JOIN Regions r on nd.region_id = r.region_id WHERE ((r.min_latitude >= {min_lat}) AND (r.max_latitude <= {max_lat})) AND ((r.min_longitude >= {min_long}) AND (r.max_longitude <= {max_long})) LIMIT 15;'

        disasters = db_conn.execute(sqlalchemy.text(query)).fetchall()
        out = []
        for row in disasters:
            tmp = []
            for idx, i in enumerate(row):
                if idx == 1:
                    tmp.append(datetime.strptime(i, '%Y%m%d').strftime('%Y-%m-%d'))
                elif idx == 3 or idx == 4:
                    tmp.append(float(i))
                elif idx == 2:
                    tmp.append(i.rstrip('\r').lower().capitalize())
                else:
                    tmp.append(i)
            out.append(tmp)

    print(out)
    connector.close()
    return out