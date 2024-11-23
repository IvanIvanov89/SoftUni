city = input()
sales_amount = float(input())
is_error = False
commission = 0
if city == 'Sofia':
    if 0 <= sales_amount <= 500:  # 5%
        commission = sales_amount * 0.05
    elif 500 < sales_amount <= 1000:  # 7%
        commission = sales_amount * 0.07
    elif 1000 < sales_amount <= 10000:  # 8%
        commission = sales_amount * 0.08
    elif sales_amount > 10000:  # 12%
        commission = sales_amount * 0.12
    else:
        is_error = True
elif city == 'Varna':
    if 0 <= sales_amount <= 500:  # 4.5%
        commission = sales_amount * 0.045
    elif 500 < sales_amount <= 1000:  # 7.5%
        commission = sales_amount * 0.075
    elif 1000 < sales_amount <= 10000:  # 10%
        commission = sales_amount * 0.1
    elif sales_amount > 10000:  # 13%
        commission = sales_amount * 0.13
    else:
        is_error = True
elif city == 'Plovdiv':
    if 0 <= sales_amount <= 500:  # 5.5%
        commission = sales_amount * 0.055
    elif 500 < sales_amount <= 1000:  # 8%
        commission = sales_amount * 0.08
    elif 1000 < sales_amount <= 10000:  # 12%
        commission = sales_amount * 0.12
    elif sales_amount > 10000:  # 14.5%
        commission = sales_amount * 0.145
    else:
        is_error = True
else:
    is_error = True
if is_error:
    print('error')
if not is_error:
    print(f'{commission:.2f}')