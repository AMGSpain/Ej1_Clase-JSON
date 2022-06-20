import json

with open('profesoresJSON') as file:
    data = json.load(file) 
    
with open('estudiantesJSON') as file2:
    data2 = json.load(file2) 

def estudianteFunc():
    estudianteOpcion = int(input("¿Que deseas hacer? Pulsa: 1-Conocer Notas, 2-Cambiar Password, 3-Registrarse,  4-Salir : "))

    if estudianteOpcion == 1:
        conocerNotas()
    elif estudianteOpcion == 2:
        cambiarPasswordAlumno()
    elif estudianteOpcion == 3:
        estudianteRegistro()
    elif estudianteOpcion == 4:
        exit
    else:
        estudianteFunc()

def cambiarPasswordAlumno():
    emailInput = input("¿Cual es tu EMAIL?: ")
    passwordInput = input("¿Cual es tu PASSWORD?: ")
    
    for alumno in data2['alumnos']:
        email = alumno['email']
        password = alumno['password']
        nombre = alumno['nombre']
        
        while emailInput in email:
            if passwordInput == password:
                newPassword = input(f"{nombre} elige un NUEVO PASSWORD: ")
                password = newPassword
                
                with open("estudiantesJSON", "w") as file_write:
                    json.dump(data2, file_write)
        

def conocerNotas():
    emailInput = input("¿Cual es tu Email?: ")
    passwordInput = input("¿Cual es tu Password?: ")

    for alumno in data2['alumnos']:
        email = alumno['email']
        password = alumno['password']
        nombre = alumno['nombre']
        nota = alumno['nota']

        while emailInput in email:
            if passwordInput == password:
                print(f"Hola {nombre}, tu nota es de: {nota}")
                estudianteFunc()
                break
            else:
                print("Error en el PASSWORD")
                estudianteFunc()
                break
            
def estudianteRegistro():
    email = input("¿Cual es tu email? ")
    password = input("Elige un password: ")
    nombre = input("¿Cual es tu nombre? ")
    apellidos = input("¿Cuales son tus apellidos? ")
    nota = float(input("¿Que nota tienes? "))
    asignatura = input("¿Que asignatura tienes? ")
    
    data2['alumnos'].append({
            'email' : email,
            'password' : password,
            'nombre' : nombre,
            'apellidos' : apellidos,
            'nota' : nota,
            'asignatura' : asignatura
        })
    with open("estudiantesJSON", "w") as file_write:
        json.dump(data2, file_write)
        
    print(f"Bienvenido {nombre} {apellidos}, te has guardado con el email de {email} y eres profesor de la asignatura de {asignatura}")
        

def profesorLogin():

    profesor = input("¿Eres un PROFESOR NUEVO? ")
    
    if profesor.lower() == "si":
        email = input("¿Cual es tu email? ")
        password = input("Elige un password: ")
        nombre = input("¿Cual es tu nombre? ")
        apellidos = input("¿Cuales son tus apellidos? ")
        edad = int(input("¿Que edad tienes? "))
        asignatura = input("¿Que asignatura impartes? ")
        
        data['profesores'].append({
            'email' : email,
            'password' : password,
            'nombre' : nombre,
            'apellidos' : apellidos,
            'edad' : edad,
            'asignatura' : asignatura
        })
        
        with open("profesoresJSON", "w") as file_write:
            json.dump(data, file_write)
        
        print(f"Bienvenido {nombre} {apellidos}, te has guardado con el email de {email} y eres profesor de la asignatura de {asignatura}")
        
        
    else:
        emailInput = input("¿Cual es tu EMAIL?: ")
        passwordInput = input("¿Cual es tu PASSWORD?: ")
        
        for profesor in data['profesores']:
            email = profesor['email']
            password = profesor['password']
            nombre = profesor['nombre']
            
            while emailInput in email:
                print("Bienvenido",email)
                if passwordInput == password:
                    print("Hola",nombre)
                    break
                else:
                    print("Error en el password.")
                break

def profesorFunc():
    profesor = input("¿Eres PROFESOR?: ")

    if profesor.lower() == "si":
        profesorLogin()
    else:
        print("adios Alumno.")

estudiante = input("¿Eres ESTUDIANTE?: ")

if estudiante.lower() == "si":
    estudianteFunc()
else:
    profesorFunc()