import scrapy
# I think it would be cool to extract data from somewebsite you need to log into
# possible project
# This form2 makes working with forms a lot easier

class FormsSpider(scrapy.Spider):
    name = 'forms2'
    login_url = 'http://quotes.toscrape.com/login'
    #allowed_domains = ['toscrape.com'] I don't think we need this part it seems
    start_urls = [login_url]

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.parse_quotes
        )

        
    def parse_quotes(self, response):
        """Parse the maain page after the spider is logged in"""
        for q in response.css('div.quote'):
            yield {
                'author_name': q.css('small.author::text').extract_first(),
                'author_url': q.css(
                    'small.author ~ a[href*="goodreads.com"]::attr(href)' # I am not sure what ~ means or *= means
                ).extract_first()
            }
            
            
    
