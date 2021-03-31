# Lori Vo 1852113
# Final Project for CIS 2348


# reads given lists and adds to dictionary
man_name = "ManufacturerList.csv"
price_name = "PriceList.csv"
SD_name = "ServiceDatesList.csv"

data_dictionary = {}
try:
    man_file = open(man_name)
    for line in man_file.readlines():
        line = line.strip()
        temp = line.split(',')
#        print(temp)
        data_dictionary[temp[0]] = temp[1:]
    man_file.close()
#    print(data_dictionary)

    price_file = open(price_name)
    for line in price_file.readlines():
        line = line.strip()
        temp = line.split(',')
#        print(temp)
        string1 = temp[1]  # makes text on file a string instead of list
        data_dictionary[temp[0]].append(string1)
    price_file.close()
#    print(data_dictionary)

    SD_file = open(SD_name)
    for line in SD_file.readlines():
        line = line.strip()
        temp = line.split(',')
#        print(temp)
        string2 = temp[1]  # information that will be appended into a string and not a list
        data_dictionary[temp[0]].append(string2)
    SD_file.close()
#    print(data_dictionary)

except:
    print("Error reading file or gathering data")

# writes Full Inventory!!!
of = open('FullInventory.csv', 'w')

# creates sorted dictionary for output part a
sorted_man = {}
sorted_names = sorted(data_dictionary.values())
# sorts the dictionary into new dictionary
for i in sorted_names:
    for k in data_dictionary.keys():
        if data_dictionary[k] == i:
            sorted_man[k] = (data_dictionary[k])
# print(sorted_man)

for n in sorted_man:
    value1 = n  # ID
    value2 = data_dictionary[n][0]  # Manufacturer
    value3 = data_dictionary[n][1]  # Item type
    value4 = data_dictionary[n][3]  # Price
    value5 = data_dictionary[n][4]  # Service date
    value6 = data_dictionary[n][2]  # if damaged
    of.write("{}, {}, {}, {}, {}, {}".format(value1, value2, value3, value4, value5, value6))
    of.write('\n')
#    print(n)
of.close()

# inventory type list

sorted_items = dict(sorted(data_dictionary.items(), key=lambda data_dictionary: data_dictionary[1][1]))
# sorts by item type
# print(sorted_items)

item_type = ""  # empty string for item type to change later in the code

for u in sorted_items:
    if item_type != sorted_items[u][1]:  # item type is different from before, initially ''
        item_type = sorted_items[u][1]  # data dictionary's value of item type
        op = open(item_type+"Inventory.csv", 'w')  # makes new file to write in
        value1 = u  # ID
        value2 = data_dictionary[u][0]  # Manufacturer
        value3 = data_dictionary[u][1]  # Item type
        value4 = data_dictionary[u][3]  # Price
        value5 = data_dictionary[u][4]  # Service date
        value6 = data_dictionary[u][2]  # if damaged
        op.write("{}, {}, {}, {}, {}, {}".format(value1, value2, value3, value4, value5, value6))
        op.write('\n')
    else:  # if item type is same as before
        op = open(item_type + "Inventory.csv", 'a')   # appends to previous file instead of creating a new one
        value1 = u  # ID
        value2 = data_dictionary[u][0]  # Manufacturer
        value3 = data_dictionary[u][1]  # Item type
        value4 = data_dictionary[u][3]  # Price
        value5 = data_dictionary[u][4]  # Service date
        value6 = data_dictionary[u][2]  # if damaged
        op.write("{}, {}, {}, {}, {}, {}".format(value1, value2, value3, value4, value5, value6))
        op.write('\n')
    op.close()

# writes damage inventory file!!
# converts price information to int so I could sort from greatest to least
for n in data_dictionary:
    data_dictionary[n][3] = int(data_dictionary[n][3])
# print(data_dictionary)

# new dictionary that sorts from greatest to least
# reverse is used bc the function without it makes it least to greatest
price_sort = dict(sorted(data_dictionary.items(), key=lambda data_dictionary: data_dictionary[1][3], reverse=True))
# print(price_sort)

os = open('DamagedInventory.csv', 'w')

for e in price_sort:
    if price_sort[e][2] == 'damaged':
        value1 = e  # ID
        value2 = data_dictionary[e][0]  # Manufacturer
        value3 = data_dictionary[e][1]  # Item type
        value4 = data_dictionary[e][3]  # Price
        value5 = data_dictionary[e][4]  # Service date
        os.write("{}, {}, {}, {}, {}".format(value1, value2, value3, value4, value5))
        os.write('\n')
os.close()
