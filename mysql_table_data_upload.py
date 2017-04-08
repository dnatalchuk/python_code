"""
Scenario to upload data into MySQL specific table with file passed as argument.
File should be formated according to table structure and perform uploading:
"""

import sys
import csv
import pymysql

#declaring variables
db_host = 'manager.de'
db_name = 'google'
db_user = 'supp'
db_pass = 'aaa'
db_tables = 'google_date'

cursor = db_name.cursor()
#chapter for formatting data

csv_data = csv.reader(sys.argv[1])

def __init__(self):
    self.conn = pymysql.connect(db_host, db_user, db_pass)
    self.query


