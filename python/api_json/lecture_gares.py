import csv
import json
"""
with open('api_sncf.json') as file:
    data = json.load(file)
print(data[1])
"""
with open('api_sncf_2.csv', 'w') as file:
    csv_file = csv.writer(file)
    for line in csv:
        csv_file.writerow(["salut"])

"""
with open('api_sncf.csv', 'r') as api_csv:
    csv_r = csv.DictReader(api_csv, delimiter='-')

    for line in csv_r:
        print(line['email'])"""
"""
    for line in csv_r:
        print(line[0].split("-"))"""