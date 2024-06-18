## Setup Instructions

1. Clone the repository/ download the zip file and extract the contents.
2. Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

3. Run the following command to start the application:
   [Make sure of the docker-compose.yml file in the root directory of the project and that the docker is installed on the system with the daemon running.]

```bash
docker-compose up -d
```

4. All the service would now be setup and running. The services are as follows:

   - **Postgres**: http://localhost:5432
   - **MongoDb**: http://localhost:27017

5. The scrapy service immediately runs the spider and stores the data in the Postgres database. The data can be viewed by ssh-ing into the Postgres container and running the following commands:

```bash
psql -U postgres # To login to the database
psql \c jobs_project # To connect to the database
psql \l     # To list all the databases
psql \dt    # To list all the tables
SELECT * FROM raw_table; # To view the data in the table
```

It also stores the data in the MongoDB database. The data can be viewed by ssh-ing into the MongoDB container and running the following commands:

```bash
mongosh mongodb://mongodb:admin@password:27017 # To connect to the database
use jobs_project # To connect to the database
show collections # To list all the collections
db.raw_collection.find() # To view the data in the collection
```

5. To stop the services, run the following command:

   ```bash
   docker-compose down
   ```

## Pipeline Process

The pipeline process is simple at a glance, but houses its own complexities specially with handling different types of data. The process is as follows:

1. **Scrapy Spider**: The spider is responsible for scraping the data from the website. Here, it's being mocked by scraping a json file. The data is then passed to the item pipeline by creating an item.
2. **Item Pipeline**: The item pipeline is responsible for processing the data and storing it in the database. This requires 2 key classes, the Item and the Pipeline. The Item class is responsible for defining the data structure and the Pipeline class is responsible for logic for processing the data and storing it in the database. Here, the data is stored in both Postgres and MongoDB databases. This is where we handle the data transformation and data cleaning.
3. **Database**: The data is stored in both Postgres and MongoDB databases for further processing, applications and retrival. The data can be viewed by ssh-ing into the respective containers and running the commands mentioned above.

## Future Scope

1. **Data Cleaning and Transformation**: The data cleaning process can be further enhanced by adding more data cleaning steps and handling more edge cases.
2. **Speed and Robudtness**: This can be improved wither with a local frontier (any list, dict or set would work), hashed data structre like redis or a distributed queue like Kafka, primarily to avoid duplicates and to handle the data in a more efficient manner.
3. **Security**: Adidng more encryption measures, like,
   - Encrypting the data before storing it in the database.
   - Storing environment variables in a more secure manner using env_vars and secrets.
