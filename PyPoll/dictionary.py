import os
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
    candidate_id = []
    candidate = {}
    voter_id = []
    total_votes = 0
    for rows in csvreader:
     #   voter_id.append(rows[0])
     #   total_votes = len(voter_id)
        total_votes = total_votes + 1      
        name = rows[2]
        if name not in candidate_id:
            candidate_id.append(name)
            candidate[name] = 0
        candidate[name] = candidate[name] + 1

#print(candidate)
#print(total_votes) 

    for candidates in candidate:
        votecount = candidate.get(candidates)
        vote_percentage = round(float(votecount) / float(total_votes) *100,3)
        #print (vote_percentage)
        print f”{candidate}: {vote_percentage}% {candidate}\n”
