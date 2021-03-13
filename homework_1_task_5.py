revenue = float(input("input company's revenue: "))
expense = float(input("input company's expanse: "))
balance = revenue - expense
print('your balance = ', balance, '$')

profit = 0

if balance > 0:
    profit = balance / revenue * 100
    print('cost-effectiveness ', round(profit,2), '%')
else:
    print('not profitable')

emp_number = int(input('set number of employees: '))
profit_on_emp = balance / emp_number
print('profit per 1 employee = ', round(profit_on_emp, 2), '$', 'per emp.')
