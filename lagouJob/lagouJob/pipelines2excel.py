# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#import xlwt
from openpyxl import Workbook


class LagouJobPipeline(object):
    wb = Workbook()
    ws = wb.active
    ws.append(['positionId', 'positionName', 'city', 'salary', 'education',
               'workYear', 'companySize', 'financeStage', 'industryField',
               'description'])

    def process_item(self, item, spider):
        #fileName = 'LagouPython.xls'
        #book = xlwt.Workbook(encoding='utf8')
        #sheet = book.add_sheet('pisition', cell_overwrite_ok=True)
        #sheet.write(0, 0, 'positionId'.encode('utf8'))
        #sheet.write(0, 1, 'positionName'.encode('utf8'))
        #sheet.write(0, 2, 'city'.encode('utf8'))
        #sheet.write(0, 3, 'salary'.encode('utf8'))
        #sheet.write(0, 4, 'education'.encode('utf8'))
        #sheet.write(0, 5, 'workYear'.encode('utf8'))
        #sheet.write(0, 6, 'companySize'.encode('utf8'))
        #sheet.write(0, 7, 'financeStage'.encode('utf8'))
        #sheet.write(0, 8, 'industryField'.encode('utf8'))
        #sheet.write(0, 9, 'description'.encode('utf8'))
        #i = 1
        #while i <= len(item):
        #    sheet.write(i, 0, item['positionId'])
        #    sheet.write(i, 1, item['positionName'])
        #    sheet.write(i, 2, item['city'])
        #    sheet.write(i, 3, item['salary'])
        #    sheet.write(i, 4, item['education'])
        #    sheet.write(i, 5, item['workYear'])
        #    sheet.write(i, 6, item['companySize'])
        #    sheet.write(i, 7, item['financeStage'])
        #    sheet.write(i, 8, item['industryField'])
        #    sheet.write(i, 9, item['description'])
        #    i += 1
        #book.save(fileName)
        fileName = 'LagouPython.xls'
        line = [item['positionId'], item['positionName'], item['city'], item['salary'],
                item['education'], item['workYear'], item['companySize'], item['financeStage'],
                item['industryField'], item['description']]
        self.ws.append(line)
        self.wb.save(fileName)
        return item
