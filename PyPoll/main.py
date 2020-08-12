import os
import csv

# set input and output paths
election_datacsv = os.path.join("Resources", "election_data.csv")
output_txt = os.path.join("analysis", "output.txt")

# define list and dictionaries for candidate names and total number vots per name
polls=[]
dic_names={}
dic_votes={}

# open and read input csv file
with open(election_datacsv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    # define number of votes
    for row in csvreader:
        polls.append(row)

    # print summary
    print("Election Results")
    print("------------------------------------") 
    print("Total Votes: "+str(len(polls)))
    print("------------------------------------")

    # write to text file
    text_file = open(output_txt, "w")
    text_file.write("Election Results")
    text_file.write("\n------------------------------------")
    text_file.write("\nTotal Votes: " + str(len(polls)))
    text_file.write("\n------------------------------------")

    # convert polls list in dictionary for counting names of candidate
    for row in polls:
        candidate = row[2]
        if candidate not in dic_names:
           # put name in dictionary 
            dic_names[candidate]=0
        # cout name in dictionary
        dic_names[candidate]+=1

    # define names, percentage and number of votes for each candidate
    total_polls = len(polls)
    for name in dic_names:
        dic_votes[name] = round((dic_names[name] / total_polls) * 100)

        # print percentage and votes per candidate
        print(str(name) + ": " + str(dic_votes[name]) + "% " + "(" + str(dic_names[name]) + ")")

        # write percentage and votes per candidate to text file
        text_file.write("\n" + str(name) + ": " + str(dic_votes[name]) + "% " + "(" + str(dic_names[name]) + ")")

    # set variable to compare and define winner
    highest = 0
    for name in dic_votes:
        if highest < dic_votes[name]:
            highest = dic_votes[name]
            winner = name

    # print winner
    print("------------------------------------")
    print("Winner: " + winner)
    print("------------------------------------")

    # write winner to text file
    text_file.write("\n------------------------------------")
    text_file.write("\nWinner: " + winner)
    text_file.write("\n------------------------------------")
    text_file.close()