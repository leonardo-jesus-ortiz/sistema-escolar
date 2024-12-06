import mysql.connector
from consultas import *

#funcion mostrar alumnos
def mostrar_alumnos(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT Legajo, Nombre, Apellido, Documento, Fecha_Nacimiento, Telefono, Domicilio, Correo FROM alumnos"
        cursor.execute(query)
        alumnos = cursor.fetchall() 
        print("Alumnos registrados:")

        for alumno in alumnos:
                print("="*45)
                print(f"Legajo: {alumno[0]}, Nombre: {alumno[1]}, Apellido: {alumno[2]}\n Documento: {alumno[3]}, Fecha de Nacimiento: {alumno[4]}, Telefono: {alumno[5]}\n Domicilio: {alumno[6]}, Correo: {alumno[7]}")
                print("="*45)
        return alumnos
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()

#funcion ver alumno
def ver_Alumno():
    try:
        mostrar_opciones("alumno")
        Legajo = input("Ingrese el Legajo del alumno: ")
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = f"""SELECT Legajo, Nombre, Apellido, idCurso, Materia
                    FROM alumnos
                    INNER JOIN alumnos_has_curso
                    ON alumnos.Legajo = alumnos_has_curso.Alumnos_Legajo
                    INNER JOIN curso
                    ON curso.idCurso = alumnos_has_curso.Curso_idCurso
                    WHERE Legajo = {Legajo}"""
        cursor.execute(query)
        tabla = cursor.fetchall()
        print("="*30,"\n")
        print(f"Legajo:{tabla[0][0]}")
        print(f"El alumno {tabla[0][1]}, {tabla[0][2]}. Esta registrado en las materias. \n")
        print("="*30)
        for txt in tabla:
            print(f"{txt[4]} ID: {txt[3]}")
            print("="*30)
        return tabla
    except mysql.connector.Error as err:
        print(f"error: {err}")
    finally:
        cursor.close()
        conexion.close()

#funcion mostrar profesores
def mostrar_profesores(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT idprofesor, Nombre, Apellido, Documento, Fecha_Nacimiento, Telefono, Domicilio, Correo FROM profesores"
        cursor.execute(query)
        profesores = cursor.fetchall()
        print("Profesores registrados:")

        for profesor in profesores:
                print("="*45)
                print(f"idprofesor: {profesor[0]}, Nombre: {profesor[1]}, Apellido: {profesor[2]}\n Documento: {profesor[3]}, Fecha de Nacimiento: {profesor[4]}, Telefono: {profesor[5]}\n Domicilio: {profesor[6]}, Correo: {profesor[7]}")
                print("="*45)
        return profesores
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()

#funcion mostrar curso
def mostrar_cursos(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT idCurso, Año, Turno, Materia, Profesores_idprofesor FROM curso"
        cursor.execute(query)
        cursos = cursor.fetchall()
        print("Cursos registrados:")

        for curso in cursos:
            print("="*45)
            print(f"idCurso: {curso[0]}, Año: {curso[1]}, Turno: {curso[2]}, Materia: {curso[3]}, Profesores_idprofesor: {curso[4]}")
            print("="*45)
        return cursos
    
    except mysql.connector.Error as err:
         print(f"Error: {err}")

    finally:
        cursor.close()
        
#funcion ver curso
def ver_Curso():
    try:
        mostrar_opciones("curso")
        idCurso = input("Ingrese el id del curso: ")
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = f"""SELECT Legajo, Nombre, Apellido, idCurso, Materia
                    FROM alumnos
                    INNER JOIN alumnos_has_curso
                    ON alumnos.Legajo = alumnos_has_curso.Alumnos_Legajo
                    INNER JOIN curso
                    ON curso.idCurso = alumnos_has_curso.Curso_idCurso
                    WHERE idCurso = {idCurso}"""
        cursor.execute(query)
        tabla = cursor.fetchall()
        print("="*30,"\n")
        print(f"Alumnos Registrados en {tabla[0][4]} \n")
        print("="*30)
        for txt in tabla:
            print(f"{txt[1]}, {txt[2]}   Legajo:{txt[0]}")
            print("="*30)
        return tabla
    except mysql.connector.Error as err:
        print(f"error: {err}")
    finally:
        cursor.close()
        conexion.close()