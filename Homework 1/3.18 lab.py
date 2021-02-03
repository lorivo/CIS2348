# Lori Vo 1852113

import math


print("Enter wall height (feet):")
height = int(input())
print("Enter wall width (feet):")
width = int(input())
area = width*height
print("Wall area:", area, "square feet")

galneeded = area/350
print("Paint needed:", '{:.2f}'.format(galneeded), "gallons")

cansneeded = math.ceil(galneeded)
print("Cans needed:", cansneeded, "can(s)")
print("")

print("Choose a color to paint the wall:")
color = str(input())
red = 35
blue = 25
green = 23
cost = 0
if color == "red":
    cost = cansneeded*red
if color == "blue":
    cost = cansneeded*blue
if color == "green":
    cost = cansneeded*green
txt1 = "Cost of purchasing {printcolor} paint: ${printcost}".format(printcolor=color, printcost=cost)
print(txt1)
