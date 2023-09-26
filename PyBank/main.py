# importing csv file and making it accessible across all os
import os 
import csv

# establishing path to collect data
budget_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# creating lists to store data
months = []
profits = []
monthly_change = []

# reading the csv file
with open(budget_csv, "r") as csvfile:

    # splitting the data on the commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # saving header
    header = next(csvfile)

    # looping through each row in the csv file and adding months and profits to the empty lists
    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))

    # calculating the change in profit between every entry
    # need to subtract 1 or else the index will be out of the range
    for i in range(len(profits) - 1):
        
        # adds the difference of each month to the monthly change list
        monthly_change.append(profits[i + 1] - profits[i])

# obtaining average monthly change
average_monthly_change = ((sum(monthly_change))/((len(monthly_change))))

# obtaining min and max change of profit
biggest_increase = max(monthly_change)
biggest_decrease = min(monthly_change)

# adding the max and min to the proper date by finding the index number of where it occured
# need to add one because the change is associated with the month that follows
biggest_increase_month = monthly_change.index(max(monthly_change)) + 1
biggest_decrease_month = monthly_change.index(min(monthly_change)) + 1  

# printing statements
print("Financial Analysis")
print("------------------------------")
print("Total Months: " + str(len(months)))
print("Total: $" + str(sum(profits)))
print("Average Change: " + str(round((average_monthly_change), 2)))
print("Greatest Increase in Profits: " + str(months[biggest_increase_month]) + " ($" + str(biggest_increase) + ")")
print("Greatest Decrease in Profits: " + str(months[biggest_decrease_month]) + " ($" + str(biggest_decrease) + ")")

# adding path to write into text file
output_file = os.path.join("..", "PyBank", "Analysis", "pybank_analysis.txt")

# writing results into the text file
with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis")
    datafile.write("\n")
    datafile.write("------------------------------")
    datafile.write("\n")
    datafile.write("Total Months: " + str(len(months)))
    datafile.write("\n")
    datafile.write("Total: $" + str(sum(profits)))
    datafile.write("\n")
    datafile.write("Average Change: " + str(round((average_monthly_change), 2)))
    datafile.write("\n")
    datafile.write("Greatest Increase in Profits: " + str(months[biggest_increase_month]) + " ($" + str(biggest_increase) + ")")
    datafile.write("\n")
    datafile.write("Greatest Decrease in Profits: " + str(months[biggest_decrease_month]) + " ($" + str(biggest_decrease) + ")")