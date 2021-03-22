# Lori Vo 1852113

team = {}

for n in range(5):
    print("Enter player {}'s jersey number:".format(n+1))
    number = int(input())
    print("Enter player {}'s rating:".format(n + 1))
    rating = int(input())
    print()

    if 99 > number < 0 and 9 > rating < 0:
        break
    else:
        team[number] = rating

print('ROSTER')
sorted_team = sorted(team.items())
for number, rating in sorted_team:
    print('Jersey number: {}, Rating: {}'.format(number, rating))


option = ''

while option != 'q':
    print()
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print()
    print('Choose an option:')

    option = input()

    if option == 'o':
        sorted_team = sorted(team.items())
        print('ROSTER')
        for number, rating in sorted_team:
            print('Jersey number: {}, Rating: {}'.format(number, rating))

    if option == 'a':
        print("Enter a new player's jersey number:")
        number = int(input())
        print("Enter the player's rating:")
        rating = int(input())
        print()
        team[number] = rating

    if option == 'd':
        print('Enter a jersey number:')
        del_num = int(input())
        team.pop(del_num, None)

    if option == 'u':
        print('Enter a jersey number:')
        number = int(input())
        print('Enter a new rating for player:')
        rating = int(input())
        team[number] = rating

    if option == 'r':
        print('Enter a rating:')
        high_rating = int(input())

        print('ABOVE', high_rating)
        for number, rating in sorted_team:
            if rating > high_rating:
                print('Jersey number: {}, Rating: {}'.format(number, rating))
