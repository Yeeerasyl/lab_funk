expenses = {}
categories = ['транспорт', 'обед', 'развлечения']

days=['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
for day in days:
    print(f'Введите расходы за {day}:')
    for category in categories:
        expense = float(input(f'{category}: '))
        
        if category in expenses:
            expenses[category] += expense
        else:
            expenses[category] = expense
    
    print('------------------------')

print('Итоговые расходы:')
for category, expense in expenses.items():
    print(f'{category}: {expense}')

total_expenses = sum(expenses.values())
print(f'Общий объем расходов за неделю: {total_expenses}')
