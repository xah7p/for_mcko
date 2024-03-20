import csv

summ = 0
with open("products.csv", encoding='utf-8') as in_file:
    reader = csv.reader(in_file, delimiter=";")
    with open("products_new.csv", 'w', encoding='utf-8', newline='') as out_file:
        writer = csv.writer(out_file, delimiter=";")
        for row in reader:
            print(row)
            if row[0] != "Category":
                row.append(float(row[3]) * float(row[4]))
                if row[0] == "Закуски":
                    summ += row[-1]
            else:
                row.append("total")
            writer.writerow(row)
print(summ)