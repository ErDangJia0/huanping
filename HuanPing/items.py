# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuanpingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    proName = scrapy.Field()  # 项目名称
    place = scrapy.Field()  # 建设地点
    prodName = scrapy.Field()  # 建设单位
    sName = scrapy.Field()  # 环评机构
    sFile = scrapy.Field()  # 报告书链接
    dqspzt = scrapy.Field()  # 审批状态
    acceptDate = scrapy.Field()  # 受理时间
    sp_date = scrapy.Field()  # 审批时间
