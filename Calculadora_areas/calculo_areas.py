# Calculadora de áreas
def area_cuadrado(lado):
    return lado * lado

def area_circulo(radio):
    from math import pi
    return pi * (radio ** 2)

def area_triangulo(base, altura):
    return (base * altura) / 2

def calculadora_areas():
    print("\n--- Calculadora de Áreas ---")
    print("1. Cuadrado\n2. Círculo\n3. Triángulo")
    opcion = input(" Elige una opción (1,2 o 3): ")
    if opcion == "1":
        lado = float(input("Ingrese el lado: "))
        print(f" Área del cuadrado: {area_cuadrado(lado)}")
    elif opcion == "2":
        radio = float(input("Ingrese el radio: "))
        print(f" Área del círculo: {area_circulo(radio):.2f}")
    elif opcion == "3":
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        print(f" Área del triángulo: {area_triangulo(base, altura)}")
    else:
        print("⚠️ Opción inválida.")

def menu():
    while True:
        print("\n===== Menu =====")
        print("1. Entrar a Calculadora de Áreas")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            calculadora_areas()
        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Por favor, intente de nuevo.")
        
if __name__ == "__main__":
    menu()