import os

from dotenv import load_dotenv, find_dotenv

import psycopg2
from psycopg2 import OperationalError
from psycopg2.extras import DictCursor

load_dotenv(find_dotenv())

def connect_to_postgres():
    
    SQL_NAME = os.getenv("SQL_NAME")
    SQL_USER = os.getenv("SQL_USER")
    SQL_PASSWORD = os.getenv("SQL_PASSWORD")
    SQL_HOST = os.getenv("SQL_HOST")
    SQL_PORT = os.getenv("SQL_PORT")
    
    try:
        connection = psycopg2.connect(
            dbname=SQL_NAME,
            user=SQL_USER,
            password=SQL_PASSWORD,
            host=SQL_HOST,
            port=SQL_PORT
        )
        
        # Создание курсора
        cursor = connection.cursor(cursor_factory=DictCursor)
        print("Подключение к базе данных PostgreSQL установлено успешно!")
        
        if cursor:
            return cursor
        else: 
            raise ValueError("Ошибка при создании подключения")

    except OperationalError as e:
        print(f"Ошибка подключения к базе данных: {e}")

def update_user_balances(cursor):
    try:
        # Обновление баланса для всех пользователей
        cursor.execute("""
            UPDATE users_user
            SET balance = balance + daily_amount
            WHERE daily_amount IS NOT NULL
        """)
        
        # Подтверждение транзакции
        cursor.connection.commit()
        print("Баланс всех пользователей успешно обновлен.")
    
    except Exception as e:
        # Откат в случае ошибки
        cursor.connection.rollback()
        print(f"Ошибка при обновлении баланса: {e}")

