import mariadb

def conexion_db():
    #conexion a mySql 
    # db = mariadb.connect("127.0.0.1", "root", "", "provincias")

    #conexion a mariaDb
    config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'provincias'
    }
    db = mariadb.connect(**config)
    return db

def crear_tabla():
    db=conexion_db()
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS provincias")  # Eliminar la tabla si existe
    cursor.execute("CREATE TABLE provincias (provincia VARCHAR(255), id INT,  localidad VARCHAR(255), cp VARCHAR(255), id_prov_mstr VARCHAR(255))")
    print("Se borro la tabla la tabla provincia y se volvio a crear la tabla")
    db.close()

def insert_data(data):
    db=conexion_db()
    cursor = db.cursor()
    try:
        sql = "INSERT INTO provincias (provincia, id, localidad, cp, id_prov_mstr) VALUES (%s, %s, %s, %s, %s)"
        val = [(row['provincia'], row['id'], row['localidad'], row['cp'], row['id_prov_mstr']) for row in data]
        cursor.executemany(sql, val)
        db.commit()
        print("Todos los registros insertados correctamente.")
    except mariadb.Error as e:
        print("Error al insertar los registros:", e)
        db.rollback()
    finally:
        db.close()

# crear_tabla()
# insert_data(data)
