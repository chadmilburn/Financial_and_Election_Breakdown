# modules to work across os and with csv files
import os
import csv

# set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# open csv file
with open(csvpath) as csvfile:

    #check for me that I have opened the correct file
    # #csv reader with delimieter and variable to hold contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # #print(csvreader)

    csv_header = next(csvreader)
    #print(f'CSV Header: {csv_header}')
    # this is counting the months but now working correctly without the +1
    total = 0
    for row in csvreader:
        total = float(row[1])
        print(total) 
         #print(row)
        row_count = sum(1 for row in csvfile)+1
        print(row_count)       

    # for row in csvreader:
    #     #print(row)
    #     row_count = sum(1 for row in csvfile)+1
    #     print(row_count) 

     
    


    