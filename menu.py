from consultas import *
from modificacion import *
from mostrar import *
from eliminar import *

print("¡Bienvenido al programa Sistema Escolar!")

while True:
    print("1: Ver datos")
    print("2: ingresar datos")
    print("3: Modificar datos")
    print("4: Eliminar datos")
    print("5: Salir del Programa")
    opcion = input("Selecciona la opción que te interese: ")
    if opcion == "1":
        print("""ingresando a la base de datos.., espere por favor""")
        mostrar = input("""Seleccione el usuario que desea ver:
                                1. Alumnos
                                2. Profesores
                                3. Cursos
                                4. ver alumnos y cursos
                                5. Volver
                                : """)
        if mostrar == "1":
            print("1. Alumnos: ")
            mostrar_alumnos(connection=conectar_bd())
        elif mostrar == "2":
            print("2. Profesores: ")
            mostrar_profesores(connection=conectar_bd())
        elif mostrar == "3":
            print("3. Cursos: ")
            mostrar_cursos(connection=conectar_bd())
        elif mostrar == "4":
            print("4. Alumnos y Cursos: ")
            ver = input("""Seleccione el alumno o curso que desea ver:
                        1. alumnos
                        2. cursos """)
            if ver == "1":
                ver_Alumno()
            elif ver == "2":
                ver_Curso()
            else:
                print("Seleccione un Numero del 1 al 2")
        elif mostrar == "5":
            print("5. Volver: ")
            while True:
                break
        else:
            print("Seleccione un Numero del 1 al 4")

    elif opcion == "2":
        print("ingrese los datos del usuario")
        usuario = input("""seleccione el usuario que desea ingresar: 
                                1 si es alumno
                                2 si es profesor
                                3 si es crear curso
                                4 si es id del alumno y id del curso
                                5 si desea volver
                                : """)
        if usuario == "1":
            print("1. ingrese los datos del alumno: ")
            ingresar_Alumno()
        elif usuario == "2":
            print("2. ingrese los datos del profesor: ")
            ingresar_profesor()
        elif usuario == "3":
            print("3. ingrese los datos del curso: ")
            crear_curso()
        elif usuario == "4":
            print("4. ingrese los datos del alumno y curso: ")
            poner_alumnos_curso()
        elif usuario == "5":
            print("5. Volver: ")
            while True:
                break
        else:
            print("Seleccione un Numero del 1 al 4")

    elif opcion == "3":
        print("Modifique los datos del usuario")
        modificar = input("""Seleccione el usuario que desea modificar:
                                1. Alumno
                                2. Profesor
                                3. Curso
                                4. Volver
                                : """)
        if modificar == "1":
            print("1. Modifique los datos del alumno: ")
            connection = conectar_bd()
            print("Lista de alumnos:")
            mostrar_alumnos(connection=connection)

            legajo_alumno = input("Ingrese el legajo del alumno a modificar: ")

            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM alumnos WHERE legajo = %s", (legajo_alumno,))
            existe = cursor.fetchone()[0]

            if existe:
                print(f"Modificando al alumno con legajo {legajo_alumno}...")
                modificar_datos_alumno(legajo_alumno)
            else:
                print(f"No existe un alumno con el legajo {legajo_alumno}.")
            cursor.close()

        elif modificar == "2":
            print("2. Modifique los datos del profesor: ")
            connection = conectar_bd()
            print("Lista de profesores:")
            mostrar_profesores(connection=connection)

            id_profesor = input("Ingrese el id del profesor a modificar: ")

            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM profesores WHERE idprofesor = %s", (id_profesor,))
            existe = cursor.fetchone()[0]

            if existe:
                print(f"Modificando al profesor con id {id_profesor}...")
                modificar_datos_profesor(id_profesor)
            else:
                print(f"No existe un profesor con id: {id_profesor}.")
            cursor.close()

        elif modificar == "3":
            print("3. Modifique los datos del curso: ")
            connection = conectar_bd()
            print("Lista de cursos:")
            mostrar_cursos(connection=connection)

            id_curso = input("Ingrese el id del curso a modificar: ")

            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM profesores WHERE idprofesor = %s", (id_curso,))
            existe = cursor.fetchone()[0]

            if existe:
                print(f"Modificando al profesor con id {id_curso}...")
                modificar_datos_profesor(id_curso)
            else:
                print(f"No existe un curso con id: {id_curso}.")
            cursor.close()

        elif modificar == "4":
            print("4. Volver: ")
            while True:
                break

        else:
            print("Seleccione un Numero del 1 al 4")

    elif opcion == "4":
        print("Eliminar usuario")
        eliminar = input("""Seleccione el usuario que desea eliminar:
                                1. Alumno
                                2. Profesor
                                3. Curso
                                4. Volver
                                : """)
        if eliminar == "1":
            connection = conectar_bd()
            print("Lista de alumnos:")
            mostrar_alumnos(connection=connection)

            eliminar_alumno = input("Ingrese el legajo del alumno a eliminar: ")

            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM alumnos WHERE legajo = %s", (eliminar_alumno,))
            existe = cursor.fetchone()[0]

            if existe:
                print(f"Eliminando al alumno con legajo {eliminar_alumno}...")
                eliminar_datos_alumno(eliminar_alumno)
            else:
                print(f"No existe un alumno con el legajo {eliminar_alumno}.")
            cursor.close()

        elif eliminar == "2":
            connection = conectar_bd()
            print("Lista de profesores:")
            mostrar_profesores(connection=connection)

            eliminar_profesor = input("Ingrese el id del profesor a eliminar: ")

            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM profesores WHERE idprofesor = %s", (eliminar_profesor,))
            existe = cursor.fetchone()[0]

            if existe:  
                print(f"Eliminando al profesor con id {eliminar_profesor}...")
                eliminar_datos_profesor(eliminar_profesor)
            else:
                print(f"No existe un profesor con id: {eliminar_profesor}.")
            cursor.close()

        elif eliminar == "3":
            connection = conectar_bd()
            print("Lista de cursos:")
            mostrar_cursos(connection=connection)

            eliminar_curso = input("Ingrese el id del curso a eliminar: ")

            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM cursos WHERE idcurso = %s", (eliminar_curso,))
            existe = cursor.fetchone()[0]

            if existe:
                print(f"Eliminando al curso con id {eliminar_curso}...")
                eliminar_datos_curso(eliminar_curso)
            else:
                print(f"No existe un curso con id: {eliminar_curso}.")
            cursor.close()

        elif eliminar == "4":
            print("4. Volver: ")
            while True:
                break

        else:
            print("Seleccione un Numero del 1 al 4")

    elif opcion == "5":
        print("saliendo del programa, gracias por usarlo")
        break

    else: 
        print("Seleccione un Numero del 1 al 5")
