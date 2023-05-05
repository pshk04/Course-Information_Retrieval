import scrapy


class QuotesSpider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        urls = [
            'https://arxiv.org/abs/1901.00001',
            'https://arxiv.org/abs/1901.00003',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)