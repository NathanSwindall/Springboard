import scrapy
# I think it would be cool to extract data from somewebsite you need to log into
# possible project
# check out the documentation for how to do forms easier

class FormsSpider(scrapy.Spider):
    name = 'forms'
    login_url = 'http://quotes.toscrape.com/login'
    #allowed_domains = ['toscrape.com'] I don't think we need this part it seems
    start_urls = [login_url]

    def parse(self, response):
        # extract the csrf token value
        token = response.css('input[name="csrf_token"]::attr(value)').extract_first()
        # create a python dictionary with the form values
        data = {
            'csrf_token': token,
            'username':'abc',
            'password':'abc',
        }
        # submit a Post request to it
        yield scrapy.FormRequest(url= self.login_url, formdata= data, callback= self.parse_quotes)
        
    def parse_quotes(self, response):
        """Parse the maain page after the spider is logged in"""
        for q in response.css('div.quote'):
            yield {
                'author_name': q.css('small.author::text').extract_first(),
                'author_url': q.css(
                    'small.author ~ a[href*="goodreads.com"]::attr(href)' # I am not sure what ~ means or *= means
                ).extract_first()
            }
            
            
    