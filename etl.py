import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn) -> None:
    """
    Load the data from s3 buckets into staging tables.
    Paramaters
    ----------
    cur: Database cursoer object
    conn: Database connection object
    """
    cur: 
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn)-> None:
    """
    Insert data into fact and dimension tables from staging tables
    Paramaters
    ----------
    cur: Database cursoer object
    conn: Database connection object
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():    
    """
    Create cursor and connection db objects, then call load_staging_tables and insert_tables
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
