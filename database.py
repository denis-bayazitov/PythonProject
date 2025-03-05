import mysql.connector
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

dbconfig = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

dbconfig_logs = {
    'host': os.getenv('LOG_DB_HOST'),
    'user': os.getenv('LOG_DB_USER'),
    'password': os.getenv('LOG_DB_PASSWORD'),
    'database': os.getenv('LOG_DB_NAME')
}

def get_db_connection():
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    return conn, cursor

def get_log_connection():
    conn_logs = mysql.connector.connect(**dbconfig_logs)
    cursor_logs = conn_logs.cursor()
    return conn_logs, cursor_logs

def log_search(keyword, query_text):
    conn_logs, cursor_logs = get_log_connection()
    log_query = """
    INSERT INTO Denis_logs (keyword, query) VALUES (%s, %s);
    """
    cursor_logs.execute(log_query, (keyword, query_text))
    conn_logs.commit()
    cursor_logs.close()
    conn_logs.close()
