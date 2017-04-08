"""
Scenario to upload data into MySQL specific table with file passed as argument.
File should be formated according to table structure and perform uploading:
"""

import sys
import csv
import pymysql

#declaring variables
db_host = 'manager.de'
db_user = 'supp'
db_pass = 'aaa'
db_tables = 'google table'

#chapter for formatting data

csv_data = csv.reader(sys.argv[1])
