import os
from dotenv import load_dotenv

class Token:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv("DISCORD_TOKEN")

    def getToken(self):
        if self.token:
            return self.token