import application.UrlMake
from dotenv import dotenv_values,find_dotenv
from bs4 import BeautifulSoup
config = dotenv_values(find_dotenv())


class SiteMapGenerate:
    def __init__(self):
        pass

    def save(self):
        r = open(f'{config["SAVE_IMAGE_DIRECTORY"]}/sitemap.xml', "a+")
        bs = BeautifulSoup(self.str, 'xml')
        pretty_xml = bs.prettify()
        r.write(pretty_xml)
        r.close()

    def xml_wirite(self):
        url = application.UrlMake.UrlMake()
        str = "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">"
        for i in url.generate_url():
            str = str+"\
                  <url>\
                        <loc>"+i["url"]+"</loc>\
                        <lastmod>"+i["lastmod"]+"</lastmod>\
                        <changefreq>daily</changefreq>\
                        <priority>1.0</priority>\
                  </url>"
        self.str = str + "</urlset>"
        self.save()
        return self.str
