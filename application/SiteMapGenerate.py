import application.UrlMake


class SiteMapGenerate:
    def __init__(self):
        pass

    def save(self):
        r = open("sitemap.xml", "a+")
        r.write(self.str)
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
