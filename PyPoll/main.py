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

    csvreader = csv.reader(csvfile, delimiter = "",")
    header = next(csvreader)