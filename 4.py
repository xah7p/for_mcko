import csv

'''
функция make_promo реализует создание промокода для продукта
ей на вход подаётся список с информацией о продукте в виде: [Category;product;Date;Price per unit;Count]
функция формирует промокод по следующей формуле:
    первые 2-ух букв названия + 
    день поступления + 
    2 предпоследние буквы названия в обратном порядке + 
    месяц поступления в обратном порядке.
'''


def make_promo(row):
    _, name, date, _, _ = row
    promo = (name[:2] + date[:2] + name[-2:][::-1] + date[3:5][::-1]).upper()
    return promo


with open("products.csv", encoding='utf-8') as in_file:
    reader = csv.reader(in_file, delimiter=";")
    with open("product_promo.csv", 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file, delimiter=";")
        answer = []  # список, в который будут сохранятся обновлённые строки
        for row in reader:
            if row[0] != "Category":
                row.append(make_promo(row))
            else:
                # если это первая строка, то вместо промокода
                # добавляем название столбца: "promocode"
                row.append("promocode")
            answer.append(row)
        writer.writerows(answer)  # записываем в csv файл



