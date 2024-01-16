# A:
# Prints the cost of the largest sq.ft detached home for sale.
import xmltodict
with open('./data/properties.xml', 'r') as f:
    data = xmltodict.parse(f.read())
    detached_data =data['properties']['sale']['detached']
    hommmme = detached_data.keys()
    plot = [(ele,detached_data[ele]['plot_size']) for ele in hommmme]

    big_plot = max(plot, key=lambda item: item[1])[0]
    # print(detached_data[big_plot]['cost'])


# B:
# Prints the description of the third home from the bungalows for sale.
bungalow_data =data['properties']['sale']['bungalow']
bungalows = [ele for ele in bungalow_data]
# print(bungalow_data[bungalows[2]])

# C:
# Prints the number of bathrooms that the first flat for rent has.
flat_data = data['properties']['rent']['flat']
flat=[ele for ele in flat_data]
# print(flat_data[flat[0]]['bathrooms'])



from collections import ChainMap
# D:
# Prints a list of all of the bungalows.
bungalow_data_rented =data['properties']['rent']['bungalow']
bungalows_rent = [ele for ele in bungalow_data_rented]
merged = ChainMap(bungalow_data_rented,bungalow_data)
# print(merged)
# print(bungalows_rent+ bungalows)

# E:
# Prints a dictionary which lists the average property price for each property type.
sale = [ele for ele in data['properties']['sale']]
# print(sale)
average_cost_obj ={}
for property_type in sale:
    total_property_price =0
    number_of_properties =0
    for prop in data['properties']['sale'][property_type]:
        # print(prop)
        total_property_price+=int(data['properties']['sale'][property_type][prop]['cost'][1:])
        number_of_properties +=1
    average_cost_obj[f"sale-{prop}"]=round(total_property_price/number_of_properties,2)



rent = [ele for ele in data['properties']['rent']]
for property_type in rent:
    total_property_price =0
    number_of_properties =0
    for prop in data['properties']['rent'][property_type]:
        total_property_price+=int(data['properties']['rent'][property_type][prop]['cost'][1:])
        number_of_properties +=1
    average_cost_obj[f"rent-{prop}"]=round(total_property_price/number_of_properties,2)

print(average_cost_obj)


# print(sale)

# F:
# Adds a new bungalow for sale to the properties data.
# G:

# Renting has just become even more unaffordable. Increase all properties to rent by 5%.
# H:

# There is a new PARK HOME property type available to rent. This home has 2 bedrooms and costs £2000. Update the data to reflect this.