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

    print(str(len(polls)))

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
        print(str(name) + ": " + str(dic_votes[name]) + "% " + "(" + str(dic_names[name]) + ")")