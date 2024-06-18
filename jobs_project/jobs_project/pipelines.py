# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
import json

# TODO: Update with MongoDB connection (Optional)

class JobsProjectPipeline:
    dummy = "dummy value"

    def __init__(self):
        hostname = 'postgresql'
        username = 'postgres'
        password = 'postgres'
        database = 'jobs_project'
        port = '5432'
        self.connection = psycopg2.connect(
            host=hostname,
            user=username,
            password=password,
            dbname=database,
            port=port)
        
        self.cur = self.connection.cursor()


#         self.cur.execute("""
#             CREATE TABLE IF NOT EXISTS jobs (
#                 id SERIAL PRIMARY KEY,
#                 slug TEXT,
#                 language TEXT,
#                 languages TEXT,
#                 req_id TEXT,
#                 title VARCHAR(255),
#                 description TEXT,
#                 street_address TEXT,
#                 city TEXT,
#                 state TEXT,
#                 country_code TEXT,
#                 postal_code TEXT,
#                 location_type TEXT,
#                 latitude TEXT,
#                 longitude TEXT,
#                 categories TEXT,
#                 tags TEXT,
#                 tags1 TEXT,
#                 tags2 TEXT,
#                 tags5 TEXT,
#                 tags6 TEXT,
#                 tags8 TEXT,
#                 brand TEXT,
#                 promotion_value TEXT,
#                 salary_currency TEXT,
#                 salary_value TEXT,
#                 salary_min_value TEXT,
#                 salary_max_value TEXT,
#                 benefits TEXT,
#                 employment_type TEXT,
#                 hiring_organization TEXT,
#                 source TEXT,
#                 apply_url TEXT,
#                 internal TEXT,
#                 searchable TEXT,
#                 applyable TEXT,
#                 li_easy_applyable TEXT,
#                 ats_code TEXT,
#                 meta_data TEXT,
#                 update_date TEXT,
#                 create_date TEXT,
#                 category TEXT,
#                 full_location TEXT,
#                 short_location TEXT,
#                 location_name TEXT,
#                 department TEXT,
#                 recruiter_id TEXT,
#                 posted_date TEXT,
#                 posting_expiry_date TEXT,
#                 work_hours TEXT,
#                 salary_frequency TEXT)
#  """)
        
        self.cur.execute("""DROP TABLE IF EXISTS jobs2""")
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS jobs2 (
                         id SERIAL PRIMARY KEY,
                         slug TEXT,
                         req_id TEXT,
                         title VARCHAR(255),
                         description TEXT,
                         street_address TEXT,
                         city TEXT,
                         state TEXT,
                         country_code TEXT,
                         postal_code TEXT,
                         location_type TEXT,
                         latitude TEXT,
                         longitude TEXT,
                         categories TEXT,
                         tags TEXT,
                         brand TEXT,
                         promotion_value TEXT,
                         salary_currency TEXT,
                         salary_value TEXT,
                         salary_min_value TEXT,
                         salary_max_value TEXT,
                         benefits TEXT,
                         employment_type TEXT,
                         hiring_organization TEXT,
                         source TEXT,
                         apply_url TEXT,
                         internal TEXT,
                         searchable TEXT,
                         applyable TEXT,
                         li_easy_applyable TEXT,
                         ats_code TEXT,
                         meta_data TEXT,
                         update_date TEXT,
                         create_date TEXT,
                         category TEXT,
                         full_location TEXT,
                         short_location TEXT,
                         location_name TEXT,
                         department TEXT,
                         recruiter_id TEXT,
                         posted_date TEXT,
                         posting_expiry_date TEXT,
                         work_hours TEXT,
                         salary_frequency TEXT
                         )""")
        self.connection.commit()

    def list2string(self, lst):
        return ", ".join(str(l) for l in lst)

    def open_spider(self, spider):
        pass


    def process_item(self, item, spider):
        try:
            insert_query = f"""INSERT INTO jobs2 (
                slug, title, description, street_address, city, state, country_code, 
                postal_code, location_type, latitude, longitude, categories, tags, brand, promotion_value,
                salary_currency, salary_value, salary_min_value, salary_max_value, benefits, employment_type,
                hiring_organization, source, apply_url, internal, searchable, applyable,
                li_easy_applyable, ats_code, meta_data, update_date, create_date, category, full_location,
                short_location, location_name, department, recruiter_id, posted_date, posting_expiry_date,
                work_hours, salary_frequency
                ) VALUES (
                '{item['slug']}',
                '{item['title']}',
                '{item['description']}',
                '{item['street_address']}',
                '{item['city']}',
                '{item['state']}',
                '{item['country_code']}',
                '{item['postal_code']}',
                '{item['location_type']}',
                '{item['latitude']}',
                '{item['longitude']}',
                '{item['categories']}',
                '{item['tags']}',
                '{item['brand']}',
                '{item['promotion_value']}',
                '{item.get('salary_currency', "NA")}',
                '{item.get('salary_value', "NA")}',
                '{item.get('salary_min_value', "NA")}',
                '{item.get('salary_max_value', "NA")}',
                '{item.get('benefits', "NA")}',
                '{item.get('employment_type', "NA")}',
                '{item.get('hiring_organization', "NA")}',
                '{item.get('source', "NA")}',
                '{item.get('apply_url', "NA")}',
                '{item.get('internal', "NA")}',
                '{item.get('searchable', "NA")}',
                '{item.get('applyable', "NA")}',
                '{item.get('li_easy_applyable', "NA")}',
                '{item.get('ats_code', "NA")}',
                '{item.get('meta_data', "NA")}',
                '{item.get('update_date', "NA")}',
                '{item.get('create_date', "NA")}',
                '{item.get('category', "NA")}',
                '{item.get('full_location', "NA")}',
                '{item.get('short_location', "NA")}',
                '{item.get('location_name', "NA")}',
                '{item.get('department', "NA")}',
                '{item.get('recruiter_id', "NA")}',
                '{item.get('posted_date', "NA")}',
                '{item.get('posting_expiry_date', "NA")}',
                '{item.get('work_hours', "NA")}',
                '{item.get('salary_frequency', "NA")}'
                 )"""
            self.cur.execute(insert_query)
            self.connection.commit()
        except:
            self.connection.rollback()
            raise
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()



# insert_query = f"""INSERT INTO jobs VALUES (
            #     {item['slug']},
            #     {str(item.get('language', ""))},
            #     {self.list2string(item.get('languages', ""))},
            #     {item['req_id']},
            #     {str(item['title'])},
            #     {item['description']},
            #     {item['street_address']},
            #     {item['city']},
            #     {item['state']},
            #     {item['country_code']},
            #     {item['postal_code']},
            #     {item['location_type']},
            #     {item['latitude']},
            #     {item['longitude']},
            #     {str(item.get('categories', ""))},
            #     {self.list2string(item.get('tags', ""))},
            #     {self.list2string(item.get('tags1', ""))},
            #     {self.list2string(item.get('tags2', ""))},
            #     {self.list2string(item.get('tags5', ""))},
            #     {self.list2string(item.get('tags6', ""))},
            #     {self.list2string(item.get('tags8', ""))},
            #     {item.get('brand', "")},
            #     {item.get('promotion_value', "")},
            #     {str(item.get('salary_currency', ""))},
            #     {item.get('salary_value', "")},
            #     {item.get('salary_min_value', "")},
            #     {item.get('salary_max_value', "")},
            #     {item.get('benefits', "")},
            #     {item.get('employment_type', "")},
            #     {item.get('hiring_organization', "")},
            #     {item.get('source', "")},
            #     {item.get('apply_url', "")},
            #     {item.get('internal', "")},
            #     {item.get('searchable', "")},
            #     {item.get('applyable', "")},
            #     {item.get('li_easy_applyable', "")},
            #     {item.get('ats_code', "")},
            #     {str(item.get('meta_data', ""))},
            #     {item.get('update_date', "")},
            #     {item.get('create_date', "")},
            #     {item.get('category', "")},
            #     {item.get('full_location', "")},
            #     {item.get('short_location', "")},
            #     {item.get('location_name', "")},
            #     {item.get('department', "")},
            #     {item.get('recruiter_id', "")},
            #     {item.get('posted_date', "")},
            #     {item.get('posting_expiry_date', "")},
            #     {item.get('work_hours', "")},
            #     {item.get('salary_frequency', "")}
            #     )"""