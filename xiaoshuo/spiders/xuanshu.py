import scrapy
from ..items import XiaoshuoItem


class XuanshuSpider(scrapy.Spider):
    name = 'xuanshu'
    allowed_domains = ['xuanshu.com']
    start_urls = ['http://www.xuanshu.com/book/7199/2069117.html']

    def parse(self, response):
        item = XiaoshuoItem()
        item["title"] = response.xpath("//div[@class='txt_cont']/h1/text()").get()
        item["content"] = response.xpath("//div[@id='content1']/text()").extract()
        yield item
        next_url = response.xpath("//div[@class='txt_lian']/a[4]/@href").get()
        # print(next_url)
        if next_url is not None and next_url != "/book/7199/":
            next_url = "http://www.xuanshu.com/book/7199/" + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
        # ch_list = response.xpath("//div[@class='pc_list']/ul/li")
        # for ch in ch_list:
        #     url = ch.xpath("./a/@href").get()
        #     if url is not None:
        #         url = "http://www.xuanshu.com/book/7199/" + url
        #         yield scrapy.Request(
        #             url,
        #             callback=self.parse_text
        #         )

    # def parse_text(self, response):
    #     item = XiaoshuoItem()
    #     item["content"] = response.xpath("//div[@id='content1']/text()").extract()
    #     yield item
