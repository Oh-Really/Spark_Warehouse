# Spark_Warehouse

## Introduction
Music app Sparkify are looking to move their data, and databases, into the cloud. Once the data is in S3 buckets (containing song, log, and log_json data), the data is to be moved to staging tables within a redshift cluster, before finally being placed into a set of dimensional tables for analytics purposes within a data warehouse.


## Usage
To start this project, you need to first create an IAM user which has redshift and S3 permissions. Once you have created the user and created an access key, update the KEY and SECRET variables within the dwh.cfg file.

One then needs to follow instructions within the *create_and_delete_cluster* notebook to create the redshift cluster, which does so using the boto3 package. Once you have confirmed the cluster exists and is available, you then need to update dwh.cfg file again with the hostname to the cluster and the ARN. You are now ready to create tables within this redshift cluster.

Next, you can run the create_tables.py module which will firstly delete any tables if they already exist, then proceed to create the staging and dimensional tables with appropriate schema. If this file runs successfully, one can check whether these tables exist via the Query Editor in AWS Redshift for your specific cluster.

Finally, run the etl.py module which first copies data from the S3 buckets into the staging tables via the COPY command, and then subsequently transforms and cleans the data before being entered into the data warehouse dimension and fact table.

### Files
* `create_and_delete_cluster.ipynb`
  * This jupyter notebook is used to create the redshift cluster, and deleting it once finished
  * Follow the file for instructions on how to create the cluster and the roles associated to it

* `dwh.cfg`
  * Edit the file to include your IAM user key and secret key
  * Also need to add in the host name of the cluster and associated ARN

* `create_tables.py`
  * You run this python script after creating and confirming the cluster is setup
  * This file creates the 2 staging tables which is **_staging_songs_** and **_staging_events_** tables to store the s3 staged log and songs data
  * The file then creates the 4 dimensions and fact table to transfer the data from the staging tables to
  * The sql queries executed within this module are found within `sql_queries.py`

* `etl.py`
  * Call this script to transfer the data from the s3 json files to the staging tables
  * The data is then cleaned and inut into the final dimension and fact tables

* `sql_queries.py`
  * Contains all sql queries executed in both `create_tables.py` and `etl.py`
