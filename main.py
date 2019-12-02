# Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
# Написать декоратор из п.1, но с параметром – путь к логам.
# Применить написанный логгер к приложению из любого предыдущего д/з.
from datetime import datetime


class Logwork:

    def __init__(self, path, mode='rt'):
        self.file = open(path, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def decor(old_function):
    """
    Он записывает в файл дату и время вызова функции,
    имя функции, аргументы, с которыми вызвалась и возвращаемое значение
    """
    print(f"******Функция {old_function} будет декорирована****")

    def new_function(*args):
        with Logwork("log.txt", "w") as file:
            start_time = datetime.now()
            file.write(f"Время начала вызова функции {old_function} - {start_time}\n")
            print(f"Время начала вызова функции {old_function} - {start_time}")
            ret = old_function(*args)
            arg = args
            file.write(f"Переданные в функцию {old_function} аргументы {arg}\n")
            print(f"Переданные в функцию {old_function} аргументы {arg}")
            file.write(f"Возвращаемое значение {ret}\n")
            print(f"Возвращаемое значение {ret}")
            stop_time = datetime.now()
            file.write(f"Время окончания вызова функции {old_function} - {stop_time}\n")
            print(f"Время окончания вызова функции {old_function} - {stop_time}")
            return ret
    return new_function


def parametrized_decor(file):
    """
    Написать декоратор из п.1, но с параметром – путь к логам.
    """
    def decor(old_function):
        print(f"******Функция {old_function} будет декорирована****")

        def new_function(*args):
            nonlocal file
            with Logwork(file, "w") as file:
                start_time = datetime.now()
                file.write(f"Время начала вызова функции {old_function} - {start_time}\n")
                print(f"Время начала вызова функции {old_function} - {start_time}")
                ret = old_function(*args)
                arg = args
                file.write(f"Переданные в функцию {old_function} аргументы {arg}\n")
                print(f"Переданные в функцию {old_function} аргументы {arg}")
                file.write(f"Возвращаемое значение {ret}\n")
                print(f"Возвращаемое значение {ret}")
                stop_time = datetime.now()
                file.write(f"Время окончания вызова функции {old_function} - {stop_time}\n")
                print(f"Время окончания вызова функции {old_function} - {stop_time}")
                return ret
        return new_function
    return decor


@decor
def polish_notation(operator, operand1, operand2):
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


@parametrized_decor('log2.txt')
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
