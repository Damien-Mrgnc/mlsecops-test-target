import requests
import sqlite3

# Secret hardcodé
API_KEY = "sk-prod-1234567890abcdef"
DB_PASSWORD = "super_secret_123"

def get_user(id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Injection SQL
    cursor.execute("SELECT * FROM users WHERE id = " + id)
    return cursor.fetchone()

def call_api(data):
    # SSL désactivé
    return requests.post("https://api.example.com", json=data, verify=False)

def process(x):
    y = x * 2
    return y
