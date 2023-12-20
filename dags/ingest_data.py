from time import time
import os
import pandas as pd
from sqlalchemy import create_engine


def ingest_function (user, password, host, port, db, table_name, parquet_file):


    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    engine.connect()
    print("connected successfuly, inserting data............................" +'//'+ os.getcwd())
        
    # df_iter = pd.read_parquet(parquet_file, iterator=True, chunksize=100000)
    
    df = pd.read_parquet(parquet_file) 
    print("df created......")


    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    print("columns name inserted.......")

    chunck_size = 100000

    for i in range(0, len(df), chunck_size):

        if (i + chunck_size) <= len(df):
            chunk = df.iloc[i:i+chunck_size]
        else:
            chunk = df.iloc[i:len(df)]

        chunk.to_sql(name=table_name, con=engine, if_exists='append', index=False)
        print(f'{i + len(chunk)} rows inserted')

    print(f'Data Insertion Completed, {len(df)} rows inserted')

    






    # while True: 

    #     try:
    #         t_start = time()
            
    #         df = next(df_iter)

    #         df.to_sql(name=table_name, con=engine, if_exists='append')

    #         t_end = time()

    #         print('inserted another chunk, took %.3f second' % (t_end - t_start))

    #     except StopIteration:
    #         print("Finished ingesting data into the postgres database")
    #         break
    
    

