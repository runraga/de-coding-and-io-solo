import csv

pizzas = []
with open("./data/pizza.csv", 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    pizzas = [row for row in reader]

for pizza in pizzas:
    cost =  pizza['Cost'] 
    new_cost = float(cost[1:]) * 1.1
    pizza['Cost'] = f"£{round(new_cost, 2)}"

with open('./data/pizza.csv', 'w') as csv_file:
    field_names = ['Pizza','Cost','Description','Calories']
    writer = csv.DictWriter(csv_file, fieldnames=field_names)

    writer.writeheader()
    for pizza in pizzas:
        writer.writerow(pizza)