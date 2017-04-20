# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class LagouJobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    positionId = Field()
    positionName = Field()
    education = Field()
    city = Field()
    salary = Field()
    industryField = Field()
    workYear = Field()
    companySize = Field()
    financeStage = Field()
    description = Field()
