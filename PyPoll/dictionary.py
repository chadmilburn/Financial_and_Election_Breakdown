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
    total_votes = 0
    for rows in csvreader:

        total_votes = total_votes + 1      
        name = rows[2]
        if name not in candidate_id:
            candidate_id.append(name)
            candidate[name] = 0
        candidate[name] = candidate[name] + 1

    print("Election Results")
    print("----------------")
    print("Total Votes: " + str(total_votes))
    print("----------------")
    candidate = tuple.get(candidate)
    for candidates in candidate:
        votecount = candidate.get(candidates)
        vote_percentage = round(float(votecount) / float(total_votes) *100,3)
        #print (vote_percentage)
        #print(candidate[candidates])
        #names = tuple(candidate_id)
        totals = f'{candidate[0]} : {vote_percentage}% ({candidate[candidates]})\n'
        #name = f'{candidate[candidate]}'
        #totals = f' {vote_percentage}%\n'

        print(totals)

    
    winner = max(candidate, key=candidate.get)
    print("----------------")
    print("Winner:" + str(winner))
    print("----------------")
print(candidate)
