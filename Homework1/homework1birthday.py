# Lori Vo
# Homework 1
# 1852113

print("Birthday Calculator ")
print("Current day")
givenmonth = int(input("Month: "))
givendate = int(input("Day: "))
givenyear = int(input("Year: "))

print("Birthday")
birthmonth = int(input("Month: "))
birthday = int(input("Day: "))
birthyear = int(input("Year: "))

if givenmonth >= birthmonth:
    if givendate >= birthday:
        print("You are", (givenyear-birthyear), "years old.")
    else:
        print("You are", (givenyear - birthyear)-1, "years old.")
else:
    print("You are", (givenyear-birthyear)-1, "years old.")

if (givenmonth == birthmonth) and (givendate == birthday):
    print("Happy Birthday!")
