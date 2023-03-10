import sqlite3
import first
conn = sqlite3.connect("weather.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        location TEXT,
        temperature REAL,
        pressure INTEGER,
        humidity INTEGER,
        wind_speed REAL,
        weather_description TEXT
    )
""")
cur.execute("""
    INSERT INTO weather (location, temperature, pressure, humidity, wind_speed, weather_description)
    VALUES (?, ?, ?, ?, ?, ?)
""", (first.city, first.temperature, first.pressure, first.humidity, first.wind_speed, first.weather_description))
conn.commit()
conn.close()
