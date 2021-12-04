import models.URLs
import re
import datetime


class UrlMake:
    def __init__(self):
        self.URL = models.URLs.URLs()
        pass

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
        return arr
