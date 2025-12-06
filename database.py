import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    connection = get_db_connection()
    with open('schema.sql') as f:
        connection.executescript(f.read())
    connection.commit()
    connection.close()
    print("Base de datos inicializada.")

if __name__ == '__main__':
    init_db()
