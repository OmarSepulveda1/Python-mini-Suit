import csv
import os

ARCHIVO_CONTACTOS = "agenda.csv"

# Función para cargar contactos desde el archivo CSV
def cargar_contactos():
    contactos = {}
    if os.path.exists(ARCHIVO_CONTACTOS):
        with open(ARCHIVO_CONTACTOS, "r", newline="", encoding="utf-8") as f:
            lector = csv.reader(f)
            for fila in lector:
                if len(fila) == 2:  
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
        opcion = input(" Seleccione una opción: ")

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
                print(" Contacto eliminado y cambios guardados.")
            else:
                print("⚠️ Contacto no encontrado.")

        elif opcion == "5":
            print("👋 Volviendo al menú principal...")
            break

        else:
            print("⚠️ Opción inválida.")



if __name__ == "__main__":
    agenda_contactos()
