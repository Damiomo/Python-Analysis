import os
import csv

total_months = 0
Profit_loss = 0
Previous_profit_loss = 0
changes = [] 
months = []

PyBank_csv = os.path.join("C:\\Users\\New User\\module-3-python\\Starter_Code\PyBank\\Resources\\budget_data.csv")
with open(PyBank_csv) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')

    next(csvreader)
   
    for row in csvreader:
        total_months = total_months + 1
        Profit_loss = Profit_loss + int(row[1])
        months.append(row[0])
        if Previous_profit_loss != 0:
            change = int(row[1]) - Previous_profit_loss
            changes.append(change)
        Previous_profit_loss = int(row[1])

change_in_profit = sum(changes)/len(changes)

max_change_index = changes.index(max(changes))
min_changes_index = changes.index(min(changes))

greatest_increase_month = months[max_change_index+1]
greatest_decrease_month = months[min_changes_index+1]

max_change = max(changes)
min_change = min(changes)       
print(f'Total Months: {total_months}')
print(f'Total: {Profit_loss}')
print(f'Average Change: {change_in_profit}')
print(f"Greatest Increase in Profits: {greatest_increase_month} ({max_change})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} ({min_change})")

output_directory = "C:\\Users\\New User\\module-3-python\\Starter_Code\\PyBank"
output_file_path = os.path.join(output_directory, "PyBank")

with open(output_file_path, 'w') as outfile:
    outfile.write("Total Months: "+str(total_months)+"\n")
    outfile.write("Total: "+str(Profit_loss)+"\n")
    outfile.write("Average Change: "+str(change_in_profit)+"\n")
    outfile.write("Greatest increase in Profits: "+str(greatest_increase_month)+" "+str(max_change)+"\n")
    outfile.write("Greatest decrease in Profits: "+str(greatest_decrease_month)+" "+str(min_change)+"\n")