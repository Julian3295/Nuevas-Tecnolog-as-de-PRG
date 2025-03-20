import hashlib


usuarios = {}
notas_estudiantes = {}

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    tipo = input("¿Es estudiante o profesor? (E/P): ").upper()
    if tipo not in ['E', 'P']:
        print("Tipo no válido. Debe ser 'E' o 'P'.")
        return
    contraseña = input("Ingrese su contraseña: ")
    usuarios[nombre] = {'tipo': tipo, 'contraseña': contraseña}
    print(f"Usuario {nombre} registrado exitosamente.")

def iniciar_sesion():
    nombre = input("Ingrese su nombre: ")
    contraseña = input("Ingrese su contraseña: ")
    if nombre in usuarios and usuarios[nombre]['contraseña'] == contraseña:
        print(f"Bienvenido, {nombre}.")
        return nombre
    else:
        print("Credenciales incorrectas.")
        return None
    
def iniciar_sesion():
    intentos = 3
    while intentos > 0:
        nombre = input("Ingrese su nombre: ")
        contraseña = input("Ingrese su contraseña: ")
        hashed_password = hashlib.sha256(contraseña.encode()).hexdigest()
        if nombre in usuarios and usuarios[nombre]['contraseña'] == hashed_password:
            print(f"Bienvenido, {nombre}.")
            return nombre
        else:
            intentos -= 1
            print(f"Credenciales incorrectas. Te quedan {intentos} intentos.")
    print("Has excedido el número máximo de intentos.")
    return None

def menu_estudiante(nombre):
    while True:
        print("\n--- Menú Estudiante ---")
        print("1. Consultar notas")
        print("2. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            if nombre in notas_estudiantes:
                print(f"Tus notas son: {notas_estudiantes[nombre]}")
                promedio = sum(notas_estudiantes[nombre]) / len(notas_estudiantes[nombre])
                print(f"Tu promedio es: {promedio:.2f}")
            else:
                print("Aún no tienes notas registradas.")
        elif opcion == "2":
            break
        else:
            print("Opción no válida.")

def menu_profesor():
    while True:
        print("\n--- Menú Profesor ---")
        print("1. Agregar notas")
        print("2. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            estudiante = input("Nombre del estudiante: ")
            if estudiante not in notas_estudiantes:
                notas_estudiantes[estudiante] = []
            nota = float(input("Ingrese la nota: "))
            notas_estudiantes[estudiante].append(nota)
            print(f"Nota agregada para {estudiante}.")
        elif opcion == "2":
            break
        else:
            print("Opción no válida.")

def main():
    while True:
        print("\n--- Sistema de Gestión Académica ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            usuario = iniciar_sesion()
            if usuario:
                if usuarios[usuario]['tipo'] == 'E':
                    menu_estudiante(usuario)
                elif usuarios[usuario]['tipo'] == 'P':
                    menu_profesor()
        elif opcion == "3":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()