# Lori Vo 1852113

def exact_change(user_total):
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    if user_total == 0:
        print('no change')

    if user_total >= 100:
        dollars = user_total // 100
        user_total -= dollars * 100
    if user_total >= 25:
        quarters = user_total // 25
        user_total -= quarters * 25
    if user_total >= 10:
        dimes = user_total // 10
        user_total -= dimes * 10
    if user_total >= 5:
        nickels = user_total // 5
        user_total -= nickels * 5
    if user_total >= 1:
        pennies = user_total // 1
        user_total -= pennies * 1

    return dollars, quarters, dimes, nickels, pennies


def main():
    inputval = int(input())
    dollars, quarters, dimes, nickels, pennies = exact_change(inputval)
    if dollars > 1:
        print(dollars, 'dollars')
    elif 1 >= dollars > 0:
        print(dollars, 'dollar')
    if quarters > 1:
        print(quarters, 'quarters')
    elif 1 >= quarters > 0:
        print(quarters, 'quarter')
    if dimes > 1:
        print(dimes, 'dimes')
    elif 1 >= dimes > 0:
        print(dimes, 'dime')
    if nickels > 1:
        print(nickels, 'nickels')
    elif 1 >= nickels > 0:
        print(nickels, 'nickel')
    if pennies > 1:
        print(pennies, 'pennies')
    elif 1 >= pennies > 0:
        print(pennies, 'penny')


if __name__ == '__main__':
    main()
