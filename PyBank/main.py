# import modules
import os 
import csv

# set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# open csv file
with open(csvpath) as csvfile:

    
    # #csv reader with delimieter and variable to hold contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #check that I am getting my file
    #print(csvreader)
    
    #skips the header row
    csv_header = next(csvreader)
    
    #print(f'CSV Header:{csv_header}')
    #check for me that I am pulling hte correct data 
    #for row in csvreader:
    #    print(row)

    # create list of total months and total profit/loss
    profit = []
    months = []

    for rows in csvreader:
        #creates a new list for first column of data a row at a time
        months.append(rows[0])
        #creates a new list for second column of data a row at a time
        profit.append(int(rows[1]))
        #check for me that this worked
        #print(months)
        #print(profit)
        total_months = len(months)
        #print(total_months)
        total_profitloss =sum(profit)
        #print(total_profitloss)


        #create rev change list and calculate list by cycling each x and subtracitng the next months for change
        rev_change =[]
        for x in range(1, len(profit)):
            rev_change.append(int(profit[x]) - int(profit[x-1]))
            #print(rev_change)
            great_increase = max(rev_change)
            great_decline = min(rev_change)
            ave_change = round((sum(rev_change)/len(rev_change)),2)
            #checks for the above lines
            #print(great_increase)
            #print(great_decline)
            #print(ave_change)
            #print(months[rev_change.index(max(rev_change))+1])
            #print(months[rev_change.index(min(rev_change))+1])
            #finds the row of the max value and searches the months list to return the month
            month_increase = (months[rev_change.index(max(rev_change))+1])
            #print(month_increase)
             #finds the row of the min value and searches the months list to return the month
            month_decrease = (months[rev_change.index(min(rev_change))+1])
            #print(month_decrease)

#creates and writes required info to txt file
file = open("Financial_Analysis.txt","w")
file.write("Financial Analysis\n")
file.write("----------------------------------------\n")
file.write(f'Total Months: {total_months}\n')
file.write(f'Total: ${total_profitloss}\n')
file.write(f'Average Change: $ {ave_change}\n')
file.write(f'Greatest Increase in Profits: {month_increase} (${great_increase})\n')
file.write(f'Greatest Decrease in Profits: {month_decrease} (${great_decline})\n')
file.close()

#print to terminal
print("Financial Analysis")
print("----------------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_profitloss}')
print(f'Average Change: $ {ave_change}')
print(f'Greatest Increase in Profits: {month_increase} (${great_increase})')
print(f'Greatest Decrease in Profits: {month_decrease} (${great_decline})')
#add commit line for push
