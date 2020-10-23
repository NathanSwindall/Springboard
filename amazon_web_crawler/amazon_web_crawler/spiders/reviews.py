import scrapy


class ReviewsSpider(scrapy.Spider):
    name = 'reviews'
    farsi_url = "https://www.amazon.com/s?k=farsi+language&i=stripbooks&ref=nb_sb_noss&page={}"
    start_urls = [farsi_url.format(1)]

    def parse(self, response):
        boxes = response.css("div.s-include-content-margin.s-border-bottom.s-latency-cf-section")
        for box in boxes:
            link = box.css('a.a-link-normal.a-text-normal').attrib['href']
            self.log(link)
