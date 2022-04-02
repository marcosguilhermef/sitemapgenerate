import application.UrlMake
from dotenv import dotenv_values,find_dotenv
from bs4 import BeautifulSoup
config = dotenv_values(find_dotenv())


class SiteMapGenerate:
    def __init__(self):
        self.NumberFiles = None

    def save(self, nameFile,str):
        r = open(f'{config["SAVE_IMAGE_DIRECTORY"]}/{nameFile}.xml', "a")
        bs = BeautifulSoup(str, 'xml')
        r.write(str)
        r.close()

    def xml_wirite(self):
        url = application.UrlMake.UrlMake()
        urls = url.generate_url()
        TotalUrls = len(urls)
        self.NumberFiles = 0

        if TotalUrls % 50000:
            self.NumberFiles = (TotalUrls // 50000) + 1
        else:
            self.NumberFiles = TotalUrls // 50000

        for i in range(0, self.NumberFiles):
            start = i * 50000
            final = (i + 1) * 50000
            str = "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">"
            for x in range(start, final):
                try:
                    print(urls[x])
                    print(x)
                except IndexError:
                    print("final")
                    break
                str = str + "\
                        <url>\
                            <loc>" + urls[x]["url"] + "</loc>\
                            <lastmod>" + urls[x]["lastmod"] + "</lastmod>\
                            <changefreq>daily</changefreq>\
                            <priority>1.0</priority>\
                        </url>"
            str = str + "</urlset>"
            self.save(f'sitemap_{i}', str)
            str = ""

