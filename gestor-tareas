# gestor_tareas.py
import json, os

ARCHIVO = "tareas.json"

def cargar():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO) as f:
            return json.load(f)
    return []

def guardar(tareas):
    with open(ARCHIVO, "w") as f:
        json.dump(tareas, f, indent=2)

def mostrar(tareas):
    if not tareas:
        print("No hay tareas.")
        return
    for i, t in enumerate(tareas):
        estado = "✓" if t["hecha"] else "○"
        print(f"{i+1}. [{estado}] {t['nombre']}")

def menu():
    tareas = cargar()
    while True:
        print("\n=== Gestor de Tareas ===")
        print("1. Ver tareas\n2. Agregar\n3. Completar\n4. Eliminar\n5. Salir")
        op = input("Opción: ")
        if op == "1":
            mostrar(tareas)
        elif op == "2":
            nombre = input("Nombre de la tarea: ")
            tareas.append({"nombre": nombre, "hecha": False})
            guardar(tareas)
        elif op == "3":
            mostrar(tareas)
            i = int(input("Número de tarea: ")) - 1
            tareas[i]["hecha"] = True
            guardar(tareas)
        elif op == "4":
            mostrar(tareas)
            i = int(input("Número a eliminar: ")) - 1
            tareas.pop(i)
            guardar(tareas)
        elif op == "5":
            break

if __name__ == "__main__":
    menu()
