import csv

csv_path = "Pypoll/Resources/election_data.csv"

votes = 0

candidates = {}

with open(csv_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
      # print(row)

        votes += 1

        candidate = row[2]
        if candidate in candidates.keys():
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

print(votes)
print(candidates)

winner = max(candidates, key=candidates.get)
print(winner)

output = f"""Election Results
------------------------------------------
Total Votes: {votes}
------------------------------------------\n"""


for key in candidates.keys():
    perc = round(100*candidates[key]/votes, 3)
    newline = f"{key}: {perc}% ({candidates[key]})\n"
    output += newline

lastline = f"""
------------------------------------------
Winner: {winner}
------------------------------------------"""

output += lastline
print(output)

with open("PyPoll_out_ryan.text", "w") as txt_file:
    txt_file.write(output)