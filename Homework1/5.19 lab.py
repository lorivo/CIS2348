import math
import string

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print("")
print("Select first service:")
firstserv=str(input())

print("Select second service:")
secondserv=str(input())
print("")

print("Davy's auto shop invoice")
print("")
costfirst=0



if firstserv=="Oil change":
    costfirst=35
elif firstserv=="Tire rotation":
    costfirst=19
elif firstserv=="Car wash":
    costfirst=7
elif firstserv=="Car wax":
    costfirst=12
elif firstserv=="-":
    costfirst=0

if firstserv!="-":
    outputtext="Service 1: {printserv1}, ${cost1}".format(printserv1=firstserv, cost1=costfirst)
else:
    outputtext="Service 1: No service"
print(outputtext)


costsecond=0

if secondserv=="Oil change":
    costsecond=35
elif secondserv=="Tire rotation":
    costsecond=19
elif secondserv=="Car wash":
    costsecond=7
elif secondserv=="Car wax":
    costsecond=12

elif secondserv=="-":
    costsecond=0

if secondserv!="-":
    outputtext2="Service 2: {printserv2}, ${cost2}".format(printserv2=secondserv, cost2=costsecond)
else:
    outputtext2="Service 2: No service"

print(outputtext2)
print("")


totalcost=costfirst+costsecond
outputtotal="Total: ${cost}".format(cost=totalcost)
print(outputtotal)



