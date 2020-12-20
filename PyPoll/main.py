import  os
import csv

#set path to data
csvpath = os.path.join("Resources", "election_data.csv")

#open csv file
with open(csvpath) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    #check for file object
    #print(csvreader)

    csv_header = next(csvreader)
    #print(csv_header)

    #Create lists to calculate results
    voter_id =[]
    khan = []
    correy = []
    li = []
    otooley = []
    # fill created lists with each variable to be counted
    for rows in csvreader:
        voter_id.append(rows[0])
        total_votes = len(voter_id)
        if "Khan" == rows[2]:
            khan.append(rows[2])
        elif "Correy" == rows[2]:
            correy.append(rows[2])
        elif "Li" == rows[2]:
            li.append(rows[2])
        else:
            otooley.append(rows[2])
    # len to count total and candidate votes
    total_votes= len(voter_id)
    votes_khan = len(khan)
    votes_correy = len(correy)
    votes_li = len(li)
    votes_otooley = len(otooley)
    
    #use counts to calcuate percentages
    percent_khan = round((votes_khan / total_votes)*100,4)
    percent_correy = round((votes_correy/total_votes)*100,4)
    percent_li = round((votes_li/total_votes)*100,4)
    percent_otooley = round((votes_otooley/total_votes)*100,4)   

    #winner
    # winner = [votes_khan, votes_correy, votes_li, votes_otooley]
    # Electionwinner = max(winner)
    # print(Electionwinner)

print("Election Results")
print("--------------------")
print(f'Total Votes: {total_votes}')
print("--------------------")
print(f'Khan: {percent_khan}% ({votes_khan})')
print(f'Correy: {percent_correy}% ({votes_correy})')
print(f'Li: {percent_li}% ({votes_li})')
print(f"""O'Tooley: {percent_otooley}% ({votes_otooley})""")




# print(total_votes)
# print(votes_khan)
# print(percent_khan)
# print(votes_correy)
# print(percent_correy)
# print(votes_li)
# print(percent_li)
# print(votes_otooley)
# print(percent_otooley)








