
# Agenda de Contactos

Este programa permite gestionar una agenda de contactos desde la consola, almacenando la información en un archivo CSV para mantener la persistencia de los datos.

## Funcionalidades principales

- **Ver contactos:** Muestra la lista de todos los contactos guardados.
- **Agregar contacto:** Permite ingresar un nuevo contacto con nombre y teléfono.
- **Buscar contacto:** Busca un contacto por su nombre y muestra su número de teléfono si existe.
- **Eliminar contacto:** Elimina un contacto existente de la agenda.
- **Persistencia:** Todos los cambios se guardan automáticamente en el archivo `agenda.csv`.

## ¿Cómo usarlo?

1. Ejecuta el archivo `agenda.py` desde la consola:
	```bash
	python agenda.py
	```
2. Selecciona la opción deseada en el menú:
	- 1: Ver contactos
	- 2: Agregar contacto
	- 3: Buscar contacto
	- 4: Eliminar contacto
	- 5: Salir

## Requisitos

- Python 3.x

No requiere librerías externas adicionales, solo las estándar (`csv`, `os`).


