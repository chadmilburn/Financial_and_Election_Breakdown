# Python Challenge

## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period
```
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
```


## PyPoll

![Vote Counting](Images/Vote_counting.png)

* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.
```
    csv_header = next(csvreader)
    #print(csv_header)
    candidate_id = []
    candidate = {}
    total_votes = 0
    for rows in csvreader:
        #as we move through the rows of csv we are totaling votes with this counter
        total_votes = total_votes + 1      
        name = rows[2]
        # with ths we creating a list of unique candidate names and dict for votes for each candidate
        if name not in candidate_id:
            #creates the list of candidates to use for dictionary key
            candidate_id.append(name)
            #to see how the list is created
            #print(candidate_id)
            #we are totaling the votes for each unique name and storing them with candidate_id as the key in a dictionary
            candidate[name] = 0
        candidate[name] = candidate[name] + 1
```        


