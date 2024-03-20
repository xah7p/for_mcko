import csv


def make_promo(row):
    _, name, date, _, _ = row
    promo = (name[:2] + date[:2] + name[-2:][::-1] + date[3:5][::-1]).upper()
    return promo


with open("products.csv", encoding='utf-8') as in_file:
    reader = csv.reader(in_file, delimiter=";")
    with open("product_promo.csv", 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file, delimiter=";")
        answer = []
        for row in reader:
            if row[0] != "Category":
                row.append(make_promo(row))
            else:
                row.append("promocode")
            answer.append(row)
        writer.writerows(answer)



