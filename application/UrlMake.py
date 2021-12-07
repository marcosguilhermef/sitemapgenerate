import models.URLs
import models.Categorias
import re
import datetime


class UrlMake:
    def __init__(self):
        self.URL = models.URLs.URLs()
        self.CATEGORIAS = models.Categorias.Categorias()

    def generate_url(self):
        arr = []
        for i in self.URL.select_all_active_urls():
            try:
                data = i["updated_at"]
            except KeyError:
                data = i["created_at"]
            arr.append({
                "lastmod": data.strftime("%Y-%m-%d"),
                "url": "https://zapgrupos.xyz/" + re.sub(" ", "-", i["categoria"]) + "/" + str(i["_id"])
            })
        for i in self.CATEGORIAS.select_all_active_categories():
            try:
                data = i["updated_at"]
            except KeyError:
                try:
                    data = i["created_at"]
                except KeyError:
                    data = datetime.datetime.strptime('2021-12-01', '%Y-%m-%d')
            arr.append({
                "lastmod": data.strftime("%Y-%m-%d"),
                "url": "https://zapgrupos.xyz/" + re.sub(" ", "-", i["categoria"])
            })
        return arr

    def generate_one_url(self):
        register = list(self.URL.select_randon_active_urls())
        url = "https://zapgrupos.xyz/" + re.sub(" ", "-", register[0]["categoria"]) + "/" + str(register[0]["_id"])
        return url
