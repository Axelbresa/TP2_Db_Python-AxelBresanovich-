from read_csv import read_csv
from conexion_insercion import insert_data, crear_tabla
from localidades_por_provincia import exportar_localidades_por_provincia

# Eliminar y crear la tabla
crear_tabla()

# Nombre del archivo CSV
csv_file = 'localidades.csv'

# Leer el archivo CSV
data = read_csv(csv_file)

# Insertar los datos en la base de datos
insert_data(data)

#Exportar las localidades por provincia
exportar_localidades_por_provincia()