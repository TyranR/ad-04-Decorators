# Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
# Написать декоратор из п.1, но с параметром – путь к логам.
# Применить написанный логгер к приложению из любого предыдущего д/з.

def polish_notation (operator, operand1, operand2):
    """
    Арифметические действия
    """
    if operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        try:
            result = operand1 / operand2
        except ZeroDivisionError:
            print("На ноль делить нельзя")
            result = operand1
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '+':
        result = operand1 + operand2
    return result

def main():
    """
    Основное тело программы
    """
    user_command = input("Введите польскую нотацию для двух положительных чисел: ").split()
    try:
        operator, operand1, operand2 = user_command
    except ValueError:
        print("Вы ввели больше аргументов чем надо")
        return
    operator = str(operator)
    assert operator in ['*', '/', '+', '-'], 'Такая команда не поддерживается'
    try:
        operand1 = int(operand1)
    except ValueError:
        print(f"Введеное вами число {operand1} не является числом")
        return
    try:
        operand2 = int(operand2)
    except ValueError:
        print(f"Введеное вами число {operand2} не является числом")
        return
    result = polish_notation(operator, operand1, operand2)
    print("Результат операции в Польской нотации:")
    print(f"{operand1} {operator} {operand2} = {result}")

main()
