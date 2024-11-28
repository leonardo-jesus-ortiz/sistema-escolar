from consultas import *
    
def eliminar_datos_alumno(eliminar_alumno):
    try:
        query = "DELETE FROM alumnos WHERE legajo = %s"
        params = (eliminar_alumno,)
        ejecutar_consulta(query, params)
        print(f"El alumno con legajo {eliminar_alumno} fue eliminado exitosamente.")
    except Exception as err:
        print(f"Error al eliminar los datos del alumno: {err}")

def eliminar_datos_profesor(eliminar_profesor):
    try:
        query = "DELETE FROM profesores WHERE idprofesor = %s"
        params = (eliminar_profesor,)
        ejecutar_consulta(query, params)
        print(f"El profesor con id {eliminar_profesor} fue eliminado exitosamente.")
    except Exception as err:
        print(f"Error al eliminar los datos del profesor: {err}")

def eliminar_datos_curso(eliminar_curso):
    try:
        query = "DELETE FROM curso WHERE idcurso = %s"
        params = (eliminar_curso,)
        ejecutar_consulta(query, params)
        print(f"El curso con id {eliminar_curso} fue eliminado exitosamente.")
    except Exception as err:
        print(f"Error al eliminar los datos del curso: {err}")