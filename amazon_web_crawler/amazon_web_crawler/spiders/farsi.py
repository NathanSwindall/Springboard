import scrapy
import time

class FarsiSpider(scrapy.Spider):
    name = 'farsi'
    amazon_url = "https://www.amazon.com"
    farsi_url = "https://www.amazon.com/s?k=farsi+language&i=stripbooks&ref=nb_sb_noss&page={}"
    ##allowed_domains = ['amazon.com']
    start_urls = [farsi_url.format(1)]
    

    def parse(self, response):
        titles =  response.css('div.s-main-slot.s-result-list').css('span.a-size-medium.a-color-base.a-text-normal::text').extract()
        for title in titles:
            yield {"title": title}
        
        
        self.log(response.url[-2:])
        self.log("Hello, I'm here")
        
        next_page = int(response.url[-2:].replace("=","")) + 1
        # need a regular expression here it seems
        self.log(next_page)
        next_page_url = "/s?k=farsi+language&i=stripbooks&ref=nb_sb_noss&page={}".format(next_page)
        
        if next_page <= 75:
            next_page_url = response.urljoin(next_page_url)
            time.sleep(1)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        
        
#         try:
#             next_page_url = response.css("li.a-last > a").attrib['href']
#         except:
#             self.log(response.css("li.a-last"))
#             next_page_url = ""
          
        
#         if next_page_url:
#             time.sleep(1)
#             next_page_url = response.urljoin(next_page_url)
#             yield scrapy.Request(url=next_page_url, callback=self.parse)
