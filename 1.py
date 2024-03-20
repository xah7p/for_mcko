import csv

summ = 0  # переменная, в которой будет лежать итоговая выручка
with open("products.csv", encoding='utf-8') as in_file:
    reader = csv.reader(in_file, delimiter=";")
    with open("products_new.csv", 'w', encoding='utf-8', newline='') as out_file:
        writer = csv.writer(out_file, delimiter=";")
        for row in reader:
            print(row)
            if row[0] != "Category":  # если строка не несёт информацию о столбцах в общем(не является первой)
                row.append(float(row[3]) * float(row[4]))  # считаем выручку за продукт
                if row[0] == "Закуски":
                    summ += row[-1]
            else:
                row.append("total")
            writer.writerow(row)  # в отдельный файл сохраняем построчно новые строки
print(summ)