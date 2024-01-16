import csv

with open("./data/pizza.csv", 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    cheap_pizzas = [row for row in reader if float(row['Cost'][1:]) < 9.00 ]
    sorted_list = sorted(cheap_pizzas, key=lambda d: float(d['Cost'][1:]))
    print(sorted_list)