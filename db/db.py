import os
from dotenv import load_dotenv

import mysql.connector

class Db:
    def __init__(self):
        load_dotenv()
        self.__db = mysql.connector.connect(
            host =      os.getenv("DB_HOST"),
            user =      os.getenv("DB_USER"),
            password =  os.getenv("DB_PASSWORD"),
            database =  os.getenv("DB_DATABSE")
        )

    def __get_db(self):
        return self.__db
    
    def add_user(self, discord_id: int, username: str):
        user_by_discord_id = self.search_by_discord_id(discord_id)
        if user_by_discord_id != None:
            # Y'a déja un compte associé avec le discord
            raise Exception("Discord ID already used")
        
        try:
            conn = self.__get_db()
            cursor = conn.cursor()

            query = "INSERT INTO users (discord_id, username) VALUES (%s, %s)"
            cursor.execute(query, (discord_id, username))
            conn.commit()
            
            success = cursor.rowcount > 0
            cursor.close()
            return success
        except mysql.connector.Error as e:
            print(f"[DB ERROR (add_user)] {e}")
            return False
        
    def search_by_discord_id(self, discord_id: int):
        try:
            conn = self.__get_db()
            cursor = conn.cursor()
            query = "SELECT id FROM users WHERE discord_id = %s"
            cursor.execute(query, (discord_id, ))
            
            result = cursor.fetchone()
            cursor.close()

            return result
        except mysql.connector.Error as e:
            print(f"[DB ERROR (search_by_discord_id)] {e}")
            return False 
