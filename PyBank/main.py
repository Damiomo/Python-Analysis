import csv

incVal = 0
decVal = 0
total = 0
months = 0
pre_rev = 0
total_ch = 0
data = csv.reader(open('Resources/budget_data.csv'))
myReport = open('Analysis/budget_report.txt', 'w')

header = next(data)

for row in data:
    months += 1
    rev = int(row[1])
    total = total + rev

    # Average change
    ch = rev - pre_rev

    if pre_rev == 0:
        ch = 0

    total_ch += ch

    # Greastest increase
    if ch > incVal:
        incVal = ch
        incMon = row[0]

    # Greatest decrease
    if ch< decVal:
        decVal = ch
        decMon = row[0]

    # reset variables for next row
    pre_rev = rev

output = f'''
    Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${total_ch/(months-1):,.2f}
Greatest Increase in Profits: {incMon} (${incVal:,})
Greatest Decrease in Profits: {decMon} (${decVal:,})
'''

print(output)
myReport.write(output)