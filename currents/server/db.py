import os
from flask import Flask, jsonify
from google.cloud.sql.connector import Connector
import pymysql
import sqlalchemy

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

def get_natural_disaster(input):
    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )
    
    with pool.connect() as db_conn:
  #      print('input:', input, type(input), input.get("query"))

        #d_name = input.get("query")
        d_name = str.upper(input) + "\r"
        query = f'SELECT * FROM NaturalDisaster WHERE name = "{d_name}" LIMIT 15;'
        # query = f'SELECT * FROM NaturalDisaster LIMIT 15;'

        disasters = db_conn.execute(sqlalchemy.text(query)).fetchall()
        out = []
        for row in disasters:
            tmp = []
            for i in row:
                tmp.append(i)
                #print(i)
            out.append(tmp)
            #print(row.values())
            #out.append(row)

    print(out)
    connector.close()
    return out
