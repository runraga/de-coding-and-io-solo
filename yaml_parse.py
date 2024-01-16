# YAML
# Create a script which reads the people YAML data and:
import yaml

people = {}
with open('./data/people.yml', 'r', encoding='utf-8') as f:
    people = yaml.safe_load(f)
    # print(people)

# A:
# Prints Craig's job.
for person in people['people']:
    if person['name'] == 'Craig':
        print(person['job'])

# B:
# Prints Ron's interests.
for person in people['people']:
    if person['name'] == 'Ron':
        print(person['interests'])       

# C:
# Prints the average age of all the people.
total_age = 0
num_people = len(people['people'])
for person in people['people']:
    if isinstance(person['age'], int):
        total_age += int(person['age'])
    else:
        num_people -= 1
average_age = total_age / num_people
print(round(average_age, 0))


# D:
# Prints a list of dictionaries representing all of the data.
# print(people['people'])

# E:
# Prints a list of people who have Tombolas listed in their interests.
tombola_people = [person for person in people['people'] if person['interests'].__contains__('Tombolas')]
print(tombola_people)

# F:
# Write to the YAML data to include information about yourself.
new_info = {'name': 'James', 'age':21, 'job':'Northcoder', 'interests':['sleeping', 'walking', 'reading'], 'wants':['find a job as a programmer'],'location':'north', 'favourite song':'definitley maybe', 'favourite movie':'Oppenheimer'}
people['people'].append(new_info)

with open('./data/people.yml', 'w') as f:
    yaml.dump(people, f)



# G:
# Add a favourite colour key to each person.
for person in people['people']:
    person['favourite colour'] = 'red'
print(people['people']) 

# H:
# Find everyone who lives in London and change it to The City.
for person in people['people']:
    if person['location'] == 'London':
        person['location'] = 'The City'

with open('./data/people.yml', 'w') as f:
    yaml.dump(people, f)