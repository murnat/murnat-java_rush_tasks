# Редактор.

# Напишите программу, которая создает словарь с информацией о книге (название, автор, год издания).
# Программа должна:
# Изменить значение ключа "год издания".
# Использовать метод setdefault() для добавления нового ключа "издательство", если он отсутствует.
# Обновить значения нескольких элементов с использованием метода update().
# Вывести обновленный словарь после каждого изменения.

book = {
    "title":"A Song of Ice and Fire",
    "author":"George Martin",
    "year":1991
}

book["year"] = 1992
print(book)

publishing_house = book.setdefault("издательство","Some publishing house")
print(book)

updates = {
    "year":1999,
    "reissue":True
}
book.update(updates)
print(book)