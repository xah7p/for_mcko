import csv

with open("products.csv", encoding='utf-8') as in_file:
    reader = csv.reader(in_file, delimiter=";")
    data = []
    for row in reader:
        if row[0] != "Category":
            data.append(row)  # заполняем пустой список data строками с данными о продуктах
    data.sort(key=lambda x: (x[0], x[3]))  # сортируем по категории товара и цене за единицу товара
    first = [i for i in data if i[0] == data[0][0]]  # создаем список товаров из первой категории
    print(f"В категории: {data[0][0]} самый дорогой товар: {first[-1][1]} "
          f"его цена за единицу товара составляет {first[-1][3]}")