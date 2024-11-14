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
        db_connection_name,
        "pymysql",
        user=db_user,
        password=db_password,
        db=db_name
    )
    print('conn successful')

    return conn 

def get_natural_disaster(d_name):
    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )
    
    with pool.connect() as db_conn:
        query = f'SELECT * FROM NaturalDisaster WHERE name = "{d_name}" LIMIT 15;'
        disasters = db_conn.execute(sqlalchemy.text(query)).fetchall()
        for row in disasters:
            print(row)
    connector.close()
