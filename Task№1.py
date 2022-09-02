# Задача 1. Напишите программу, которая принимает на
# вход цифру, обозначающую день недели, и выводит
# название этого дня недели.

number_day = int(input('Введите цифру, обозначающую день недели(от 1 до 7):  '))
while (1 > number_day or number_day > 7):
    number_day = int(input('Введите цифру, обозначающую день недели:  '))
if number_day == 1:
    print('нет')
elif number_day == 2:
    print('нет')
elif number_day == 3:
    print('нет')
elif number_day == 4:
    print('нет')
elif number_day == 5:
    print('нет')
elif number_day == 6:
    print('да')
elif number_day == 7:
    print('да')

# или

def find_day(number: int):
    if day == 6 or day == 7:
        return f'День номер {day} это выходной!'
    elif day == 0 or day > 7:
        return 'В неделе 7 дней введите число от 1 до 7'
    else:
        return f'День номер {day} рабочий!'

day = int(input('Введите номер дня от 1 до 7: '))
print(find_day(day))
