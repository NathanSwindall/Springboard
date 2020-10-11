import scrapy
import json

#when there is infinite scrolling you really don't have to parse the html
#you can use the json and just scroll through everything
# https://docs.python.org/3/tutorial/classes.html for class tutorial

class InfiniteScrollSpider(scrapy.Spider):
    name = 'infinite_scroll'
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    #allowed_domains = ['toscrap.com'] # This doesn't seem to be needed in the tutorial
    start_urls = [api_url.format(1)]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
            yield {
                'author_name': quote['author']['name'],
                'text': quote['text'],
                'tags': quote['tags']
            }
        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(url=self.api_url.format(next_page), callback= self.parse)
                    
