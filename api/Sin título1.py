from fastapi import FastAPI
import mysql.connector

app = FastAPI()

# conexión a la base
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="music_user",
        password="music_pass",
        database="music_analytics"
    )


@app.get("/")
def home():
    return {"message": "Music Analytics API"}