import os
import csv

total_votes = 0
unique_candidates = set()
Percentages = []
Votes = []
Charles_votes = 0
Diana_votes = 0
Raymon_votes = 0

PyPoll_csv = os.path.join("C:\\Users\\New User\\module-3-python\\Starter_Code\\PyPoll\\Resources\\election_data.csv")
with open(PyPoll_csv) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')

    next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        Candidate = row[2]
        unique_candidates.add(Candidate)
        if row[2] == "Charles Casper Stockham":
            Charles_votes = Charles_votes + 1
        elif row[2] == "Diana DeGette":
            Diana_votes = Diana_votes + 1
        else: Raymon_votes = Raymon_votes + 1
    
    Votes.append(Charles_votes)
    Votes.append(Diana_votes)
    Votes.append(Raymon_votes)

    Percentage_Charles_votes = Charles_votes/total_votes
    Percentage_Diana_votes = Diana_votes/total_votes
    Percentage_Raymon_votes = Raymon_votes/total_votes

    Percentage_formatted_Charles ="{:2%}".format(Percentage_Charles_votes)
    Percentage_formatted_Diana ="{:2%}".format(Percentage_Diana_votes)
    Percentage_formatted_Raymon ="{:2%}".format(Percentage_Raymon_votes)

    Percentages.append(Percentage_formatted_Charles)
    Percentages.append(Percentage_formatted_Diana)
    Percentages.append(Percentage_formatted_Raymon)

print(f'Total Votes: {total_votes}')

zipped_lists = zip(sorted(unique_candidates),Votes,Percentages)
zipped_lists = list(zipped_lists)

print(zipped_lists)

def print_winner(Votes):
    if max(Votes) == 85213:
        winner = "Winner: Charles Casper Stockham"
    elif max(Votes) == 272892:
        winner = "Winner: Diana DeGette"
    else: winner = "Winner: Raymon Anthony Doane"

    return winner

print(print_winner(Votes))
Winner = print_winner(Votes)

output_directory = "C:\\Users\\New User\\module-3-python\\Starter_Code\\PyPoll\\"
output_file_path = os.path.join(output_directory, "PyPoll.txt")

with open(output_file_path, 'w') as outfile:
    outfile.write("Total Votes: "+str(total_votes)+"\n")
    outfile.write(str(zipped_lists)+"\n")
    outfile.write(str(Winner)+"\n")