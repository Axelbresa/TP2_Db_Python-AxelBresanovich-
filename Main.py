from read_csv import read_csv
from conexion_insercion import insert_data

# Nombre del archivo CSV
csv_file = 'localidades.csv'

# Leer el archivo CSV
data = read_csv(csv_file)

# Insertar los datos en la base de datos
insert_data(data)
