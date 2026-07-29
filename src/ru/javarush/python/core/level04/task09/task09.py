# Доступ запрещен

# Напишите программу, которая запрашивает у пользователя имя пользователя и пароль.
# Если имя пользователя равно "admin" и пароль равен "1234", программа должна вывести сообщение "Доступ разрешен".
# В противном случае программа должна вывести сообщение "Доступ запрещен".

# request login and password
login = input("Enter your login name: ")
password = input("Enter your password: ")
access_allowed = login == "admin" and password == "1234"
if access_allowed:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")