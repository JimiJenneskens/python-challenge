import os
import csv

# set input and output paths
budget_datacsv = os.path.join("Resources", "budget_data.csv")
output_txt = os.path.join("analysis", "output.txt")

profitlosses = []

# open and read input csv file
with open(budget_datacsv) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    
    months = 0
    total = 0

    # loop through csvreader for total month and total profit/loss
    for row in csvreader:
        profitlosses.append(row)
        # total number months
        months += 1
        # total profit/losses
        total += int(row[1])
       
    dif_prof = 0
    tot_change = 0
    avg_change = 0
    max_decr = 0
    max_incr = 0

    # loop to determine total amount change, average change and max/min values + month
    for i in range(months,1,-1): 
        dif_prof = int(profitlosses[i-1][1]) - int(profitlosses[i-2][1])
        # find greatest increase and decrease values and month
        if dif_prof < max_decr:
            min_month_yr = profitlosses[i-1][0]
            max_decr = dif_prof
        elif dif_prof > max_incr:
            max_incr = dif_prof
            max_month_yr = profitlosses[i-1][0]
        # total change
        tot_change = tot_change + dif_prof
    # define average change
    avg_change = tot_change / (months-1)

# print financial analysis
print("Financial Analysis")
print("------------------------------------")
print("Total Months: " + str(months))
print("Total: $" + str(total))
print("Average  Change: $" + str(round(avg_change,2)))
print("Greatest Increase in Profits: " + max_month_yr + " ($" + str(max_incr) + ")")
print("Greatest Decrease in Profits: " + min_month_yr + " ($" + str(max_decr) + ")")


# write to text file       
text_file=open(output_txt,"w")
text_file.write("Financial Analysis")
text_file.write("\n------------------------------------")
text_file.write("\nTotal Months: " + str(months))
text_file.write("\nTotal: $" + str(total))
text_file.write("\nAverage  Change: $" + str(round(avg_change,2)))
text_file.write("\nGreatest Increase in Profits: " + max_month_yr + " ($" + str(max_incr) + ")")
text_file.write("\nGreatest Decrease in Profits: " + min_month_yr + " ($" + str(max_decr) + ")")
text_file.close()