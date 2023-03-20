import scrapy
from cleantext import clean


class PoliticalEmailArchiveSpider(scrapy.Spider):

    name = "political_email_archive"

    allowed_domains = ["politicalemails.org"]
    start_urls = ["https://politicalemails.org/localities/27"]

    def parse(self, response):

        orgs = response.css('div.resource-list > a.resource-tease')

        for org in orgs:

            yield{
                'name': clean(org.css('div.resource-tease__title-right::text').get(), no_line_breaks=True),
                'url': org.css('a').attrib['href']
            }

        next_page = response.css('[rel="next"] ::attr(href)').get()

        if next_page is not None:
            next_page_url = next_page
            yield response.follow(next_page_url, callback=self.parse)