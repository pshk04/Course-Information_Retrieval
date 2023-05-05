import scrapy


class QuotesSpider(scrapy.Spider):
    name = "archiv"
    start_urls = [
        'https://arxiv.org/abs/1904.00103',
    ]

    def parse(self, response):
        for quote in response.css('div.leftcolumn'):
            yield {
                'title': quote.css('h1.mathjax::text').getall(),
                'authors': quote.css('div.authors a::text').getall(),
                'description': quote.css('blockquote::text').get(),
                'subject': quote.css('div.metatable span.primary-subject::text').get(),
                'pdf': "https://arxiv.org"+response.css('div.full-text a::attr(href)').get()+".pdf",
                'submission': quote.css('div.submission-history::text').getall(),
            }

        for href in response.css('span.arrow a::attr(href)'):
            yield response.follow(href, callback=self.parse)        




            