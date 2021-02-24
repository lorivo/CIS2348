# Lori Vo 1852113

import csv
with open(input(),'r', newline='') as csv_file:
    word_reader = csv.reader(csv_file, delimiter=',')

    words = {}
    for row in word_reader:
        for word in row:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

for key in words.keys():
    print(key, str(words[key]))
