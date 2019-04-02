# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import HuanpingItem


class HuanpingSpider(scrapy.Spider):
    name = 'huanping'
    allowed_domains = ['http://hbj.taiyuan.gov.cn']
    url = 'http://hbj.taiyuan.gov.cn/intertidwebapp/custom/CustomJson'
    def start_requests(self):
        for page in range(1,14):
            form_data = {
                'chanId': '9246',
                'pageNum': str(page),
                'PageSize': '20',
                'items_type': '3',  # 区域
                'items': '5',
                'dqspzt': '1',  # 审批状态（1，2，3）
                'project_name': '',
                'orderby': 'accept_date desc'
            }

            yield scrapy.FormRequest(url=self.url, formdata=form_data, callback=self.parse)

    def parse(self, response):
        datas = json.loads(response.text)['list']['topics']
        for data in datas:
            item = HuanpingItem()
            item['proName'] = data['project_name']
            item['place'] = data['construction_place']
            item['prodName'] = data['construction_unit']
            item['sName'] = data['survey']
            item['sFile'] = 'http://hbj.taiyuan.gov.cn' + data['sqsb_file']
            item['dqspzt'] = data['dqspzt']
            item['acceptDate'] = data['accept_date']
            if 'sp_date' in data.keys():
                item['sp_date'] = data['sp_date']
            else:
                item['sp_date'] = '/'
            yield item
