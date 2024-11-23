username = input()
password = input()

entry_password = input()

while True:
    if entry_password == password:
        print(f'Welcome {username}!')
        break
    entry_password = input()
