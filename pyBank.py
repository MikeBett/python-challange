import os
import csv

csvpath = os.path.join("Resources", 'budget_data')
with open(csvpath) as csvfile
csvreader=csv.reader(csvfile, delimiter = ",")

moth_count= csvfile.len("months")
print(moth_count)