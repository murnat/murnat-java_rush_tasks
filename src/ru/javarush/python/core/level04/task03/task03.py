# Мешанина

# Напишите программу, которая запрашивает у пользователя целое число, вещественное число и строку.
# Затем преобразуйте целое число в вещественное, вещественное число в строку, и строку в целое число (если это возможно).
# Выведите результаты преобразований и их типы.
# request data
num_int = int(input("Provide integer: "))
num_float = float(input("Provide float number: "))
var_str = str(input("Provide string: "))
# cast types
num_int = float(num_int)
num_float = str(num_float)
var_str = int(var_str)
# print results with types
print(num_int,"-",type(num_int),"\n",num_float,"-",type(num_float),"\n",var_str,"-",type(var_str))
