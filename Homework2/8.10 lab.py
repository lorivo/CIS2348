# Lori Vo 1852113

string = input()

if string.replace(" ", "") == string[::-1].replace(" ", ""):
    print(string, 'is a palindrome')
else:
    print(string, 'is not a palindrome')
