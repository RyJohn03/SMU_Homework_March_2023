import csv

csv_path = "Resources/election_data.csv"

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

for key in candidates:
    print(key, 100*candidates[key]/votes)