import pymongo
from dotenv import dotenv_values, find_dotenv
import urllib.parse
from sshtunnel import SSHTunnelForwarder

config = dotenv_values(find_dotenv())


class Connect:
    def __init__(self):
        """server = SSHTunnelForwarder(
            ("34.123.3.51", 22),
            ssh_username="origin",
            ssh_password="!@%17aBc",
            ssh_pkey="/media/micos/Data/Chaves/ssh/id_rsa",
            ssh_private_key_password="!@%17aBc",
            remote_bind_address=('localhost', 27017)
        )
        server.start()
        server.local_bind_port
        """

        if config["MONGO_USER"] and config["MONGO_PASSWORD"]:
            self.conn_str = f'mongodb://{config["MONGO_USER"]}:{urllib.parse.quote(config["MONGO_PASSWORD"], safe="")}@{config["MONGO_ADDRESS"]}:{config["MONGO_PORT"]}'
        else:
            self.conn_str = f'mongodb://{config["MONGO_ADDRESS"]}:{config["MONGO_PORT"]}'
        self.client = pymongo.MongoClient(self.conn_str)
        self.database = self.client["gruposWhatsapp"]

    def test_connection(self):
        try:
            print(self.client.server_info())
        except Exception:
            print("Unable to connect to the server.")
