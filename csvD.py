import csv

with open('./data/pizza.csv', 'a', newline='\n') as csv_file:
    field_names = ['Pizza','Cost','Description','Calories']

    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writerow({'Pizza':'Florentine', 'Cost': '£7.50', 'Description':'egg, spinach', 'Calories':'550kcal'})