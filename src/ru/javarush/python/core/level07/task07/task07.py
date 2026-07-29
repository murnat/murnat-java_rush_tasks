# Три проверки.

# Напишите программу, которая создает словарь с информацией о книге (title, author, year).
# Программа должна:
# Проверить наличие ключа "author" с использованием оператора in.
# Проверить наличие ключа "publisher" с использованием метода get().
# Проверить наличие ключа "title" с использованием метода keys().

book = {
    "title":"A Song of Ice and Fire",
    "author":"George Martin",
    "year":1991
}
if "author" in book:
    print('Key author is in the dict')
else:
    print('Key author is not in the dict')

key = book.get("publisher")
if key is None:
    print('Key publisher is not in the dict')
else:
    print('Key publisher is in the dict')

if "title" in book.keys():
    print('Key title is in the dict')
else:
    print('Key title is not in the dict')


