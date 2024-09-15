import json

class Model:
    title = '1'
    text = '2'
    author = '3'

    def save(self):
        with open("dictionary.json", "w") as write_file:
            # Сохраняем атрибуты экземпляра в словаре
            data = {
                "title": self.title,
                "text": self.text,
                "author": self.author
            }
            json.dump(data, write_file)

M = Model()

# Вызываем метод save для сохранения данных в файл
M.save()