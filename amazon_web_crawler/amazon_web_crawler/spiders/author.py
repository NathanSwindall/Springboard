import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'
    farsi_url = "https://www.amazon.com/s?k=farsi+language&i=stripbooks&ref=nb_sb_noss&page={}"
    start_urls = [farsi_url.format(1)]

    def parse(self, response):
        boxes = response.css("div.s-include-content-margin.s-border-bottom.s-latency-cf-section")
        for box in boxes:
            
            # get the author
            box_author = box.css('div.a-row.a-size-base.a-color-secondary')
            author_string_date = box_author[0].css("span::text, a::text").getall()
            author_string_date = [a.strip() for a in author_string_date]
            
            # get the stars
            star_box = box.css('div.a-row.a-size-small')
            star_box = star_box.css('span::text').getall()
            star_box_text = [a.strip() for a in star_box]
            star_box_text = [a for a in star_box_text if a != ""]
            
            
            yield {
                'author': author_string_date,
                'stars' : star_box_text,
            }
        
        #div.a-row.a-size-small
        
        box1 = boxes[0].css('div.a-row.a-size-base.a-color-secondary')
        self.log(box1[0].css("span::text, a::text").getall())
        self.log("The length is of this one: " + str(len(box1)))

   