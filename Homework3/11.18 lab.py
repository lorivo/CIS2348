# Lori Vo 1852113

num_list = input().split()
new_list = []

for n in num_list:
    n = int(n)
    if n >= 0:
        new_list.append(n)

new_list.sort()
for i in new_list:
    print(i, end=' ')
