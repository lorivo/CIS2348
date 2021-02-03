#Lori Vo
#1852113

import math

print("Enter amount of lemon juice (in cups):")
lemonjcup=float(input())
print("Enter amount of water (in cups):")
watercup=float(input())
print("Enter amount of agave nectar (in cups):")
nectarcup=float(input())
print("How many servings does this make?")
servings=float(input())
print("")
print("Lemonade ingredients - yields",'{:.2f}'.format(servings),"servings")
print('{:.2f}'.format(lemonjcup),"cup(s) lemon juice")
print('{:.2f}'.format(watercup),"cup(s) water")
print('{:.2f}'.format(nectarcup),"cup(s) agave nectar")
print("")
print("How many servings would you like to make?")
servingslike=float(input())
print("")
proportion=servingslike/servings
print("Lemonade ingredients - yields",'{:.2f}'.format(servingslike),"servings")
print('{:.2f}'.format(lemonjcup*proportion),"cup(s) lemon juice")
print('{:.2f}'.format(watercup*proportion),"cup(s) water")
print('{:.2f}'.format(nectarcup*proportion),"cup(s) agave nectar")
print("")
print("Lemonade ingredients - yields",'{:.2f}'.format(servingslike),"servings")
print('{:.2f}'.format((lemonjcup*proportion)/16),"gallon(s) lemon juice")
print('{:.2f}'.format((watercup*proportion)/16),"gallon(s) water")
print('{:.2f}'.format((nectarcup*proportion)/16),"gallon(s) agave nectar")