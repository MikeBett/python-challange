#all imports neccessary
import os
import csv
from tokenize import Double
#variables to keep track of 
months=[]
month_count = 0
profit=[]
netTotalProfit = Double
avarageprofitChange= float
greatestProfitIncrease= Double
change_in_profit =[]
greatestDecreaselosses= Double
#read in csv file with correct path
csv_path=os.path.join('..', 'Resources', 'budget_data.csv')
with open(csv_path, "r")as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvheader= next(csvreader)
#code for solution
#for loop
    for row in csvreader:
        month=row[0]
        months.append(month)
        values=int(row[1])
        profit.append(values)
        month_count= len(months) 
        Total=sum(profit)  
    for i in range(len(profit)-1):
        change_in_profit.append(profit[i+1]-profit[i])
        avarageprofitChange= Total/len(profit)-1

#maximun and minimum profit change
        greatestProfitIncrease=max(change_in_profit)
        greatestDecreaselosses=min(change_in_profit)

print(month_count) 
print(avarageprofitChange)

#print results
print("PyBank Analysis")
print("--------------------------")
print(f"Total Profts: {Total}")
print("---------------------------")
print(f"Greatest increase in Profits: {greatestProfitIncrease}")
print("---------------------------")
print(f"Greatest Decrease in Losses: {greatestDecreaselosses}")

write_file = f"pybank_results_summary.txt"

#open write file
filewriter = open(write_file, mode = 'w')

#print analysis to file
filewriter.write("PyBank Analysis\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Profits: {Total}\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Greatest increase in Profits: {greatestProfitIncrease}\n")
filewriter.write(f"Greatest decrease in losses: {greatestDecreaselosses}\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Average Profit Change: {avarageprofitChange}\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Total Number of Months: {month_count}\n")

#close file
filewriter.close()
