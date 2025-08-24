# formulario.py

def formulario():
    print("\n--- Formulario en Consola ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    altura = float(input("Altura (en metros): "))
    estudiante = input("¿Eres estudiante? (sí/no): ").lower() == "sí"

    print("\n✅ Información ingresada:")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Altura: {altura} m")
    print(f"Estudiante: {'Sí' if estudiante else 'No'}")

def menu():
    while True:
        print("\n===== Menu =====")
        print("1. Entrar al formulario")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            formulario()
        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
