# import modules
import os
import csv

# path to CSV file
csvpath = os.path.join('C:/Users/jariwalaj2/OneDrive/Python_Homework2_Py-Me-Up-Charlie/election_data.csv')

# open and read the CSV file
with open(csvpath) as csvfile:

    # specify delimiter and variable that holds the content from the CSV file
    csvreader = csv.reader(csvfile, delimiter=',')

    # specify csv header 
    csv_header = next(csvreader)
    row = next(csvreader)

# Declare Variables
total_votes_cast = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0


    # Read each row of data
    for row in csvreader:
    
        # Calculate total votes casted
        total_votes_cast +=1

        # Through If statements, Iterate through the values and calculate 
        # total votes each candidate won

        if (row[2] == "Khan"):
            Khan_votes +=1
        elif (row[2] == "Correy"):
            Correy_votes +=1
        elif (row[2] == "Li"):
            Li_votes +=1
        else:
            Otooley_votes +=1
        
    # Calculate the votes percentage each candidate received to win the election
    Khan_votes_percentage = Khan_votes / total_votes_cast
    Correy_votes_percentage = Correy_votes / total_votes_cast    
    Li_votes_percentage = Li_votes / total_votes_cast
    Otooley_votes_percentage = Otooley_votes / total_votes_cast

    # Through If statements, Iterate through the values and calculate 
    # who won the election based on popular votes
    Election_winner = max(Khan_votes, Correy_votes, Li_votes, Otooley_votes)

    if Election_winner == Khan_votes:
        winner_name == "Khan"
    elif Election_winner == Correy_votes:
        winner_name == "Correy"
    elif Election_winner == Li_votes:
        winner_name == "Li"
    else:
        winner_name == "Otooley"
      
# Print out the Election Results Analysis output
print(f"Election Results")
print(f".......................................")
print(f"Total Votes: {total_votes_cast}")
print(f".......................................")
print(f"Khan: {Khan_votes_percentage:.3%}({Khan_votes})")
print(f"Correy: {Correy_votes_percentage:.3%}({Correy_votes})")
print(f"Li: {Li_votes_percentage:.3%}({Li_votes})")
print(f"Khan: {Otooley_votes_percentage:.3%}({Otooley_votes})")
print(f".......................................")
print(f'Winner is: {winner_name}')
print(f".......................................")

# Write Election Results Analysis output
output_path = 'Election Results.txt'
with open(output_path, "w") as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f".......................................\n")
    txtfile.write(f"Total Votes: {total_votes_cast}\n")
    txtfile.write(f".......................................\n")
    txtfile.write(f"Khan: {Khan_votes_percentage: .3%} ({Khan_votes})\n")
    txtfile.write(f"Correy: {Correy_votes_percentage: .3%} ({Khan_votes})\n")
    txtfile.write(f"Li: {Li_votes_percentage: .3%} ({Khan_votes})\n")
    txtfile.write(f"Otooley: {Otooley_votes_percentage: .3%} ({Otooley_votes})\n")
    txtfile.write(f".......................................\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f".......................................\n")
