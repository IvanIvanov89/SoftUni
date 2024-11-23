actor_name = input()
academy_points = float(input())
judges = int(input())

points_gained = 0

total_points = 0

for idx in range(judges):
    name_of_judge = input()
    awarded_points = float(input())

    points_awarded = (len(name_of_judge) * awarded_points) / 2

    points_gained += points_awarded

    total_points = academy_points + points_gained

    if total_points >= 1_250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break

points_missing = 1250.5 - total_points

if total_points < 1250.5:
    print(f"Sorry, {actor_name} you need {points_missing:.1f} more!")
