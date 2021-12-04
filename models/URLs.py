import models.database


class URLs(models.database.Connect):
    def __init__(self):
        super().__init__()
        self.collection = self.database["URLs"]

    def select_all_active_urls(self):
        arr = self.collection.find({"ativo": True})
        return arr


