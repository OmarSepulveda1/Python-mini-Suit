# conversor.py

def conversor():
    print("\n--- Conversor de Unidades ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Kilómetros a Millas")
    print("4. Millas a Kilómetros")

    opcion = input(" Selecciona una opción: ")

    if opcion == "1":
        celsius = float(input("Ingrese la temperatura en °C: "))
        print(f"{celsius}°C = {celsius * 9/5 + 32}°F")
    elif opcion == "2":
        fahrenheit = float(input("Ingrese la temperatura en °F: "))
        print(f"{fahrenheit}°F = {(fahrenheit - 32) * 5/9}°C")
    elif opcion == "3":
        km = float(input("Ingrese los kilómetros: "))
        print(f"{km} km = {km * 0.621371} millas")
    elif opcion == "4":
        millas = float(input("Ingrese las millas: "))
        print(f"{millas} millas = {millas / 0.621371} km")
    else:
        print("⚠️ Opción inválida.")


def menu():
    while True:
        print("\n===== Menu =====")
        print("1. Entrar a Conversor de Unidades")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            conversor()
        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
