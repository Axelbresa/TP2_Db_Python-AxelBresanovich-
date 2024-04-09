import MySQLdb

def crear_tabla():
    db = MySQLdb.connect("127.0.0.1", "root", "", "provincias")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS provincias")  # Eliminar la tabla si existe
    cursor.execute("CREATE TABLE provincias (provincia VARCHAR(255), localidad VARCHAR(255))")
    db.close()

def insert_data(data):
    db = MySQLdb.connect("127.0.0.1", "root", "", "provincias")
    cursor = db.cursor()
    for row in data:
        sql = "INSERT INTO provincias (provincia, localidad) VALUES (%s, %s)"
        val = (row['provincia'], row['localidad'])
        try:
            cursor.execute(sql, val)
            db.commit()
            print("Registro insertado correctamente.")
        except MySQLdb.Error as e:
            print("Error al insertar el registro:", e)
            db.rollback()
    db.close()

# insert_data(data)
