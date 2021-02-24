# Lori Vo 1852113

from datetime import date

months2num = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
              'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

today = date.today()
today_day = today.day
today_year = today.year
today_month = today.month

givenstring = input()

while givenstring != '-1':
    if (givenstring[-5:-4] == ' ') and (givenstring[-6:-5] == ',') and (givenstring.count(' ') == 2) \
            and givenstring[:givenstring.find(' ')] in months2num.keys():
        space1 = givenstring.find(' ')
        space2 = givenstring.rfind(' ')
        month = givenstring[0: space1]
        day = givenstring[space1+1: space2-1]
        year = givenstring[space2+1:]
        num_month = months2num[month]
        if int(year) < today_year:
            wantedoutput = str(num_month) + '/' + str(day) + '/' + str(year)
            print(wantedoutput)
        elif int(year) == today_year:
            if num_month < today_month:
                wantedoutput = str(num_month) + '/' + str(day) + '/' + str(year)
                print(wantedoutput)
            elif num_month == today_month:
                if int(day) <= today_day:
                    wantedoutput = str(num_month) + '/' + str(day) + '/' + str(year)
                    print(wantedoutput)
        givenstring = input()
    else:
        givenstring = input()
