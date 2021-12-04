import models.database


class Categorias(models.database.Connect):
    def __init__(self):
        super().__init__()
        self.collection = self.database["Categorias"]

    def select_all_active_categories(self):
        arr = self.collection.find()
        return arr
