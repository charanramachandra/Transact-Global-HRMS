'''
import glob
import os

list_of_files = glob.glob('E:/Transact-Global-HRMS/New_Code/Logsdata/') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)
'''


import glob
import os.path
import pandas as pd
files = glob.glob('E:/Transact-Global-HRMS/New_Code/Logsdata/*')
max_file = (files, key=os.path.getctime)

print(max_file)
