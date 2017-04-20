# -*- coding: utf-8 -*-
import scrapy
import json
import math
import re
from lagouJob.items import LagouJobItem
from scrapy.http import FormRequest
from scrapy.http import Request


class LagouSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["www.lagou.com"]

    def __init__(self):
        super(LagouSpider, self).__init__()
        self.url = 'http://www.lagou.com/jobs/positionAjax.json'
        self.cookies = {
            'user_trace_token': '20170411181328-8fb1a66930404e16b0b924d337ae6f5d',
            'index_location_city': '%E5%85%A8%E5%9B%BD',
            'SEARCH_ID': '9e999986dd2649b898aaddc02b630626',
            'JSESSIONID': '50495D980C9BCFBF594DA6AC14BAE855',
            'TG-TRACK-CODE': 'search_code',
            'LGSID': '20170420122346-2552ba5a-2581-11e7-b401-525400f775ce',
            'LGRID': '20170420122642-8e2762fe-2581-11e7-b405-525400f775ce',
            'LGUID': '20170411181328-81c29590-1e9f-11e7-9db9-5254005c3644',
            '_ga': 'GA1.2.1668151603.1491905609',
            '_gat': '1'
        }
        self.pn = 1

    def start_requests(self):
        yield FormRequest(self.url, formdata={'first': 'true', 'pn': str(self.pn), 'kd': 'python'},
                          callback=self.first_parse, cookies=self.cookies)

    def first_parse(self, response):
        jdict = json.loads(response.text)
        jcontent = jdict["content"]
        jposresult = jcontent["positionResult"]
        self.pn = math.ceil(jposresult['totalCount'] / jposresult['resultSize'])
        for n in range(2, int(self.pn) + 1):
            yield FormRequest(self.url, formdata={'first': 'false', 'pn': str(n), 'kd': 'python'},
                              callback=self.parse)
        yield self.parse(response)

    def parse(self, response):
        jdict = json.loads(response.text)
        jcontent = jdict["content"]
        jposresult = jcontent["positionResult"]
        jresult = jposresult["result"]
        for position in jresult:
            yield Request('https://www.lagou.com/jobs/' + str(position['positionId']) + '.html',
                          callback=self.description, meta={'position': position})

    @classmethod
    def description(cls, response):
        text = ''.join(response.css('.job_bt > div:nth-child(2) *::text').extract())
        text = re.sub('\s+', '', text)
        item = LagouJobItem()
        position = response.meta['position']
        item['positionId'] = position['positionId']
        item['positionName'] = position['positionName']
        item['education'] = position['education']
        item['city'] = position['city']
        item['salary'] = position['salary']
        item['industryField'] = position['industryField']
        item['workYear'] = position['workYear']
        item['companySize'] = position['companySize']
        item['financeStage'] = position['financeStage']
        item['description'] = text
        yield item
