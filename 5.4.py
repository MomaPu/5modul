import json

class Model:
   
    def __init__(self, title='1', text='2', author='3'):
        self.title = title
        self.text = text
        self.author = author

    def save(self):
        # Создаем словарь из атрибутов экземпляра
        data = {
            'title': self.title,
            'text': self.text,
            'author': self.author
        }

        # Записываем словарь в JSON-файл
        with open("dictionary.json", "w") as write_file:
            json.dump(data, write_file)  # добавление в json

M = Model()
# Вызываем метод save для сохранения данных в файл
M.save()