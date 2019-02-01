# -*- coding: utf-8 -*-
import scrapy
from HR.items import HrItem

class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        item = HrItem()
        position_list = response.xpath("//table[@class='tablelist']//tr")[1:-1]
        for tr in position_list:
            item['position'] = tr.xpath("./td[1]/a/text()").extract_first()
            item['site'] = tr.xpath("./td[4]/text()").extract_first()
            item['num'] = tr.xpath("./td[3]/text()").extract_first()
            yield item
        
        next_url = response.xpath("//a[@id='next']/@href").extract_first()
        if next_url != 'javascript:;':
            next_url = 'https://hr.tencent.com/' + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )

            
