import scrapy

# inherits from scrapy.Spider which provides start_requests() to go through start_urls
class FlippaSpider(scrapy.Spider):
    name = 'flippa'
    #android apps
    # start_urls = ['https://flippa.com/apps/just-sold?property_type=android_app&page=1',
    #               'https://flippa.com/apps/just-sold?property_type=android_app&page=2']

    #ios apps
    start_urls = ['https://flippa.com/apps/just-sold?property_type=ios_app&page=1',
                  'https://flippa.com/apps/just-sold?property_type=ios_app&page=2']


    def parse(self, response):
        """proceed to other pages of the listings"""
        for page_url in response.css(r'a[class ~= Pagination___pageLink]::attr(href)').extract():
            page_url = response.urljoin(page_url)
            yield scrapy.Request(url=page_url, callback=self.parse)


        for fi in response.css(r'li.ListingResults___listingResult'):
            a_price = fi.css('span')[12]
            yield {
                'url' : fi.css('::attr(href)').extract_first(),
                'price' : a_price.css('::text').extract_first()
            }


