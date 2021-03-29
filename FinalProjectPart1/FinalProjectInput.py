# Lori Vo 1852113
# Final Project for CIS 2348

# reads manufacturer list
man_name = "ManufacturerList.csv"
data = []
data_dictionary = {}
try:
    man_file = open(man_name)
    for line in man_file.readlines():
        data.append(line.strip())
        data_dictionary[line[0:7]] = line[8:]

    man_file.close()
    print(data)
    print(data_dictionary)

except:
    print("Error reading file or gathering data")
