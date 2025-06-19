## Preparation

Create the conda environment based on the `environment.yml` file. 
We will also be using google cloud acocunt for this project. 

```
conda env update -f environment.yml
conda activate dwh
pip install -r requirements.txt
```

Create project in Google Cloud Console

Download the csv files from https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Clean the data with data_clean.py (located in ~/olist/notebook/) script. 

Upload all cleaned csv files to buckets in Google Cloud

```
#!/bin/bash

# Variables - set these to your values
LOCAL_DIR="/path/to/your/csvs"
GCS_BUCKET="your-bucket"
GCS_PATH="path/in/bucket"  # Optional: folder in the bucket

# Upload all CSV files from the local directory to the GCS bucket
gsutil cp "$LOCAL_DIR"/*.csv gs://$GCS_BUCKET/$GCS_PATH/

```
Then load the csv file to BigQuery

```
#!/bin/bash

# Variables - set these to your values
PROJECT_ID="your-gcp-project-id"
DATASET="your_dataset"
TABLE="your_table"
GCS_BUCKET="your-bucket"
GCS_PATH="path/to/csvs"  # Folder in the bucket containing CSVs

# Optional: schema file (remove --autodetect if you use this)
# SCHEMA="name:STRING,age:INTEGER"

# Load all CSV files in the folder (wildcard)

bq load \
  --project_id="$PROJECT_ID" \
  --source_format=CSV \
  --autodetect \
  --skip_leading_rows=1 \
  "$DATASET.$TABLE" \
  "gs://$GCS_BUCKET/$GCS_PATH/*.csv"
```

Transform the csv files to tables/views in BigQuery by DBT. 

### Note: 

The zip code prefix is 5 digits, but if let goolge handle the schema automatically, all zip codes starts with 0 will be reduced to 4 digits, so please set the schema manually and change the zip code data type to string.

### Finding:

There is "customer id" and "customer unique id" fields in the customer dataset, when checked other datasets, only "customer id" field was used, "customer unique id" field could be ignored. 

```
dbt init olist
```
By default, dbt will update the profiles.yml file in the .dbt directory. This can be overridden by profiles.yml in the project directory, in this case, the project directory is m2_project which was created by dbt init.

In GCP IAM, create a google service account for this project and download the key file, save the key file in the safe directory (such as .secrets/gcp_key.json)

```
dbt debug
```
Verify the connection to the database and all checks passed.

### Business case and problem statement

Through EDA analysis, I noticed the delivery time was not consistent across all regions, since the zip code and geolocation data wasd provided, I decided to use the zip code to group the data and calculate the average delivery time for each region. 

Based on the analysis, I deisgned schema to calculate the average delivery time for each region. The fact table is the delivery time data, and the dimension tables are the zip code and geolocation data. For geoclocation dataset, it is many to many relationship with zip code, so I used the zip code as the primary key in the geolocation table, for all the latitude and longitude data, I use the average value pair for latitude and longitude for each zip code. 

I tested the idea with jupyter notebook and found it is feasible. Then with the help of Amazon Q assistant, I deisgn and implement the dashboard.