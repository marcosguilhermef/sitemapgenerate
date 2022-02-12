import models.database
import random


class URLs(models.database.Connect):
    def __init__(self):
        super().__init__()
        self.collection = self.database["URLs"]
    def select_all_urls(self):
        arr = self.collection.find({})
        return arr

    def select_all_active_urls(self):
        arr = self.collection.find({"ativo": True})
        return arr

    def select_randon_active_urls(self):
        length = self.collection.count_documents({"ativo": True})
        print(length)
        arr = self.collection.find({"ativo": True}).limit(-1).skip(random.randrange(1, length))
        return arr

# A = URLs()

# print(list(A.select_randon_active_urls()))
