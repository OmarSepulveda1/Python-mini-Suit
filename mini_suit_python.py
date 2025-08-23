import csv
import os

# ===============================
# MINI SUITE PYTHON
# ===============================


# Conversor de unidades de temperatura
def conversor_temperatura():
    print("\n--- Conversor de Temperatura ---")
    opcion = input("1. Celsius a Fahrenheit\n2. Fahrenheit a Celsius\n👉 Elige una opción: ")
    if opcion == "1":
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"🌡 {celsius} °C = {fahrenheit:.2f} °F")
    elif opcion == "2":
        fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"🌡 {fahrenheit} °F = {celsius:.2f} °C")
    else:
        print("⚠️ Opción inválida.")


# Formulario en consola 
def formulario_usuario():
    print("\n--- Formulario de Usuario ---")
    nombre = input("Nombre: ")  # string
    edad = int(input("Edad: "))  # int
    altura = float(input("Altura en metros: "))  # float
    estudiante = input("¿Eres estudiante? (s/n): ").lower() == "s"  # bool

    print("\n✅ Datos registrados:")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Altura: {altura} m")
    print(f"Estudiante: {'Sí' if estudiante else 'No'}")


# Uso de condicionales 
def verificar_numero():
    print("\n--- Verificar Número ---")
    num = float(input("Ingrese un número: "))
    if num > 0:
        print("🔵 El número es positivo.")
    elif num < 0:
        print("🔴 El número es negativo.")
    else:
        print("⚪ El número es cero.")


# Uso de iteraciones 
def tablas_y_factorial():
    print("\n--- Tablas de Multiplicar y Factorial ---")
    opcion = input("1. Tabla de multiplicar\n2. Factorial\n👉 Elige una opción: ")
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


ARCHIVO_CONTACTOS = "agenda.csv"

# Función para cargar contactos desde el archivo CSV
def cargar_contactos():
    contactos = {}
    if os.path.exists(ARCHIVO_CONTACTOS):
        with open(ARCHIVO_CONTACTOS, "r", newline="", encoding="utf-8") as f:
            lector = csv.reader(f)
            for fila in lector:
                if len(fila) == 2:  # Asegurarse de que tenga Nombre y Teléfono
                    nombre, telefono = fila
                    contactos[nombre] = telefono
    return contactos

# Función para guardar contactos en el archivo CSV
def guardar_contactos(contactos):
    with open(ARCHIVO_CONTACTOS, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        for nombre, telefono in contactos.items():
            escritor.writerow([nombre, telefono])

# Agenda con persistencia en CSV
def agenda_contactos():
    print("\n--- Agenda de Contactos ---")

    contactos = cargar_contactos()

    while True:
        print("\n1. Ver contactos\n2. Agregar contacto\n3. Buscar contacto\n4. Eliminar contacto\n5. Salir")
        opcion = input("👉 Seleccione una opción: ")

        if opcion == "1":
            if contactos:
                print("\n Lista de contactos:")
                for nombre, telefono in contactos.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("⚠️ No hay contactos guardados.")

        elif opcion == "2":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            contactos[nombre] = telefono
            guardar_contactos(contactos)
            print("✅ Contacto agregado y guardado.")

        elif opcion == "3":
            nombre = input("Ingrese el nombre a buscar: ")
            if nombre in contactos:
                print(f" {nombre}: {contactos[nombre]}")
            else:
                print("⚠️ Contacto no encontrado.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            if nombre in contactos:
                del contactos[nombre]
                guardar_contactos(contactos)
                print("🗑 Contacto eliminado y cambios guardados.")
            else:
                print("⚠️ Contacto no encontrado.")

        elif opcion == "5":
            print("👋 Volviendo al menú principal...")
            break

        else:
            print("⚠️ Opción inválida.")


# Cálculo de áreas
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
    opcion = input("👉 Elige una figura: ")
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


# ---- MENÚ PRINCIPAL ----
def menu():
    while True:
        print("\n===== 🐍 MINI SUITE PYTHON =====")
        print("1. Conversor de temperatura")
        print("2. Formulario de usuario")
        print("3. Verificar número (+/-/0)")
        print("4. Tablas de multiplicar y factorial")
        print("5. Agenda de contactos")
        print("6. Calculadora de áreas")
        print("7. Salir")

        opcion = input("👉 Seleccione una opción: ")

        if opcion == "1":
            conversor_temperatura()
        elif opcion == "2":
            formulario_usuario()
        elif opcion == "3":
            verificar_numero()
        elif opcion == "4":
            tablas_y_factorial()
        elif opcion == "5":
            agenda_contactos()
        elif opcion == "6":
            calculadora_areas()
        elif opcion == "7":
            print("👋 Gracias por usar la Mini Suite Python.")
            break
        else:
            print("⚠️ Opción inválida.")


# ---- EJECUCIÓN ----
if __name__ == "__main__":
    menu()
