# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

# TODO: Update with MongoDB connection (Optional)

class JobsProjectPipeline:

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = 'password'
        database = 'jobs_project'
        self.connection = psycopg2.connect(
            host=hostname,
            user=username,
            password=password,
            dbname=database)
        self.cur = self.connection.cursor()


    def process_item(self, item, spider):
        try:
            # TODO: Update insert into sql command with all the data
            # self.cur.execute("INSERT INTO jobs (slug, language, languages, req_id, title, description, street_address, city, state, country_code, postal_code, location_type, latitude, longitude, categories, tags, brand, promotion_value, salary_currency, salary_value, salary_min_value, salary_max_value, benefits) VALUES (%")
            self.connection.commit()
        except:
            self.connection.rollback()
            raise
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()