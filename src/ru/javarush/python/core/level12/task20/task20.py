# Исключение несериализуемых полей
from importlib import resources


# Напишите класс, который содержит несериализуемые поля, такие как открытые файлы или базы данных,
# и реализуйте методы __getstate__() и __setstate__(),
# чтобы исключить эти поля при сериализации и восстановить их при десериализации.
import pickle
class MyClass:
    def __init__(self, value, files, db, res):
        self.value = value
        self.files = files
        self.db = db
        self.res = res

    def __getstate__(self):
        state = self.__dict__.copy()
        for key in ('files','db','res'):
            del state[key]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.files = 'Restored files'
        self.db = 'New DB connection'
        self.res = 'Other new resources'

    def __repr__(self):
        return f"Class {MyClass.__name__}: (value={self.value}, files={self.files}, db={self.db}, res={self.res})"

new_obj = MyClass(42, 'file paths', 'db connection', 'resources')
print(f'Before serializing: {new_obj}')

with open('test.pkl', 'wb') as file:
    pickle.dump(new_obj, file)

with open('test.pkl', 'rb') as file:
    loaded_obj = pickle.load(file)

print(f'After serializing: {loaded_obj}')





