import os
from dotenv import load_dotenv
import mysql.connector

class Db:
    def __init__(self):
        load_dotenv()

    def __create_connection(self):
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABSE")
        )

    def get_discord_id_users(self):
        try:
            conn = self.__create_connection()
            cursor = conn.cursor()
            query = "SELECT DISTINCT discord_id FROM users"
            cursor.execute(query)
            result = [row[0] for row in cursor.fetchall()]
            cursor.close()
            conn.close()
            return result
        except mysql.connector.Error as e:
            print(f"[DB ERROR (get_discord_id_users)] {e}")
            return []

    def search_by_discord_id(self, discord_id: int):
        try:
            conn = self.__create_connection()
            cursor = conn.cursor()
            query = "SELECT id FROM users WHERE discord_id = %s"
            cursor.execute(query, (discord_id,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            return result[0] if result else None
        except mysql.connector.Error as e:
            print(f"[DB ERROR (search_by_discord_id)] {e}")
            return None

    def search_by_username(self, username: str):
        try:
            conn = self.__create_connection()
            cursor = conn.cursor()
            query = "SELECT id FROM users WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            return result[0] if result else None
        except mysql.connector.Error as e:
            print(f"[DB ERROR (search_by_username)] {e}")
            return None

    def add_user(self, discord_id: int, username: str):
        user_exists = self.search_by_discord_id(discord_id)
        if user_exists is not None:
            raise Exception("Discord ID already used")

        try:
            conn = self.__create_connection()
            cursor = conn.cursor()
            query = "INSERT INTO users (discord_id, username) VALUES (%s, %s)"
            cursor.execute(query, (discord_id, username))
            conn.commit()
            success = cursor.rowcount > 0
            cursor.close()
            conn.close()
            return success
        except mysql.connector.Error as e:
            print(f"[DB ERROR (add_user)] {e}")
            return False

    def add_account(self, discord_id: int, mail: str, password: str):
        try:
            user_id = self.search_by_discord_id(discord_id)
            if user_id is None:
                raise Exception("Aucun utilisateur lié à ce Discord")

            conn = self.__create_connection()
            cursor = conn.cursor()
            query = "INSERT INTO fivem_accounts (user_id, mail, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, mail, password))
            conn.commit()
            success = cursor.rowcount > 0
            cursor.close()
            conn.close()
            return success
        except mysql.connector.Error as e:
            print(f"[DB ERROR (add_account)] {e}")
            return False

    def get_accounts_discord_id(self, discord_id: int):
        try:
            user_id = self.search_by_discord_id(discord_id)
            if user_id is None:
                return []

            conn = self.__create_connection()
            cursor = conn.cursor()
            query = "SELECT mail, password FROM fivem_accounts WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            return results
        except mysql.connector.Error as e:
            print(f"[DB ERROR (get_accounts_discord_id)] {e}")
            return []