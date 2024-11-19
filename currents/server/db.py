import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
    except pymysql.MySQLError as e:
        print(e)

    return conn


def get_natural_disaster(d_name):
    conn = open_connection()
    with conn.cursor() as cursor:
        query = f'SELECT * FROM NaturalDisaster WHERE name == {d_name} LIMIT 15;'
        result = cursor.execute(query)
        disasters = cursor.fetchall()
        got_names = jsonify(disasters) if result > 0 else 'No matching events found.'
    conn.close()
    return got_names
