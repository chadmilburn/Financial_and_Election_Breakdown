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
    
    profit_change =[]
    for i in range(1, len(profit)):
        profit_change.append(int(profit[i])- int(profit[i-1]))
    greatest_increase = max(profit_change)
    greatest_increase_month = profit_change.index(max(profit_change))+1
    big_month = month[greatest_increase_month]
    greatest_decrease = min(profit_change)
    average_change = sum(profit_change)/len(profit_change)
    #check for correct list info
    #print(month)
    #print(profit)
    # find total of months with lenght of list
    total_months = len(month)
    #find sum of profits/loss column
        
    
    
    print(f' Total Months:  {total_months}')
    print(f' Total: ${total_profit}')
    print(profit_change)
    print(greatest_increase)
    print(greatest_decrease)
    print(average_change)
    print(greatest_increase_month)
    print(big_month)
