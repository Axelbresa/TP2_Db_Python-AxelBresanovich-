import os
import MySQLdb
import csv

def exportar_localidades_por_provincia():
    db = MySQLdb.connect("127.0.0.1", "root", "", "provincias")
    cursor = db.cursor()

    # Crear la carpeta si no existe
    carpeta_salida = 'csvProvincias'
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Obtener las provincias disponibles
    cursor.execute("SELECT DISTINCT provincia FROM provincias")
    provincias = cursor.fetchall()

    for provincia in provincias:
        provincia_nombre = provincia[0]
        
        # Obtener las localidades de la provincia actual
        cursor.execute("SELECT localidad FROM provincias WHERE provincia=%s", (provincia_nombre,))
        localidades = cursor.fetchall()

        # Exportar las localidades en un archivo CSV separado por provincia
        csv_file = os.path.join(carpeta_salida, f'{provincia_nombre}.csv')
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Localidad'])
            for localidad in localidades:
                writer.writerow(localidad)
        print(f'Archivo CSV "{csv_file}" exportado correctamente para la provincia de {provincia_nombre}')

    db.close()

# exportar_localidades_por_provincia()
