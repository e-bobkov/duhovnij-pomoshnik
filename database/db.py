import aiosqlite

from models.User import User


class Db:
    def __init__(self, db_name='../bot.db'):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    async def connect(self):
        self.connection = await aiosqlite.connect(self.db_name)
        await self.connection.execute("PRAGMA journal_mode=WAL;")
        self.cursor = await self.connection.cursor()

    async def close(self):
        await self.cursor.close()
        await self.connection.close()

    async def save_user(self, chat_id, username, first_name, created_at, last_name=None):
        await self.connect()

        existing_user = await self.cursor.execute('''
            SELECT * FROM users WHERE chat_id = ?
        ''', (chat_id,))

        existing_user = await existing_user.fetchone()

        if not existing_user:
            await self.cursor.execute('''
                INSERT INTO users (chat_id, username, first_name, last_name, created_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (chat_id, username, first_name, last_name, created_at))
            await self.connection.commit()

        await self.close()

    async def get_user_by_chat_id(self, chat_id):
        await self.connect()

        user_data = await self.cursor.execute('''
            SELECT * FROM users WHERE chat_id = ?
        ''', (chat_id,))

        user_data = await user_data.fetchone()

        if user_data:
            user_dict = {
                'chat_id': user_data[0],
                'username': user_data[1],
                'first_name': user_data[2],
                'last_name': user_data[3],
                'date': user_data[4]
            }
            return User(**user_dict)

        await self.close()
        return None

    async def get_user_reg_date_by_chat_id(self, chat_id):
        await self.connect()

        user_data = await self.cursor.execute('''
            SELECT created_at FROM users WHERE chat_id = ?
        ''', (chat_id,))

        user_data = await user_data.fetchone()

        if user_data:
            return user_data[0]

        await self.close()
        return None

    async def get_order_total(self, temple_name, period, service):
        await self.connect()

        period_columns = {
            'once': {'Подать записку': 'note_once_price', 'Поставить свечу': 'candle_once_price'},
            'month': {'Подать записку': 'note_month_price', 'Поставить свечу': 'candle_month_price'},
            'half_year': {'Подать записку': 'note_half_year_price', 'Поставить свечу': 'candle_half_year_price'},
            'year': {'Подать записку': 'note_year_price', 'Поставить свечу': 'candle_year_price'}
        }

        period_column = period_columns.get(period)
        if period_column is None:
            return None

        period_column = period_column.get(service)
        if period_column is None:
            return None

        query = f'''
            SELECT s.{period_column}
            FROM temples t
            JOIN services s ON t.id = s.temple_id
            WHERE t.name = ?;
        '''

        cursor = await self.cursor.execute(query, (temple_name,))
        price = await cursor.fetchone()
        if price is None:
            return None

        await self.close()
        return price[0]

    async def get_temple_id_by_name(self, temple_name):
        await self.connect()

        temple_id = await self.cursor.execute('''
            SELECT id FROM temples WHERE name = ?
        ''', (temple_name,))

        temple_id = await temple_id.fetchone()

        if temple_id:
            return temple_id[0]

        await self.close()
        return None

    async def get_user_id_by_chat_id(self, chat_id):
        await self.connect()

        user_id = await self.cursor.execute('''
            SELECT id FROM users WHERE chat_id = ?
        ''', (chat_id,))

        user_id = await user_id.fetchone()

        if user_id:
            return user_id[0]

        await self.close()
        return None

    async def create_order(self, user_id, user_phone, user_email, order_amount, temple_id, service_name, service_type,
                           period, created_at):
        await self.connect()

        await self.cursor.execute('''
            INSERT INTO orders (user_id, user_phone, user_email, order_amount, status, temple_id, service_name, 
            service_type, period, created_at, started_at, completed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, user_phone, user_email, order_amount, 'waiting', temple_id, service_name, service_type, period,
              created_at, None, None))

        await self.connection.commit()
        await self.close()

    async def get_users_orders_status_waiting(self, user_id):
        await self.connect()

        orders = await self.cursor.execute('''
            SELECT * FROM orders WHERE user_id = ? AND status = ?
        ''', (user_id, 'waiting'))

        orders = await orders.fetchall()

        if orders:
            return orders

        await self.close()
        return None

    async def get_user_orders_status_in_progress(self, user_id):
        await self.connect()

        orders = await self.cursor.execute('''
            SELECT * FROM orders WHERE user_id = ? AND status = ?
        ''', (user_id, 'in_progress'))

        orders = await orders.fetchall()

        if orders:
            return orders

        await self.close()
        return None

    async def get_user_orders_status_completed(self, user_id):
        await self.connect()

        orders = await self.cursor.execute('''
            SELECT * FROM orders WHERE user_id = ? AND status = ?
        ''', (user_id, 'completed'))

        orders = await orders.fetchall()

        if orders:
            return orders

        await self.close()
        return None

    async def get_temple_info_by_id(self, temple_id):
        await self.connect()

        temple_info = await self.cursor.execute('''
            SELECT name, country, city FROM temples WHERE id = ?
        ''', (temple_id,))

        temple_info = await temple_info.fetchone()

        if temple_info:
            return temple_info

        await self.close()
        return None

    async def get_services_by_temple_id(self, temple_id):
        await self.connect()

        services = await self.cursor.execute('''
            SELECT * FROM services WHERE temple_id = ?
        ''', (temple_id,))

        services = await services.fetchall()

        if services:
            return services

        await self.close()
        return None
