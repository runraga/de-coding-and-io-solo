# #Create a script which reads the cars JSON data and:
# A:
# Prints a list of dictionaries containing all of the table information.

import json

body=[]
with open('./data/cars.json', 'r', encoding='utf-16') as file:
    cars = json.load(file)
    cars_data = cars['Cars']
    # print(cars_data)

# B:
# Prints a collection of all the different car makes we have data on. There shouldn't be any repeats.
    car_makes = {ele['make'] for ele in cars_data}
    # print(car_makes)
    

# C:
# Prints a list of cars under 20 years old, youngest to oldest.
    car_age = [ele for ele in cars_data if ele['year'] > 2003]
    sorted_cars = sorted(car_age, key= lambda d: d['year'])
    # print(sorted_cars)


# D:
# Add your dream car to the cars data.
    new_car = {'vin': 'adhfakjdfhljh', 'make': 'Lambo', 'model': 'Aventador', 'year': 2022, 'colour': 'Black'}    
    cars_data.append(new_car)
    cars['Cars'] = cars_data
    with open('./data/cars.json', 'w', encoding='utf-16') as d:
        d.write('\n')
        json.dump(cars,d)


# E: 
# The Red Ford Tempo year was actually 1985. Please reflect this in the data.
    for car in cars_data:
        if car['make']=='Ford' and car['model']=='Tempo':
            car['year']=1985
            print(car)
    
