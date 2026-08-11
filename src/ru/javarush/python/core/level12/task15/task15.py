# Сериализация помощью pickle

# Напишите программу, которая сериализует и десериализует объект Python с использованием модуля pickle.
# Объектом для сериализации будет словарь, содержащий информацию о студенте: имя, возраст и статус студента.

import pickle
# Объект для сериализации
student_info = {
    'name': 'John Doe',
    'age': 20,
    'status': 'student'
}

with open('student_info.pkl', 'wb') as file:
    pickle.dump(student_info, file)

with open('student_info.pkl', 'rb') as file:
    loaded_student_info = pickle.load(file)
    print(loaded_student_info)