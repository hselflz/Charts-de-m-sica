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

@app.get("/top-songs")
def top_songs():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM top_songs
        LIMIT 10
    """)

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results

@app.get("/top-artists")
def top_artists():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM top_artists
    """)

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results

@app.get("/active-users")
def active_users():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM active_users
        LIMIT 10
    """)

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results

@app.get("/plays-by-day")
def plays_by_day():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM plays_by_day")

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results