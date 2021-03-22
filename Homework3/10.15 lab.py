# Lori Vo 1852113

class Team:
    def __init__(self, name='none', win=0, lose=0):
        self.name = name
        self.team_wins = win
        self.team_losses = lose

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


if __name__ == '__main__':

    given_team = Team()
    given_team.name = input()
    given_team.team_wins = int(input())
    given_team.team_losses = int(input())

    percentage = given_team.get_win_percentage()
    if percentage > 0.5:
        print('Congratulations, Team {} has a winning average!'.format(given_team.name))
    else:
        print('Team {} has a losing average.'.format(given_team.name))
