# НДС

# Напишите функцию calculate_total_cost(price, tax=0.2), которая принимает цену товара и необязательный параметр налог (по умолчанию 20%).
# Функция должна вычислять и выводить общую стоимость товара с учетом налога.
# Затем напишите программу, которая вызывает эту функцию с различными параметрами.

def calculate_total_cost(price, tax=0.2):
    print(f"{price * (tax + 1):.2f}")

calculate_total_cost(10)
calculate_total_cost(45,0.1)
calculate_total_cost(5,0.5)