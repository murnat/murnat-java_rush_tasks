# Символы в строке

# Напишите программу, которая принимает строку от пользователя, выводит ее длину,
# а затем запрашивает у пользователя индекс.
# Программа должна вывести символ строки по этому индексу.
# Если индекс выходит за пределы строки, программа должна вывести соответствующее сообщение.

strng = input('Provide any string: ')
print(f'The length of the string is {len(strng)}')
ind = int(input('Provide an index: '))
if ind < 0 or ind >= len(strng):
    print('The index is out of range')
else:
    print(f'Char by the index is: {strng[ind]}')