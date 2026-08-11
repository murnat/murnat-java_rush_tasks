# Использование декодера

# Напишите программу, которая десериализует JSON-строку в объект Python с использованием
# пользовательского декодера для преобразования строк ISO в объекты datetime.

import json
from datetime import datetime

def custom_decoder(dct):
    if 'timestamp' in dct.keys():
        dct['timestamp'] = datetime.fromisoformat(dct['timestamp'])
    return dct

json_string = '''
{
    "name": "Alice",
    "timestamp": "2023-05-15T14:30:00"
}
'''

loaded_json = json.loads(json_string, object_hook=custom_decoder)
print(loaded_json)
