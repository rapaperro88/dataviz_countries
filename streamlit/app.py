
# ---------------------------------- using mysql.connector ----------------------------------


# import streamlit as st
# import pandas as pd
# import mysql.connector

# def connection():
#     conn = mysql.connector.connect(host = "mysql-development",
#                   user = 'root',
#                   password = 'andres',
#                   database = 'datavizapp',
#                   port = 3306
#     )
#     c = conn.cursor()
#     return c , conn

# # Load CSV
# homicides_path = "data/homicides.csv"
# homicides = pd.read_csv(homicides_path)
# st.dataframe(homicides)

# # mysql.connector
# c, connector = connection()

# sql = "CREATE TABLE regions (id INT AUTO_INCREMENT PRIMARY KEY, region VARCHAR(255));"
# c.execute(sql)

# dataframe to sql database: does not work with mysql.connerctor ?
# homicides.to_sql('homicides', con=connector, if_exists="replace", method='multi')


# ---------------------------------- using sqlalchemy ----------------------------------

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
# 
# specify database configurations
config = {
    'host': 'mysql-development',
    'port': 3306,
    'user': 'root',
    'password': 'andres',
    'database': 'datavizapp'
}

# Title
st.title("Hello App!")
# Load CSV
homicides_path = "data/homicides.csv"
homicides = pd.read_csv(homicides_path)
st.dataframe(homicides)

# sqlalchemy
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')
# specify connection string
connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_str)
# connect to database
connection = engine.connect()

# connection.commit()

homicides.to_sql('homicides', 
    con=connection, 
    if_exists="replace",
    # method='multi',
    )

res = connection.execute('''
SELECT * FROM homicides 
''')

st.text(res)

# ---------------------------------- END ----------------------------------

st.success("Success")