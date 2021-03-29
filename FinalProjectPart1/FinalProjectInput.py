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
        data_dictionary[temp[0]].append(temp[1:])
    price_file.close()
#    print(data_dictionary)

    SD_file = open(SD_name)
    for line in SD_file.readlines():
        line = line.strip()
        temp = line.split(',')
#        print(temp)
        data_dictionary[temp[0]].append(temp[1:])
    SD_file.close()
#    print(data_dictionary)

except:
    print("Error reading file or gathering data")

# writes Full Inventory!!!
of = open('FullInventory.csv', 'w')
for n in data_dictionary:
    value1 = n # ID
    value2 = data_dictionary[n][0] #Manufacturer
    value3 = data_dictionary[n][1] # Item type
    value4 = data_dictionary[n][3] # Price
    value5 = data_dictionary[n][4] # Service date
    value6 = data_dictionary[n][2] # if damaged
    of.write("{}, {}, {}, {}, {}, {}".format(value1, value2, value3, value4, value5, value6))
    of.write('\n')
#    print(n)
of.close()
