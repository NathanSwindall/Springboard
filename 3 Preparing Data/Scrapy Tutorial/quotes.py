import scrapy
# to create a new spider: scrapy genspider quotes.py toscrape.com
# to runspider: scrapy runspider quotes.py 
# to run and put into json file: scrapy runspider quotes.py -o quotes.json

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.log("Hello I am here")
        for quote in response.css('div.quote'):
            self.log("in the for loop right now")
            item = {
                'author_name': quote.css('small.author::text').extract_first(),
                'text': quote.css('span.text::text').extract_first(),
                'tags': quote.css('a.tag::text').extract(),
            }
            yield item
        #add pagination part to the code
        next_page_url = response.css('li.next > a::attr(href)').extract_first() #go to list item with class next, from there go to the a and get the attr(href)
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
