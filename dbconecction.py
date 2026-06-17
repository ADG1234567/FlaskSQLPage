## Conexion a sql desde python, con mysql.connector, para hacer consultas, insertar o borrar registros de la tabla clientes
import mysql.connector

conexion = mysql.connector.connect(
    user= "root", 
    password="", 
    host="localhost", 
    database="herbolariataller",
    port="3306"
    )

miCursor = conexion.cursor()

miCursor.execute("SHOW DATABASES")
consulta = miCursor.fetchall()
print(consulta)
## Código

print("USTED AHORA PUEDE HACER CONSULTAS, INSERTAR O BORRAR REGISTROS DE LA TABLA CLIENTES")

while True:
    entrada = input("Ingrese que quiere hacer: [añadir, borrar, consultar]: ")
    if entrada == "":
        break

    if entrada.find("consultar") > -1:
        miCursor.execute("SELECT * FROM clientes;")
        consulta = miCursor.fetchall()
        for i in range(len(consulta)):
            print(consulta[i])

    if entrada.find("añadir") > -1:
        id = input("Ingrese el id: ")
        nombre = input("Ingrese el nombre: ")
        aps = input("Ingrese los apellidos: ")
        codpos = input("Ingrese el codigo postal: ")
        miCursor.execute(f"INSERT INTO clientes VALUES('{id}','{nombre}','{aps}',{codpos});")
        print("Insertado correcto c:")
    
    def borrapo(campo):
        condicion = input("Bajo que condicion borrar: [= {registro}, <,> {valor}]: ")
        try:
            miCursor.execute(f"DELETE FROM clientes WHERE {campo} {condicion};")
        except mysql.connector.errors.ProgrammingError:
            print("Borrado correcto c:")
    if entrada.find("borrar") > -1:
        campoborra = input("Ingrese el campo de su condicion: [id, nombre, apellidos, codigo postal]")
        if campoborra.find("id"):
            borrapo("id_cliente")
        elif campoborra.find("nombre"):
            borrapo("nombre")
        elif campoborra.find("apellidos"):
            borrapo("apellidos")
        elif campoborra.find("codigo postal"):
            borrapo("codpos")