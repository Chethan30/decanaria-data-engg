import csv
import psycopg2
import pymongo

# Define the connection parameters for postgres
postgres_db = 'jobs_project'
postgres_user = 'postgres'
postgres_password = 'postgres'
postgres_host = 'postgresql'
postgres_port = '5432'

table_nmae = 'raw_table'

# Define the connection parameters for mongo
mongo_host = 'mongodb'
mongo_port = '27017'
mongo_db = 'jobs_project'
mongo_collection = 'raw_collection'
mongo_password = 'password'

def connect_to_postgres_db():
    """
    Connect to postgres database
    """
    try:
        conn = psycopg2.connect(
            dbname=postgres_db,
            user=postgres_user,
            password=postgres_password,
            host=postgres_host,
            port=postgres_port
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
    
def connect_to_mongo_db():
    """
    Connect to mongo database
    """
    try:
        client = pymongo.MongoClient(f"mongodb://{mongo_host}@{mongo_password}:{mongo_port}/")
        db = client[mongo_db]
        return db
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
    
def fetch_data(conn, table_name):
    """
    Fetch data from table
    """
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table_name}")
        data = cur.fetchall()
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    finally:
        cur.close()

def fetch_data_from_mongo(db, collection_name):
    """
    Fetch data from mongo collection
    """
    try:
        collection = db[collection_name]
        data = collection.find()
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def save_csv(data, filename):
    """
    Save data to csv file
    """
    try:
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(data)
    except Exception as e:
        print(f"Error saving data to csv: {e}")
        return None
    
def save_mongo_data_to_csv(data, filename):
    """
    Save mongo data to csv file
    """
    try:
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            for doc in data:
                writer.writerow(doc.values())
    except Exception as e:
        print(f"Error saving data to csv: {e}")
        return None

def main(self):
    """
    Read data from postgres and write to csv
    """
    conn = connect_to_postgres_db()
    # conn = connect_to_mongo_db()
    if not conn:
        return
    
    data = fetch_data(conn, self.table_name)
    # data = fetch_data_from_mongo(conn, self.mongo_collection)
    if not data:
        return
    
    output_filename = 'data.csv'
    save_csv(data, output_filename)
    # save_mongo_data_to_csv(data, output_filename)
    print("Data saved to csv file successfully")

if __name__ == "__main__":
    main()
