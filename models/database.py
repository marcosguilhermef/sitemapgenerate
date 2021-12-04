import pymongo


class Connect:
    def __init__(self):
        self.conn_str = "mongodb://localhost:27017"
        self.client = pymongo.MongoClient(self.conn_str)
        self.database = self.client["gruposWhatsapp"]

    def test_connection(self):
        try:
            print(self.client.server_info())
        except Exception:
            print("Unable to connect to the server.")
