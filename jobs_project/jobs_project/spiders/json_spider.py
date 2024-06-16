import json
from typing import Iterable
import scrapy
from jobs_project.items import JobsProjectItem

class Jobspider(scrapy.Spider):
    name = 'job_spider'
    # custom_settings =  {
    #     'ITEM_PIPELINES': {
    #         'local_spider.pipelines.JobsProjectPipeline': 300
    #     }
    # }

    def __init__(self, **kwargs):
        # TODO: Convert aboslute path to relative path
        self.json_path = 'D:\Projects\decanaria-data-engg\data_src\s01.json'
        pass

    def start_requests(self):
        # your code here
        # make sure you can send a request locally at the file
        # if you can't get this to work, do not waste too much time here
        # instead load the json file inside parse_page
        # with open(self.json_path, 'r') as f:
        #     data = json.load(f)
        url = f'file:///{self.json_path}'
        yield scrapy.Request( url=url, callback=self.parse_page)

    def parse_page(self, response):
        # your code here
		# load json files using response.text
        # loop over data
		# return items

        data = json.loads(response.text)
        jobs = data['jobs']
        
        for job in jobs:
            job_data = job.get('data')
            item = JobsProjectItem()
            item['slug'] = job_data['slug']
            item['language'] = job_data['language']
            item['languages'] = job_data['languages']
            item['req_id'] = job_data['req_id']
            item['title'] = job_data['title']
            item['description'] = job_data['description']
            item['street_address'] = job_data['street_address']
            item['city'] = job_data['city']
            item['state'] = job_data['state']
            item['country_code'] = job_data['country_code']
            item['postal_code'] = job_data['postal_code']
            item['location_type'] = job_data['location_type']
            item['latitude'] = job_data['latitude']
            item['longitude'] = job_data['longitude']
            item['categories'] = job_data['categories']
            item['tags'] = job_data['tags']
            item['brand'] = job_data['brand']
            item['promotion_value'] = job_data['promotion_value']
            item['salary_currency'] = job_data['salary_currency']
            item['salary_value'] = job_data['salary_value']
            item['salary_min_value'] = job_data['salary_min_value']
            item['salary_max_value'] = job_data['salary_max_value']
            item['benefits'] = job_data['benefits']
            item['employment_type'] = job_data['employment_type']
            item['hiring_organization'] = job_data['hiring_organization']
            item['source'] = job_data['source']
            item['apply_url'] = job_data['apply_url']
            item['internal'] = job_data['internal']
            item['searchable'] = job_data['searchable']
            item['applyable'] = job_data['applyable']
            item['li_easy_applyable'] = job_data['li_easy_applyable']
            item['ats_code'] = job_data['ats_code']
            item['meta_data'] = job_data['meta_data']
            item['update_date'] = job_data['update_date']
            item['create_date'] = job_data['create_date']
            item['category'] = job_data['category']
            item['full_location'] = job_data['full_location']
            item['short_location'] = job_data['short_location']
            yield item

