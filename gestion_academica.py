import hashlib

# Almacenamiento simulado (mejoraría con una base de datos)
usuarios = {}

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def mostrar_menu_principal():
    print("\n--- Sistema de Gestión Académica ---")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

def registrar_usuario():
    usuario = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()
    tipo = input("Tipo (E/P): ").strip().upper()

    if tipo not in ("E", "P"):
        print("Tipo inválido. Debe ser E (Estudiante) o P (Profesor).")
        return

    if usuario in usuarios:
        print("Error: Usuario ya existe.")
        return

    # Hash de contraseña
    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
    usuarios[usuario] = {"contraseña": hash_contraseña, "tipo": tipo}
    print("¡Registro exitoso!")

def iniciar_sesion():
    usuario = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()

    if usuario not in usuarios:
        print("Usuario no encontrado.")
        return

    hash_contraseña = hashlib.sha256(contraseña.encode()).hexdigest()
    if usuarios[usuario]["contraseña"] != hash_contraseña:
        print("Contraseña incorrecta.")
        return

    print(f"Bienvenido, {usuario}!")
    if usuarios[usuario]["tipo"] == "E":
        menu_estudiante(usuario)
    else:
        menu_profesor(usuario)

