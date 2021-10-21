import mysql.connector
from mysql.connector import Error
import os
import csv
import datetime
from werkzeug.utils import secure_filename
import glob

connection = mysql.connector.connect(host='localhost',database='tghrms',user='root',password='')
cursor = connection.cursor()
    
#csv reader
fns=glob.glob("E:/Transact-Global-HRMS/New_Code/Logsdata/*")
print(fns)
for i in fns:
    fn=i
#print(fn)

fields = [] 
rows = []
with open(fn, 'r') as csvfile:
    # creating a csv reader object 
    csvreader = csv.reader(csvfile)   
  
    # extracting each data row one revenue one 
    for row in csvreader:
        rows.append(row)
        print(row)

try:     
    #print(rows[1][1])       
    for row in rows[1:]: 
        # parsing each column of a row
        if row[0][0]!="":                
            query="";
            query="insert into  logstable(id,SystemName,Username,logintime,logouttime,actions,entrydate,entry,processed,isAutoentry,isSynched,version)values (";
            for col in row: 
                query =query+"'"+col+"',"
            query =query[:-1]
            query=query+");"
        print("query :"+str(query), flush=True)
        cursor.execute(query)
        connection.commit()
except:
    print("An exception occurred")
csvfile.close()
        
      
        

connection.close()
cursor.close()

