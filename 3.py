import csv

with open("products.csv", encoding='utf-8') as in_file:
    reader = csv.reader(in_file, delimiter=";")
    data = dict()  # словарь, в котором будут хранится все товары по категориям
    for row in reader:
        if row[0] != "Category":
            # добавляем в название категории строку с информацией
            # о продукте, начиная с названия о продукте
            data[row[0]] = data.get(row[0], []) + [row[1:]]
    while 1:
        request = input()  # запрашиваем у пользователя название категории
        if request == "молоко":
            break
        if request in data:
            q = data[request]  # все товары данной категории
            q.sort(key=lambda x: x[-1])
            print(f"В категории: {request} товар: {q[0][0]} был куплен {q[0][-1]} раз")
        else:
            print("Такой категории не существует в нашей БД")
