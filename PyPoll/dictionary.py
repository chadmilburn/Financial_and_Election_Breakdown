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
        #look to see how the loop is working
        #print(candidate)
    # for key in candidate:
    #     print(key)
    # print (candidate_id)
    file = open("Election_Results.txt", "w")
    file.write("Election Results")
    file.write("----------------")
    file.write(f'Total Votes:  {total_votes}')
    file.write("----------------")
    print("Election Results")
    print("----------------")
    print("Total Votes: " + str(total_votes))
    print("----------------")
    for key in candidate:
        #retrieveing the votes for each candidate
        votecount = candidate.get(key)
        #calculating percent of total vote
        vote_percentage = round(float(votecount) / float(total_votes) *100,3)
        totals = f'{key} : {vote_percentage}% ({candidate[key]})\n'
        #check for percentages
        #totals = f' {vote_percentage}%\n'
        print(totals)
        file.write(f'{totals}\n')
    
    winner = max(candidate, key=candidate.get)
    print("----------------")
    print("Winner:" + str(winner))
    print("----------------")

    file.write("----------------\n")
    file.write(f'Winner: {winner}\n')
    file.write("----------------")
    file.close()

