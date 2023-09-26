# importing csv file and making it accessible across all os
import os 
import csv

# establishing path to collect data
election_csv = os.path.join("Resources", "election_data.csv")

# making variables to store total and individual vote counts
# these are essentially counters
total_votes = 0
candadite1 = 0
candadite2 = 0
candadite3 = 0

# reading csv file
with open(election_csv, "r") as csvfile:
    
    # splitting the data on the commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # saving header
    header = next(csvfile)

    # looping through each row of the csv file
    for row in csvreader:

        # establishing a counter (essentially counting each row) to get total votes
        total_votes += 1

        # using a conditional statement to add to the established variables when the candidates name appears in the file
        if row[2] == "Charles Casper Stockham":
            candadite1 += 1
        elif row[2] == "Diana DeGette":
            candadite2 += 1
        elif row[2] == "Raymon Anthony Doane":
            candadite3 += 1

# making variables to calculate the percentage of votes each candidate recieved 
candadite1_percent = round((((candadite1) / (total_votes)) * 100), 3)
candadite2_percent = round((((candadite2) / (total_votes)) * 100), 3)
candadite3_percent = round((((candadite3) / (total_votes)) * 100), 3)

# finding the winner by making a dictionary of the candidates and their vote counts
candadite_dictionary = {
    "Charles Casper Stockham": candadite1,
    "Diana DeGette": candadite2,
    "Raymon Anthony Doane": candadite3
}

# using max to find the maximum value within the dictionary and get to find the maximum key within that dictionary  
winner = max(candadite_dictionary, key = candadite_dictionary.get)

# printing statements
print("Election Results")
print("------------------------------")
print("Total Votes: " + str(total_votes))
print("------------------------------")
print("Charles Casper Stockham: " + str(candadite1_percent) + "% (" + str(candadite1) + ")")
print("Diana DeGette: " + str(candadite2_percent) + "% (" + str(candadite2) + ")")
print("Raymon Anthony Doane: " + str(candadite3_percent) + "% (" + str(candadite3) + ")")
print("------------------------------")
print("Winner: " + str(winner))

# adding path to write into text file
output_file = os.path.join("Analysis", "pybank_analysis.txt")

# writing results into the text file
with open(output_file, "w") as datafile:
    datafile.write("Election Results")
    datafile.write("\n")
    datafile.write("------------------------------")
    datafile.write("\n")
    datafile.write("Total Votes: " + str(total_votes))
    datafile.write("\n")
    datafile.write("------------------------------")
    datafile.write("\n")
    datafile.write("Charles Casper Stockham: " + str(candadite1_percent) + "% (" + str(candadite1) + ")")
    datafile.write("\n")
    datafile.write("Diana DeGette: " + str(candadite2_percent) + "% (" + str(candadite2) + ")")
    datafile.write("\n")
    datafile.write("Raymon Anthony Doane: " + str(candadite3_percent) + "% (" + str(candadite3) + ")")
    datafile.write("\n")
    datafile.write("------------------------------")
    datafile.write("\n")
    datafile.write("Winner: " + str(winner))