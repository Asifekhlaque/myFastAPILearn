from fastapi import FastAPI

import sqlite3

app=FastAPI()
conn=sqlite3.connect("text.db",check_same_thread=False)

cursor=conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS todos(
id INTEGER PRIMARY KEY,
title TEXT,
completed TEXT
)
''')

conn.commit()

@app.get("/")
def home():
    return{
        "message":"SQLite is connected"
    }