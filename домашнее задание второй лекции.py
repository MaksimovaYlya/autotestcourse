print('Домашнее задание №2')
print('Задача 1')
sade_of_square = 5
print('Сторона квадрата =', sade_of_square)
perimeter = sade_of_square * 4
print('P =', perimeter)
square = sade_of_square ** 2
print('S =', square)
diagonal = ((sade_of_square ** 2) + (sade_of_square ** 2)) ** 0.5
print('D =', diagonal)

print('Задача 2')
print('ax^2 + bx + c = 0')
a = 1
b = -6
c = 4
discriminant = b ** 2 - 4 * a * c
x1 = (-1 * b + discriminant ** 0.5) / 2 * a
x2 = (-1 * b - discriminant ** 0.5) / 2 * a
print('x1 =', round(x1, 2))
print('x2 =', round(x2, 2))

print('Задача 3')
string1 = 'Первая строка'
string2 = 'Вторая строка'
print(string1, string2)
print(string1[:2] + string2[2:], string2[:2] + string1[2:])
print(string1.replace(string1[:2], string2[:2]), string2.replace(string2[2:], string1[2:]))

print('Задача 4')
path_to_file = r'C:\Users\um.maksimova\PycharmProjects\pythonProject\домашнее задание второй лекции.py'
print(path_to_file[-33:-3])

divider = (path_to_file.split('\\'))
file_name = (divider[-1])
without_py = file_name.split('.')[0]
print(without_py)
print(divider[0])
print(divider[1])
print('Задача 5')
a = 7
b = 2
c = a + b
result_1 = """%d + %d = %d""" % (a, b, c)
print(result_1)
c = a * b
result_2 = f"""%d * %d = %d""" % (a, b, c)
print(result_2)

print('Задача 6')
string = 'Ничего не понимаю'
result = string[::2]
print(result)

print('Задача 7')
first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox'
first_letter = (second_string.find(first_string[0]))
second_letter = (second_string.find(first_string[1]))
third_letter = (second_string.find(first_string[2]))
print(second_string[min(first_letter, second_letter, third_letter):max(first_letter, second_letter, third_letter) + 1])
