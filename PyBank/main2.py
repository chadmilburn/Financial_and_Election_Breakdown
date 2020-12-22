# modules needed to create file paths across different os
import os
# module to read a csv file
import csv

# path to the file for analyis
csvpath = os.path.join('Resources','budget_data.csv')

# open the file 
with open(csvpath) as csvfile:
    # CSV reader with delimiter and variable to hold contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #check file path is correct 
    #print(csvreader)

    #checks for header 
    csv_header = next(csvreader)
    #print(csv_header)
    #creates lists for months and profits from data by looping each row
    month = []
    profit = []
    total_profit = 0 
    for rows in csvreader:
        month.append(rows[0])
        profit.append(rows[1])
        total_profit += int(rows[1])

    #check for correct list info
    #print(month)
    #print(profit)
    # find total of months with lenght of list
    total_months = len(month)
    #find sum of profits/loss column
        
    
    
    print(total_months)
    print(total_profit)
