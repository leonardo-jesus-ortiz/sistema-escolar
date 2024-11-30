import mysql.connector
import re


def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="sistema_escolar_bd"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

def ejecutar_consulta(query, params):
    conexion = conectar_bd()
    if conexion:
        try:
            cur = conexion.cursor()
            cur.execute(query, params)
            conexion.commit()
            print(f"Consulta ejecutada exitosamente: {cur.rowcount} filas afectadas.")
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
        finally:
            cur.close()
            conexion.close()
    else:
        print("No se pudo establecer la conexión.")

def mostrar_opciones(opcion):

    if opcion == "profesor":
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "SELECT idprofesor, Nombre, Apellido, Documento FROM profesores"
        cursor.execute(query)
        tabla = cursor.fetchall()
        print("="*30,"\n")
        print("Profesores registrados: \n")
        print("="*30)
        for txt in tabla:
                print(f"{txt[2]}, {txt[1]}")
                print(f"   ID: {txt[0]}\n   Documento: {txt[3]}")
                print("="*30)
        return tabla
    elif opcion == "alumno":
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "SELECT Legajo, Nombre, Apellido, Documento FROM alumnos"
        cursor.execute(query)
        tabla = cursor.fetchall()
        print("="*30,"\n")
        print("Alumnos registrados:")
        print("="*30)
        for txt in tabla:
                print(f"Legajo: {txt[0]}\n Nombre: {txt[1]}\n Apellido: {txt[2]}\n Documento: {txt[3]}")
                print("="*30)
        return tabla
    elif opcion == "curso":
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = """SELECT idCurso, año, Turno, Materia, profesores_idProfesor, profesores.Nombre, profesores.Apellido FROM curso
                    INNER JOIN Profesores
                    ON Profesores.idProfesor = Curso.Profesores_idProfesor
                    """
        cursor.execute(query)
        tabla = cursor.fetchall()
        print("="*30,"\n")
        print("            Materias: \n")
        print("="*30)
        for txt in tabla:
                print(f"   Profesor:{txt[5]}, {txt[6]}\n   ID:{txt[0]}\n   Materia:{txt[3]}\n   Turno:{txt[2]}")
                print("="*30)
        return tabla
    
def ingresar_nombre():
    while True:
        nombre = input("Ingresa tu nombre: ").strip()
        if len(re.findall(r'\b\w+\b', nombre)) <= 3 and len(nombre.replace(" ", "")) >= 3:
            print(f"Nombre ingresado correctamente: {nombre}")
            return nombre
        print("El nombre no es correcto. Inténtalo de nuevo.")

def ingresar_apellido():
    while True:
        apellido = input("Ingresa tu apellido: ").strip()
        if len(re.findall(r'\b\w+\b', apellido)) <= 2 and len(apellido.replace(" ", "")) >= 3:
            print(f"Apellido ingresado correctamente: {apellido}")
            return apellido
        print("El apellido no es correcto. Inténtalo de nuevo.")


    
def validar_num(opcion):
    num = input(f"ingrese el numero de {opcion}: ")
    if opcion == "dni":
        if len(num) == 8:
            print("DNI valido")
            return num
        else:
            print("DNI invalido")
    elif opcion == "telefono":
        if len(num) == 10:
            print("Telefono valido")
            return num
        else:
            print("Telefono invalido")
    elif opcion == "legajo":
        if len(num) == 6:
            print("Legajo valido")
            return num
        else:
            print("Legajo invalido")

def pedir_domicilio():
    while True:
        domicilio = input("Ingresa tu domicilio: ")
        if re.fullmatch(r"(\b\w+\b\s?){1,3}\d{4}$", domicilio.strip()):
            print("Domicilio válido:", domicilio)
            return domicilio
        else:
            print("Dirección no válida. Intenta de nuevo.")

def validar_correo(nombre):
    patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    correo = input(f"Ingrese correo electronico del {nombre}: ")
    if re.match(patron, correo):
        print("correo valido")
        return correo
    else:
        print("correo invalido")



def validacion_año(año):
    limite_inferior = 1
    limite_superior = 6
    while True:
        try:
            año = int(input(f"Ingrese un año entre {limite_inferior} y {limite_superior}: "))
            
            if limite_inferior <= año <= limite_superior:
                print(f"¡Año válido! Ingresaste: {año}")
                return año
            else:
                print("El Año está fuera de los límites. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def turno():
    while True:
        turnos_validos = ["mañana", "tarde", "noche"]
        turno = input("Ingrese un turno (mañana, tarde, noche): ").strip().lower()
        if turno in turnos_validos:
            print(f"Turno Elegido: {turno.capitalize()}")
            return turno
        else:
            print("Turno incorrecto. Por favor, ingrese un turno que esté en la lista.")


def ingresar_Alumno():
    try:
        legajo = validar_num('legajo')
        nombre = ingresar_nombre()
        apellido = ingresar_apellido()
        documento = validar_num('dni')
        fecha = input("ingrese su fecha de nacimiento (YYYY-MM-DD): ")
        telefono = validar_num('telefono')
        domicilio = pedir_domicilio()
        correo = validar_correo("alumno")
    except:
        print("Datos ingresados erroneamente")
    else:
        query = """
                INSERT INTO Alumnos (Legajo, Nombre, Apellido, Documento, Fecha_Nacimiento, Telefono, Domicilio, Correo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
        params = (legajo, nombre, apellido, documento, fecha, telefono, domicilio, correo)
        ejecutar_consulta(query, params)


def ingresar_profesor():
    try:
        nombre = ingresar_nombre()
        apellido = ingresar_apellido()
        documento = validar_num('dni')
        fecha = input("ingrese su fecha de nacimiento (YYYY-MM-DD): ")
        telefono = validar_num('telefono')
        domicilio = pedir_domicilio()
        correo = validar_correo("profesor")
    except:
        print("Datos ingresados erroneamente")
    else:
            
        query = """
                INSERT INTO profesores (Nombre, Apellido, Documento, Fecha_Nacimiento, Telefono, Domicilio, Correo)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """

        params = (nombre, apellido, documento, fecha, telefono, domicilio, correo)
        ejecutar_consulta(query, params)

            
def crear_curso():
    try:
        materia = input("Ingrese el nombre de la materia: ")
        año_actual = validacion_año("año")
        Turno = turno()
        mostrar_opciones('profesor')
        profesor_idprofesor = int(input("ingrese el id del profesor que dara la materia: "))
    except:
        print("Datos ingresados erroneamente")
    else:
        query = """
                INSERT INTO curso (Año, Turno, Materia, Profesores_idprofesor)
                VALUES (%s, %s, %s, %s)
                """

        params = (año_actual, Turno, materia, profesor_idprofesor)
        ejecutar_consulta(query, params)

def poner_alumnos_curso():
    mostrar_opciones("alumno")
    try:
        alumno_legajo = input("ingrese el legajo del alumno: ")
        curso_idcurso = input("ingrese el id del curso: ")
    except:
        print("Datos ingresados erroneamente")
    else:
        query = """
                INSERT INTO alumnos_has_curso (Alumnos_Legajo, Curso_idcurso)
                VALUES (%s, %s)
                """

        params = (alumno_legajo, curso_idcurso)
        ejecutar_consulta(query, params)
