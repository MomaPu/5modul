import json

class Model:
    def __init__(self, title='1', text='2', author='3'):
        self.title = title
        self.text = text
        self.author = author

    def save(self):
        # Создаем словарь из атрибутов экземпляра
        data = self.__dict__ # пользовательские
        data2 = []
        for x in dir(Model): # запись всех аттрибутов
            data2.append(x)
        
        # Записываем словарь в JSON-файл
        with open("dictionary.json", "w") as write_file:
            json.dump(data, write_file)  # добавление в json
            json.dump(data2, write_file)

# Создаем экземпляр класса
M = Model()
# Вызываем метод save для сохранения данных в файл
M.save()