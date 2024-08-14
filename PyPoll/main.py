import csv

total = 0
candidates = {}
data = csv.reader(open('Resources/election_data.csv'))
myReport = open('Analysis/Election_Report.txt', 'w')

next(data)

for row in data:
   total +=1 
   cand = row[2]

   if cand not in candidates.keys():
      candidates[cand] = 0
    
   candidates[cand] += 1

output = f'''
Election Results
-------------------------
Total Votes: {total:,}
-------------------------
'''

win_votes = 0
for cand in candidates.keys():
   votes = candidates[cand]
   if win_votes < votes:
      win_votes = votes
      winner = cand

   output += f'{cand}: {votes/total*100:.3f}% ({votes:,})\n'

output += f'''
-------------------------
Winner: {winner}
-------------------------
'''

print(output)
myReport.write(output)