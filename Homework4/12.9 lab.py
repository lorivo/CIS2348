# Lori Vo 1852113
user_name = ''
while user_name != '-1':
    try:
        user_info = input().split(' ')
        user_name = user_info[0]
        user_age = int(user_info[1])
        user_age += 1
      #  print(user_name, user_age)
    except ValueError:
        user_age = 0
    print(user_name, user_age)
