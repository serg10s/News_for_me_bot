import psycopg2
import os
from dotenv import load_dotenv
from loader import bot


load_dotenv()


class News:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("Host"),
            user=os.getenv("User"),
            password=os.getenv("Password"),
            database=os.getenv("Database")
        )
        self.cur = self.conn.cursor()

    def create_tabla(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Admin_news (
            photo TEXT,
            text VARCHAR(255),
            link VARCHAR(255)
        )
        """)

        self.conn.commit()
        print("[INFO] Tables created successfully")

    async def add_info(self, state):
        async with state.proxy() as data:
            self.cur.execute("INSERT INTO admin_news VALUES (%s, %s, %s)", tuple(data.values()))
            self.conn.commit()

    async def get_news(self):
        self.cur.execute("SELECT * FROM admin_news ORDER BY photo DESC LIMIT 1")
        rows = self.cur.fetchone()
        await bot.send_photo(chat_id=629990425, photo=rows[0], caption=rows[1] + " Link: " + str(rows[2]))



