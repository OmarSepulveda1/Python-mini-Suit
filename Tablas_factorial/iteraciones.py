def tablas_y_factorial():
    print("\n--- Tablas de Multiplicar y Factorial ---")
    opcion = input("1. Tabla de multiplicar\n2. Factorial\n ¿Que quieres hacer hoy?. Elige una opción: ")
    if opcion == "1":
        n = int(input("Ingrese un número: "))
        for i in range(1, 11):
            print(f"{n} x {i} = {n*i}")
    elif opcion == "2":
        n = int(input("Ingrese un número: "))
        factorial = 1
        contador = 1
        while contador <= n:
            factorial *= contador
            contador += 1
        print(f" El factorial de {n} es {factorial}")
    else:
        print("⚠️ Opción inválida.")

def menu():
    while True:
        print("\n===== Menu =====")
        print("1. Entrar a tablas y factorial")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            tablas_y_factorial()
        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
