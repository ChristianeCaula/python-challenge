import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

profit = 0
loss = 0
amount = 0
total = 0
months = 0

prev_month = 0
inc_dec = 0
great_inc = 0
great_dec = 0
sum_inc_dec = 0
avarage = 0
index = 0

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    
    for row in csv_reader:
        amount = float(row[1])

        if amount > 0:
            profit = profit + amount
        else:
            loss = loss + amount

        inc_dec = amount - prev_month
        if index != 0:
            sum_inc_dec = sum_inc_dec + inc_dec

        if (inc_dec > 0) and (inc_dec > great_inc):
            great_inc = inc_dec
            month_row_inc = row[0]
        elif (inc_dec < 0) and (inc_dec < great_dec):
            great_dec = inc_dec
            month_row_dec = row[0]    
        
        prev_month = amount
        index +=1

    total = profit + loss

    months = len(list(csv.reader(open(csvpath))))
    # Check how many months are in the file not considering the header
    months = months - 1
    
    # Calculate the avarage dividing the total of changes by the number of changes
    avarage = sum_inc_dec / (months - 1)

    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: $ {total}")
    print(f"Average Change: $ {avarage}")
    print(f"Greatest Increase in Profits: {month_row_inc} ($ {great_inc})")
    print(f"Greatest Decrease in Profits: {month_row_dec} ($ {great_dec})")

output_path = os.path.join ("Financial_Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])

