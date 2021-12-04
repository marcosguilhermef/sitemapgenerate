import pymongo
from dotenv import dotenv_values
config = dotenv_values(".env")

class Connect:
    def __init__(self):
        if (config["MONGO_USER"] and config["MONGO_PASSWORD"]):
            self.conn_str = f'mongodb://{config["MONGO_USER"]}:{config["MONGO_PASSWORD"]}@{config["MONGO_ADDRESS"]}:{config["MONGO_PORT"]}'
        else:
            self.conn_str = f'mongodb://{config["MONGO_ADDRESS"]}:{config["MONGO_PORT"]}'
        self.client = pymongo.MongoClient(self.conn_str)
        self.database = self.client["gruposWhatsapp"]

    def test_connection(self):
        try:
            print(self.client.server_info())
        except Exception:
            print("Unable to connect to the server.")