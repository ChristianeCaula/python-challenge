import os
import csv

###### FINAL VERSION

csvpath = os.path.join('Resources', 'election_data.csv')

candidate = []
votes = []
total_votes = 0
count = 0
khan = 0
total_candidates_with_votes = 0
i = 0
votes_candidate = 0
percent = 0
winner_percent = 0

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    
    total_votes  = len(list(csv.reader(open(csvpath))))

    output_path = os.path.join ("Election_Results.csv")

#   Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as csvfile:

        # Initialize csv.writer
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(["Election Results"])
        csvwriter.writerow(["----------------------------"])
        csvwriter.writerow([f"Total Votes: {total_votes}"])
        csvwriter.writerow(["----------------------------"])

        for row in csv_reader:
            name = row[2]
            votes.append(name)
            if name in candidate:
                continue
            else:
                candidate.append(name)

        print(f"Election Results")
        print(f"----------------------------")
        print(f"Total Votes: {total_votes}")
        print(f"----------------------------")

        total_candidates_with_votes = len(candidate)

        while i < total_candidates_with_votes:
            name_aux = candidate[i]
            votes_candidate = votes.count(name_aux)
            percent = votes_candidate / total_votes * 100
        
            if percent > winner_percent:
                winner_percent = percent
                winner_name = name_aux

            percent = round(percent,4)
            print(f"{name_aux} : {percent} % ( {votes_candidate} )")

            i = i + 1

            csvwriter.writerow([f"{name_aux} : {percent} % ( {votes_candidate} )"])
        

    #   Open the file using "write" mode. Specify the variable to hold the contents
        with open(output_path, 'r+', newline='') as csvfile:

            csvwriter.writerow([f"----------------------------"])
            csvwriter.writerow([f"Winner: {winner_name}"])

    print(f"----------------------------")
    print(f"Winner: {winner_name}")

    
