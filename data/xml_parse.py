# A:
# Prints the cost of the largest sq.ft detached home for sale.
import xmltodict
with open('./data/properties.xml', 'r') as f:
    data = xmltodict.parse(f.read())


detached_data =data['properties']['sale']['detached']
detached_homes = detached_data.keys()
plot = [(ele,detached_data[ele]['plot_size']) for ele in detached_homes]

big_plot = max(plot, key=lambda item: item[1])[0]
# print(detached_data[big_plot]['cost'])


# B:
# Prints the description of the third home from the bungalows for sale.
# bungalow_data =data['properties']['sale']['bungalow']
# bungalows = [ele for ele in bungalow_data]
# print(bungalow_data[bungalows[2]]['description'])

# C:
# Prints the number of bathrooms that the first flat for rent has.
# flat_data = data['properties']['rent']['flat']
# flat=[ele for ele in flat_data]
# print(flat_data[flat[0]]['bathrooms'])



# D:
# Prints a list of all of the bungalows.
rented_bungalows =data['properties']['rent']['bungalow']
rented_bungalow_dicts = [rented_bungalows[key] for key in rented_bungalows.keys()]

sale_bungalows =data['properties']['sale']['bungalow']
sale_bungalow_dicts = [sale_bungalows[key] for key in sale_bungalows.keys()]

# print(sale_bungalow_dicts + rented_bungalow_dicts)


# E:
# Prints a dictionary which lists the average property price for each property type.
def get_averages(sale_or_rent):
    types = [ele for ele in data['properties'][sale_or_rent]]
    average_cost_obj ={}
    for property_type in types:
        total_property_price =0
        number_of_properties =0
        for prop in data['properties'][sale_or_rent][property_type]:
            total_property_price+=int(data['properties'][sale_or_rent][property_type][prop]['cost'][1:])
            number_of_properties +=1
        average_cost_obj[f"{sale_or_rent}-{property_type}"]=round(total_property_price/number_of_properties,2)
    return average_cost_obj

# print({**get_averages('rent'), **get_averages('sale')})


# # F:
# # Adds a new bungalow for sale to the properties data.
# # G:

# # Renting has just become even more unaffordable. Increase all properties to rent by 5%.
# # H:
all_rentals = data['properties']['rent']
for house_type in all_rentals:
    for house in all_rentals[house_type]:
        cost_str = all_rentals[house_type][house]['cost']
        cost_num = int(cost_str[1:])
        cost_increased = round(cost_num *1.05,2)
        all_rentals[house_type][house]['cost'] = f"£{cost_increased}"
print(data)

# # There is a new PARK HOME property type available to rent. This home has 2 bedrooms and costs £2000. Update the data to reflect this.