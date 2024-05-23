import sqlite3


def create_table_users(db_name='bot.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            created_at TEXT
        )
    ''')

    connection.commit()
    connection.close()


def create_table_orders(db_name='bot.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            user_phone TEXT,
            user_email TEXT,
            order_amount INTEGER,
            status TEXT,
            temple_id INTEGER,
            service_name TEXT,
            service_type TEXT,
            period TEXT,
            created_at TEXT,
            started_at TEXT,
            completed_at TEXT     
        )
    ''')

    connection.commit()
    connection.close()


def create_table_temples(db_name='bot.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS temples (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            country TEXT,
            city TEXT DEFAULT '-'
        )
    ''')

    connection.commit()
    connection.close()


def create_table_services(db_name='bot.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temple_id INTEGER,
            note_once_price INTEGER,
            note_month_price INTEGER,
            note_half_year_price INTEGER,
            note_year_price INTEGER,
            candle_once_price INTEGER,
            candle_month_price INTEGER,
            candle_half_year_price INTEGER,
            candle_year_price INTEGER
        )
    ''')


def drop_table_orders(db_name='bot.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS orders
    ''')

    connection.commit()
    connection.close()


def clear_tables(db_name='bot.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Удаляем все строки из таблицы orders
    cursor.execute('''
        DELETE FROM orders
    ''')

    # Удаляем все строки из таблицы users
    cursor.execute('''
        DELETE FROM users
    ''')

    connection.commit()
    connection.close()


if __name__ == "__main__":
    # drop_table_orders()
    # create_table_users()
    # create_table_orders()
    # create_table_temples()
    # create_table_services()
    clear_tables()
