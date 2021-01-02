# import modules
import os
import csv

# path to CSV file
csvpath = os.path.join('C:/Users/jariwalaj2/OneDrive/Python_Homework2_Py-Me-Up-Charlie/budget_data.csv')

# open and read the CSV file
with open(csvpath) as csvfile:

    # specify delimiter and variable that holds the content from the CSV file
    csvreader = csv.reader(csvfile, delimiter=',')

    # specify csv header 
    csv_header = next(csvreader)
    row = next(csvreader)

    # Total number of Months
    total_months = 0

    # Total net amount of "Profit/Losses"
    total_net_amount = 0

    # Calculate the changes in "Profil/Losses" over the entire period (empty lsit)
    monthly_changes = []

    # Find the average of "Profit/Losses changes"
    monthly_average_count = []

    # Find the greatest increase in profits over the entire period
    greatest_increase = 0
    greatest_monthly_increase = []
    
    # Find the greatest decrease in profits over the entire period
    greatest_decrease = 0
    greatest_monthly_decrease = []


    # Iterate through the values and calculate total_months, total_net_amount,
    # monthly_changes, monthly_average_count, greatest_increase, greatest_monthy_increase, greatest_decrease, greatest_monthly_decrease
    previous_profit = int(row[1])
    total_months +=1
    total_net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_monthly_increase = row[0]

    # Read each rows in csv file
    for row in csvreader:

        total_months = total_months + 1
        total_net_amount = total_net_amount + int(row[1])

        # Calculate the change in profit from this month (current) to last month (previous)
        profit_changes = int(row[1]) - previous_profit
        monthly_changes.append(profit_changes)
        previous_profit = int(row[1])
        monthly_average_count.append(row[0])

        # Calculate the greatest increase and the greatest decrease
        if int(row[1]) > greatest_increase:
                greatest_increase = int(row[1])
                greatest_monthly_increase = row[0]

        if int(row[1]) < greatest_decrease:
                greatst_decrease = int(row[1])
                greatest_monthly_decrease = row[0]

    # Calculate the average and the date
    average = sum(monthly_changes)/len(monthly_changes)

    # Calculate the max and min from the csv file
    increase = max(monthly_changes)
    decrease = min(monthly_changes)

# Print out the Financial Analysis output
print(f"Financial Analysis")
print(f".......................................")
print(f"Total Months: {total_months}")
print(f"Total Net Profit/Losses: ${total_net_amount}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits:, {greatest_monthly_increase}, (${increase})")
print(f"Greatest Decrease in Profits:, {greatest_monthly_decrease}, (${decrease})")


# Write Financial Analysis output
output_path = 'Fiancial Analysis.txt'
with open(output_path, "w") as txtfile:
    txtfile.writerow(f"Financial Analysis\n")
    txtfile.writerow(f".......................................\n")
    txtfile.writerow(f"Total Months: {total_months}\n")
    txtfile.writerow(f"Total Net Profit/Losses: ${total_net_amount}\n")
    txtfile.writerow(f"Average Change: ${average}\n")
    txtfile.writerow(f"Greatest Increase in Profits:, {greatest_monthly_increase}, (${increase})\n")
    txtfile.writerow(f"Greatest Decrease in Profits:, {greatest_monthly_decrease}, (${decrease})\n")
