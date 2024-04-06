# 2. Взяти csv файл, який додано до домашки і скопіювати тільки колонку email в інший csv файл
import csv

with open('names.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    with open('emails.csv', 'w', newline='') as csv_emails:
        writer = csv.writer(csv_emails)

        for line in reader:
            email = line[2]
            writer.writerow([email])
