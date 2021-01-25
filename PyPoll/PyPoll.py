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
    print(csv_header)

# Declare Variables
    total_votes_cast = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    Otooley_votes = 0
    klist = []


    # Read each row of data
    for row in csvreader:     
    # Calculate total votes casted
        total_votes_cast +=1
    #     if row[2] not in electionlist:
    #         electionlist.append(row[2])
    # print(electionlist)        
    # print(total_votes_cast)      
        if (row[2] == "Khan"):
            klist.append(row[2])
    #print(klist)        
            Khan_votes +=1
            
        elif (row[2] == "Correy"):
            klist.append(row[2])
            Correy_votes +=1
        elif (row[2] == "Li"):
            klist.append(row[2])
            Li_votes +=1
        else:
            klist.append(row[2])
            Otooley_votes +=1
    
        
    #Calculate the votes percentage each candidate received to win the election
    Khan_votes_percentage = Khan_votes / total_votes_cast
    Correy_votes_percentage = Correy_votes / total_votes_cast    
    Li_votes_percentage = Li_votes / total_votes_cast
    Otooley_votes_percentage = Otooley_votes / total_votes_cast

    #Through If statements, Iterate through the values and calculate 
    #who won the election based on popular votes
    election_winner = []
    election_winner.append(Khan_votes)
    election_winner.append(Correy_votes)
    election_winner.append(Li_votes)
    election_winner.append(Otooley_votes)
    
    # print(election_winner)
    Election_winner = max(election_winner)
    winner_name = ("")
    # print(Election_winner)

    if Election_winner == Khan_votes:
        winner_name = "Khan"
        
    elif Election_winner == Correy_votes:
        winner_name = "Correy"
    elif Election_winner == Li_votes:
        winner_name = "Li"
    else:
        winner_name = "Otooley"
     

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