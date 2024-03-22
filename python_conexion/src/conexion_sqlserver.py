import pyodbc

try:
    # pydoc modulo para conectar con base de datos
    # pide el driver, servidor de conexion, nombre de la bd, usuario y contraseña
    connection=pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=test;UID=sa;PWD=Quesolulu12')
    print("Conexion exitosa")
    cursor = connection.cursor()
    cursor.execute('SELECT @@version')
    row = cursor.fetchone()
    print(row)
    
    cursor.execute('SELECT Top(10) * FROM cat_asentamientos')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)