# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RippingofjobinfoItem(scrapy.Item):
    job_title = scrapy.Field()
    job_at = scrapy.Field()
    job_location = scrapy.Field()
    job_start_date = scrapy.Field()
    job_duration = scrapy.Field()
    job_application_duration = scrapy.Field()
    job_stipend = scrapy.Field()
    job_posted_on = scrapy.Field()
