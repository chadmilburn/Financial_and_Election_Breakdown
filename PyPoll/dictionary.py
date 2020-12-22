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
        # with ths we creating a list of unique candidate names
        if name not in candidate_id:
            candidate_id.append(name)
            #we are totaling the votes for each unique name and storing them with candidate_id as the key in a dictionary
            candidate[name] = 0
        candidate[name] = candidate[name] + 1

    # for key in candidate:
    #     print(key)
    # print (candidate_id)

    print("Election Results")
    print("----------------")
    print("Total Votes: " + str(total_votes))
    print("----------------")
    for candidates in candidate:
        #retrieveing the votes for each candidate
        votecount = candidate.get(candidates)
        #calculating percent of total vote
        vote_percentage = round(float(votecount) / float(total_votes) *100,3)
        #print (vote_percentage)
        #print(candidate[candidates])
        #for key in candidate_id.keys():
            
        totals = f'{candidates} : {vote_percentage}% ({candidate[candidates]})\n'
        #name = f'{candidates}'
        #totals = f' {vote_percentage}%\n'
        #print(name)
        print(totals)

    
    winner = max(candidate, key=candidate.get)
    print("----------------")
    print("Winner:" + str(winner))
    print("----------------")

    print("Election Results")
    print("----------------")
    print("Total Votes: " + str(total_votes))
    print("----------------")
   
   
   
    file = open("Election_Results.txt", "w")
    file.write("Election Results\n")
    file.write("----------------\n")
    file.write(f'Total Votes:  {total_votes}\n')
    file.write("----------------\n")
    for candidates in candidate:
        #retrieveing the votes for each candidate
        votecount = candidate.get(candidates)
        #calculating percent of total vote
        vote_percentage = round(float(votecount) / float(total_votes) *100,3)
        #print (vote_percentage)
        #print(candidate[candidates])
        #for key in candidate_id.keys():
            
        totals = f'{candidates} : {vote_percentage}% ({candidate[candidates]})\n'
        #name = f'{candidates}'
        #totals = f' {vote_percentage}%\n'
        #print(name)
        file.write(f'{totals}\n')
        
    
    winner = max(candidate, key=candidate.get)
    file.write("----------------\n")
    file.write(f'Winner: {winner}\n')
    file.write("----------------")
    file.close()
