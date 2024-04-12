import os
import csv
from conexion_insercion import conexion_db

def exportar_localidades_por_provincia():
    db=conexion_db()
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
    print("archivos csv exportados con exito un total de ", len(provincias), "provincias" )

    db.close()

exportar_localidades_por_provincia()
