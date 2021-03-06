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

# part b which just requires reading given file
filedates = open('inputDates.txt')
date_filecontents = filedates.readlines()
# reads each line and puts it into a list
filedates.close()

# part c, creating new file to write into
f = open('parsedDates.txt', 'w')

for n in date_filecontents:
    # n is each part of the list
    if n != '-1':
        if (n[-6:-5] == ' ') and (n[-7:-6] == ',') and (n.count(' ') == 2) \
                and n[:n.find(' ')] in months2num.keys():
            # requirements: needs comma and space before year, space before date,
            # month should be in dictionary, 2 spaces
            space1 = (n.find(' '))
            # find first space
            space2 = (n.rfind(' '))
            # find second space
            month = n[0: space1]
            # month string is from beginning to first space
            day = n[space1+1: space2-1]
            # day string is from first space comma
            year = n[space2+1:]
            # year is from second space to end
            num_month = months2num[month]
            # converts given month to int
            if int(year) < today_year:
                # checks if year given is before today's year, if yes then output
                wantedoutput = str(num_month) + '/' + str(day) + '/' + str(year)
                # the following line writes the output into the file
                f.write(wantedoutput)
            elif int(year) == today_year:
                # if not ^, givenyear is same as today's year, check to see if given month is before
                if num_month < today_month:
                    wantedoutput = str(num_month) + '/' + str(day) + '/' + str(year)
                    f.write(wantedoutput)
                elif num_month == today_month:
                    # if not ^, if given month = today's monday then check if given day is before today or same day
                    if int(day) <= today_day:
                        wantedoutput = str(num_month) + '/' + str(day) + '/' + str(year)
                        f.write(wantedoutput)
            # input can repeat loop or exit with -1
        else:
            continue
            # repeat loop or -1
# closes writing file
f.close()
