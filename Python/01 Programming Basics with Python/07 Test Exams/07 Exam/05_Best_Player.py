command = input()

best_player_name = ''
best_player_goals = 0
hat_trick = False

while command != 'END':
    player_name = command
    goals_scored = int(input())
    if goals_scored > best_player_goals:
        best_player_goals = goals_scored
        best_player_name = player_name
        if goals_scored >= 3:
            hat_trick = True
    if goals_scored >= 10:
        break

    command = input()

print(f'{best_player_name} is the best player!')
if hat_trick:
    print(f'He has scored {best_player_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_player_goals} goals.')
