import scrapy
#remember the scrapy shell is pretty cool
# fetch(url) to change the url in scrapy shell
# scrapy runspider details.py -o details.json   -> This is to run the file
# This can get all the stuff for infinite scrolling websites. I think it would be cool to pull youtube data using this spider
# Let's try to make a scrapy tool for youtube

class DetailsPySpider(scrapy.Spider):
    name = 'details'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        urls = response.css('div.quote > span > a::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)
        next_page_url = response.css('li.next > a::attr(href)').extract_first() 
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
     
    
    def parse_details(self,response):
        yield {
        'name' : response.css('h3.author-title::text').extract_first(),
        'birth_date': response.css('span.author-born-date::text').extract_first(),
        }
            
            
            
            
            
                       
            

