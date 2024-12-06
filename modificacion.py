from consultas import *

#funcion mofificar alumnos
def modificar_datos_alumno(legajo_alumno):
    try:
        nuevo_nombre = ingresar_nombre()
        nuevo_apellido = ingresar_apellido()
        nuevo_documento = validar_num("dni")
        nueva_fecha_nacimiento = solicitar_fecha_nacimiento()
        nuevo_telefono = validar_num("telefono")
        nuevo_domicilio = pedir_domicilio()
        nuevo_correo = validar_correo("alumno")
        #actualizar la base de datos con los nuevos datos
        query = " UPDATE alumnos SET Nombre = %s, Apellido = %s, Documento = %s, Fecha_Nacimiento = %s, Telefono = %s, Domicilio = %s, Correo = %s WHERE legajo = %s "
        params = (nuevo_nombre, nuevo_apellido, nuevo_documento, nueva_fecha_nacimiento,nuevo_telefono, nuevo_domicilio, nuevo_correo, legajo_alumno)
         #ejecuta la consulta
        ejecutar_consulta(query, params)
        print(f"El alumno con legajo {legajo_alumno} fue modificado exitosamente.")
    #si hay un error aparecera este msj
    except Exception as err:
        print(f"Error al modificar los datos del alumno: {err}")

#funcion modificar profesores
def modificar_datos_profesor(id_profesor):
    try:
        nuevo_nombre = ingresar_nombre()
        nuevo_apellido = ingresar_apellido()
        nuevo_documento = validar_num('dni')
        nueva_fecha_nacimiento = solicitar_fecha_nacimiento()
        nuevo_telefono = validar_num('telefono')
        nuevo_domicilio = pedir_domicilio()
        nuevo_correo = validar_correo("profesor")
        #actualizar la base de datos con los nuevos datos
        query = "UPDATE profesores SET Nombre = %s, Apellido = %s, Documento = %s, Fecha_Nacimiento = %s, Telefono = %s, Domicilio = %s, Correo = %s WHERE idprofesor = %s"
        params = (nuevo_nombre, nuevo_apellido, nuevo_documento, nueva_fecha_nacimiento, nuevo_telefono, nuevo_domicilio, nuevo_correo, id_profesor)
        #ejecuta la consulta
        ejecutar_consulta(query, params)
        print(f"El profesor con id {id_profesor} fue modificado exitosamente.")
    #si hay un error aparecera este msj
    except Exception as err:
        print(f"Error al modificar los datos del alumno: {err}")

#funcion modificar cursos
def modificar_datos_curso(id_curso):
    try:
        nuevo_año = validacion_año("año")
        nuevo_turno = turno()
        nueva_materia = input("Ingrese la nueva materia: ")
        nuevo_profesor_idprofesor = int(input("Ingrese el nuevo profesor: "))
        #actualizar la base de datos con los nuevos datos
        query = "UPDATE curso SET Año = %s, Turno = %s, Materia = %s, Profesores_idprofesor = %s WHERE idcurso = %s"
        params = (nuevo_año, nuevo_turno, nueva_materia, nuevo_profesor_idprofesor, id_curso)
        #ejecuta la consulta
        ejecutar_consulta(query, params)
        print(f"El curso con id {id_curso} fue modificado exitosamente.")
    #si hay un error aparecera este msj
    except Exception as err:
        print(f"Error al modificar los datos del curso: {err}")