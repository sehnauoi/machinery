from admin import *
import json

json_files = open('/workspaces/machinery/laundry/datas/settings.json')

# members = {
#     1:{'kilat':0, 'sscepat':0, 'cepat':0, 'biasa':0}, # non member
#     2:{'kilat':0, 'sscepat':0, 'cepat':0.05, 'biasa':0.1}, # bronze
#     3:{'kilat':0, 'sscepat':0.05, 'cepat':0.1, 'biasa':0.15}, # silver
#     4:{'kilat':0.05, 'sscepat':0.1, 'cepat':0.15, 'biasa':0.20}, # gold
#     5:{'kilat':0.1, 'sscepat':0.2, 'cepat':0.5, 'biasa':0.7} # platinum
# }      

def get_method(a):
    data_list = []
    method = a
    x =  json_files
    data = json.load(x)
    for x in data['method']:
        for y in x[method]:
            for b in y:
                data_list.append(y.get(b))
                # print(y.get(b))

    # print(data['method'])
    # print(data_list)
    return data_list

def get_discount(x):
    if x == 0:
        x = 1

    elif x > 12:
        x = 5

    elif x <= 3:
        x = 2

    elif x <= 6:
        x = 3

    elif x <= 12:
        x = 4

    else:
        x = 1
    x = str(x)
    disc = get_method(x)
    # kilat = members[x]['kilat']
    # sscepat = members[x]['sscepat']
    # cepat = members[x]['cepat']
    # biasa = members[x]['biasa']
    # print(disc)
    return disc

def generate_discount_price(prices, method, name):
    x, y = look_member(name)
            
    # convert membership year and month to month only so it can be subtracted to look membership type
    membership_date = int(y[0:4]) * 12 + int(y[5:7])
    converted_date = int(date[0:4]) * 12 + int(date[5:7])
    membership_counter = converted_date - membership_date

    disc = get_discount(membership_counter)

    a = prices * disc[method]
    # print(a)
    return a

# print(generate_discount_price(10000, 2, "asep"))