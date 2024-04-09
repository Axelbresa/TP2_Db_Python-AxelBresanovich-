import csv
import MySQLdb

def read_csv(csv_file):
    data = []
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def create_table():
    db = MySQLdb.connect("127.0.0.1", "root", "", "provincias")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS provincias (provincia VARCHAR(255), localidad VARCHAR(255))")
    db.close()

csv_file = 'localidades.csv'
data = read_csv(csv_file)
create_table()
