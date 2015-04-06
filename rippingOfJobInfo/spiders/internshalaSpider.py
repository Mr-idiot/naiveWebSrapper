from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import bleach , re
from scrapy.http import Request
from  rippingOfJobInfo.items import RippingofjobinfoItem

class InternshalaSpider(CrawlSpider):
    name = 'internshala'
    allowed_domains = ['http://internshala.com/internships/']
    start_urls = [
            "http://internshala.com/internships/"
            ,"http://internshala.com/internships/page-2"
                ]
    
   
    
    def parse(self, response):
        
        items = []
        det = []
        sel = Selector(response)
        # Accessing main Job Div with class 'Container-Fluid individual_internship'
      
        jobs = sel.xpath("//div[@class='container-fluid individual_internship']")
        
        for job in jobs:
            item = RippingofjobinfoItem()
            item['job_title'] = job.xpath("normalize-space(.//h4[@title]/text())").extract()
            item['job_at'] = job.xpath("normalize-space(.//h4/a[@title]/text())").extract()
            item['job_location'] = job.xpath("normalize-space(.//div[@class='individual_internship_details']//p//span//a/text())").extract()
            job_detail = job.xpath(".//div[@class='individual_internship_details']//div//table//tbody//text()").extract()
            for j in job_detail:
                x = bleach.clean(j, strip=True)
                if len(x.strip()) == 0:
                    pass
                
                else: 
                     det.append(x)
                     
             
            item['job_start_date'] = det[0]
            item['job_duration'] = det[1]
            item['job_stipend']=det[2]
            item['job_posted_on'] = det[3]
            item['job_stipend']=det[4]
            
            items.append(item)
            
       
        
        return items
    
             