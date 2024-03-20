import csv

with open("products.csv", encoding='utf-8') as in_file:
    reader = csv.reader(in_file, delimiter=";")
    data = []  # массив, в котором будет хранится информация о каждом продукте
    for row in reader:
        if row[0] != "Category":
           data.append(row)  # заполняем массив информацией о продуктах

    data.sort(key=lambda x: x[-1], reverse=1)  # сортируем его по количеству проданных штук в обратном порядке

    # далее формируем хэш-массив, в котором останутся категория
    # и минимальное количество проданных штук в ней
    hash = {x[0]:float(x[-1]) for x in data}

    # превращаем его в список, чтобы далее отсортировать по количеству проданных
    hash = list({key:value for key, value in hash.items()}.items())
    hash.sort(key=lambda x: x[1])

    # превращаем его обратно в хэш-массив, но берем только первые 10 элементов
    hash = {key:value for key, value in hash[:10]}
    for key, value in hash.items():
        print(key, value)




