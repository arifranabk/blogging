from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

class DBConnector:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "127.0.0.1")
        self.port = os.getenv("DB_PORT", "3306")
        self.user = os.getenv("DB_USERNAME", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        self.database = os.getenv("DB_DATABASE", "laravel_site")
        self.engine = None

    def connect(self):
        # Default to MySQL for now, easy to switch to Postgres
        connection_string = f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        try:
            self.engine = create_engine(connection_string)
            with self.engine.connect() as conn:
                result = conn.execute(text("SELECT 1"))
                print("Database connection successful!")
        except Exception as e:
            print(f"Database connection failed: {e}")

    def fetch_pages(self):
        query = "SELECT * FROM pages"
        # Implementation depends on actual schema
        pass

    def fetch_seos(self):
        query = "SELECT * FROM seos"
        # Implementation depends on actual schema
        pass
