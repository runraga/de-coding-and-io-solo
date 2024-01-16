import csv

with open("./data/pizza.csv", 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)
        if row['Pizza'] == 'Capri':
            desc = row['Description'].replace(', ', '\n')
            print(desc)
    