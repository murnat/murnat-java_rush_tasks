# Пересечение имен.

# Вызовите функцию sqrt вашего модуля math.
# Вызовите функцию sqrt встроенного модуля math.

import importlib.util
import sys

sys.path.remove('/Users/Lia/javarush/1063014/javarush-project/src/ru/javarush/python/core/level11/task17')       # тимчасово прибираємо поточну папку з пошуку
import math
sys.path.insert(0, '/Users/Lia/javarush/1063014/javarush-project/src/ru/javarush/python/core/level11/task17')

spec = importlib.util.spec_from_file_location('math', '/Users/Lia/javarush/1063014/javarush-project/src/ru/javarush/python/core/level11/task17/math.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

module.sqrt(2)
print(math.sqrt(4))