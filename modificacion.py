from consultas import *

def modificar_datos_alumno(legajo_alumno):
    try:
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nuevo_apellido = input("Ingrese el nuevo apellido: ")
        nuevo_documento = validar_num("dni")
        nueva_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento (YYYY-MM-DD): ")
        nuevo_telefono = validar_num("telefono")
        nuevo_domicilio = pedir_domicilio()
        nuevo_correo = validar_correo("alumno")

        query = " UPDATE alumnos SET Nombre = %s, Apellido = %s, Documento = %s, Fecha_Nacimiento = %s, Telefono = %s, Domicilio = %s, Correo = %s WHERE legajo = %s "
        params = (nuevo_nombre, nuevo_apellido, nuevo_documento, nueva_fecha_nacimiento,nuevo_telefono, nuevo_domicilio, nuevo_correo, legajo_alumno)

        ejecutar_consulta(query, params)
        print(f"El alumno con legajo {legajo_alumno} fue modificado exitosamente.")
    
    except Exception as err:
        print(f"Error al modificar los datos del alumno: {err}")


def modificar_datos_profesor(id_profesor):
    try:
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nuevo_apellido = input("Ingrese el nuevo apellido: ")
        nuevo_documento = validar_num('dni')
        nueva_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento (YYYY-MM-DD): ")
        nuevo_telefono = validar_num('telefono')
        nuevo_domicilio = pedir_domicilio()
        nuevo_correo = validar_correo("profesor")

        query = "UPDATE profesores SET Nombre = %s, Apellido = %s, Documento = %s, Fecha_Nacimiento = %s, Telefono = %s, Domicilio = %s, Correo = %s WHERE idprofesor = %s"
        params = (nuevo_nombre, nuevo_apellido, nuevo_documento, nueva_fecha_nacimiento, nuevo_telefono, nuevo_domicilio, nuevo_correo, id_profesor)

        ejecutar_consulta(query, params)
        print(f"El profesor con id {id_profesor} fue modificado exitosamente.")
    
    except Exception as err:
        print(f"Error al modificar los datos del alumno: {err}")

def modificar_datos_curso(id_curso):
    try:
        nuevo_año = validacion_año("año")
        nuevo_turno = input("Ingrese el nuevo turno: ")
        nueva_materia = input("Ingrese la nueva materia: ")
        nuevo_profesor = input("Ingrese el nuevo profesor: ")

        query = "UPDATE curso SET Año = %s, Turno = %s, Materia = %s, Profesores_idprofesor = %s WHERE idcurso = %s"
        params = (nuevo_año, nuevo_turno, nueva_materia, nuevo_profesor, id_curso)

        ejecutar_consulta(query, params)
        print(f"El curso con id {id_curso} fue modificado exitosamente.")

    except Exception as err:
        print(f"Error al modificar los datos del curso: {err}")