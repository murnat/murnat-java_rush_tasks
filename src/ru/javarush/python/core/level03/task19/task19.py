# F-нотация

# Напишите программу, которая запрашивает у пользователя его имя, возраст и город.
# Затем используйте f-нотацию, чтобы вывести сообщение в следующем формате: "Привет, {имя}! Тебе {возраст} лет, и ты живешь в городе {город}."

# request data
name = input("What is your name? ")
age = int(input("How old are you? "))
city = input("What city do you live in? ")
# print the result
print(f"Привет, {name}! Тебе {age} лет, и ты живешь в городе {city}.")
