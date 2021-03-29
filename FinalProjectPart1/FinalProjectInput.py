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
        string1 = temp[1]
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

