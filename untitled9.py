# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:14:39 2018

@author: Project
"""
from datetime import datetime
import mysql.connector
cnx = mysql.connector.connect(host="localhost", user="root", 
                           passwd="321", db="test")
cursor = cnx.cursor()

timestamp = datetime.now()

add_mydrones = (
    "INSERT INTO mydrones "
    "(model, url, price, extracted) "
    "VALUES (%(model)s, %(url)s, %(price)s, %(extracted)s)"
    )

data_mydrones = {
        'model': "drone 00+",
        'url': "amason.come",
        'price': 25,
        'extracted': timestamp
         }            
cursor.execute(add_mydrones, data_mydrones)

current_id = cursor.lastrowid

add_mydrones_text = (
    "INSERT INTO mydrones_text "
    "(topic, model_id) "
    "VALUES (%(topic)s, %(model_id)s)"
    )

data_mydrones_text = {
        'topic': 'Article_00+',
        'model_id': current_id
        }
                     
cursor.execute(add_mydrones_text, data_mydrones_text)

# Make sure data is committed to the database
cnx.commit()

# Last row output
sql = ("""
       SELECT * FROM MyDrones join mydrones_text 
       on MyDrones_text.model_id = mydrones.unic_id
       ORDER BY mydrones.unic_id DESC LIMIT 1
       """)
    
cursor.execute(sql)
data = cursor.fetchall()
print(data)

cursor.close()
cnx.close()