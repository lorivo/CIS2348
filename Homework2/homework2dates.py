# Lori Vo 1852113

from datetime import date

months2num = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
              'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
# dictionary that converts months to ints

today = date.today()
today_day = today.day
# int value for today's date
today_year = today.year
# int value for today's year
today_month = today.month
# int value for today's month

givenstring = input()

while givenstring != '-1':
    if (givenstring[-5:-4] == ' ') and (givenstring[-6:-5] == ',') and (givenstring.count(' ') == 2) \
            and givenstring[:givenstring.find(' ')] in months2num.keys():
        # requirements: needs comma and space before year, space before date, month should be in dictionary, 2 spaces
        space1 = givenstring.find(' ')
        # find first space
        space2 = givenstring.rfind(' ')
        # find second space
        month = givenstring[0: space1]
        # month string is from beginning to first space
        day = givenstring[space1+1: space2-1]
        # day string is from first space comma
        year = givenstring[space2+1:]
        # year is from second space to end
        num_month = months2num[month]
        # converts given month to int
        if int(year) < today_year:
            # checks if year given is before today's year, if yes then output
            wantedoutput = str(num_month) + '/' + str(day) + '/' + str(year)
            print(wantedoutput)
        elif int(year) == today_year:
            # if not ^, givenyear is same as today's year, check to see if given month is before
            if num_month < today_month:
                wantedoutput = str(num_month) + '/' + str(day) + '/' + str(year)
                print(wantedoutput)
            elif num_month == today_month:
                # if not ^, if given month = today's monday then check if given day is before today or same day
                if int(day) <= today_day:
                    wantedoutput = str(num_month) + '/' + str(day) + '/' + str(year)
                    print(wantedoutput)
        givenstring = input()
        # input can repeat loop or exit with -1
    else:
        givenstring = input()
        # repeat loop or -1
