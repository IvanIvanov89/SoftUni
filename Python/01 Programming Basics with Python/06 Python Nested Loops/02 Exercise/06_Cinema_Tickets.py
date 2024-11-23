command = input()

ticket_student = 0
ticket_standard = 0
ticket_kid = 0

while command != 'Finish':
    movie_name = command
    free_spaces = int(input())
    sold = 0
    while free_spaces > sold:
        one_sold = input()

        if one_sold == 'End':
            break
        elif one_sold == 'student':
            ticket_student += 1
            sold += 1
        elif one_sold == 'standard':
            ticket_standard += 1
            sold += 1
        elif one_sold == 'kid':
            ticket_kid += 1
            sold += 1

    used_space_percent = (sold / free_spaces) * 100
    print(f'{movie_name} - {used_space_percent :.2f}% full.')
    command = input()

total_sold = ticket_student + ticket_standard + ticket_kid
print(f'Total tickets: {total_sold}')
print(f'{(ticket_student / total_sold) * 100 :.2f}% student tickets.')
print(f'{(ticket_standard / total_sold) * 100 :.2f}% standard tickets.')
print(f'{(ticket_kid / total_sold) * 100 :.2f}% kids tickets.')
