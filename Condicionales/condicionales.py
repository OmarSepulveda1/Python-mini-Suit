# clasificador.py

def clasificador():
    print("\n--- Clasificador de Números ---")
    numero = float(input("Ingrese un número: "))

    if numero > 0:
        print("El número es positivo ✅")
    elif numero < 0:
        print("El número es negativo 🔻")
    else:
        print("El número es cero ⚖️")

def menu():
    while True:
        print("\n===== Menu =====")
        print("1. Entrar a Clasificador de Números")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            clasificador()
        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Por favor, intente de nuevo.")

        
if __name__ == "__main__":
    menu()

