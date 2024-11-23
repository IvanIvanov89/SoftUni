pool_volume = int(input())
pipe_one_debit = int(input())
pipe_two_debit = int(input())
time_in_hours = float(input())

pipe_one_volume = pipe_one_debit * time_in_hours
pipe_two_volume = pipe_two_debit * time_in_hours

total_volume_of_pipes = pipe_one_volume + pipe_two_volume

percent_pipe_one = (pipe_one_volume * 100) / total_volume_of_pipes
percent_pipe_two = (pipe_two_volume * 100) / total_volume_of_pipes

pool_percentage = (total_volume_of_pipes * 100) / pool_volume

overflow = total_volume_of_pipes - pool_volume

if overflow <= 0:
    print(f'The pool is {pool_percentage:.2f}% full. Pipe 1: {percent_pipe_one:.2f}%. Pipe 2: {percent_pipe_two:.2f}%.')

else:
    print(f'For {time_in_hours} hours the pool overflows with {overflow:.2f} liters.')