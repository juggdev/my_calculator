def calculate(a,b,check):
    if check == '/' and b == 0:
        return 'Ошибка: на ноль делить нельзя!'
    if check == '+':
        return a + b
    if check == '-':
        return a - b
    if check == '*':
        return a * b
    if check == '/':
        return a / b
    else:
        return 'Ошибка: введён неверный знак операции'

a = float(input('Введите первое число:'))
check = (input('Введите знак операции:'))
b = float(input('Введите второе число:'))

result = calculate(a,b,check)
print('Ответ:', result)