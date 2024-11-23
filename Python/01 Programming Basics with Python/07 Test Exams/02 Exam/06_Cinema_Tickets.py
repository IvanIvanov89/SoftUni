student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0
command = input()

while command != 'Finish':
    movie_name = command
    free_spaces = int(input())
    tickets_bought = 0

    for idx in range(free_spaces):
        ticket_type = input()
        if ticket_type == 'End':
            break
        if ticket_type == 'student':
            student_tickets += 1
            tickets_bought += 1
            total_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
            tickets_bought += 1
            total_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1
            tickets_bought += 1
            total_tickets += 1
    percent_full = (tickets_bought / free_spaces) * 100
    print(f'{movie_name} - {percent_full :.2f}% full.')
    command = input()

print(f'Total tickets: {total_tickets}')
print(f'{(student_tickets / total_tickets) * 100 :.2f}% student tickets.')
print(f'{(standard_tickets / total_tickets) * 100 :.2f}% standard tickets.')
print(f'{(kid_tickets / total_tickets) * 100 :.2f}% kids tickets.')
