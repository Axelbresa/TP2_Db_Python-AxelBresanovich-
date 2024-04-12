import csv

def read_csv(csv_file):
    data = []
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

csv_file = 'localidades.csv'
data = read_csv(csv_file)
# print(data)
