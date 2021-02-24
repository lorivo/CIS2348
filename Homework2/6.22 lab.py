# Lori Vo 1852113

x1 = int(input())
y1 = int(input())
num1 = int(input())
x2 = int(input())
y2 = int(input())
num2 = int(input())

sub1 = 0
sub2 = 0

for n in range(-10, 10):
    for i in range(-10, 10):
        if x1*n+y1*i == num1 and x2*n+y2*i == num2:
            sub1 = n
            sub2 = i
            break
        else:
            continue

if sub1 != 0 and sub2 != 0:
    print(sub1, sub2)
else:
    print("No solution")