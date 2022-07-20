import pandas as pd
import os
# import csv
# import sys
# print(os.getcwd())
# print(sys.argv)
# try :
#     day= sys.argv[1]

# except: 
#     print('no arguments')

#print(f'successfully executed and imported the file {day}')
df=pd.read_parquet('wk1/docker_setup/yellow_tripdata_2022-01.parquet')
os.chdir('wk1/docker_setup')
df.to_csv('tripdata.csv')