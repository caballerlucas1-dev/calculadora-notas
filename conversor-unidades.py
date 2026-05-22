# conversor_unidades.py
def menu():
    print("=== Conversor de Unidades ===")
    print("1. Temperatura\n2. Distancia\n3. Peso")
    return input("Elegí una categoría: ")

def temperatura():
    print("1. Celsius → Fahrenheit\n2. Fahrenheit → Celsius\n3. Celsius → Kelvin")
    op = input("Opción: ")
    v = float(input("Valor: "))
    if op == "1": print(f"Resultado: {v * 9/5 + 32:.2f} °F")
    elif op == "2": print(f"Resultado: {(v - 32) * 5/9:.2f} °C")
    elif op == "3": print(f"Resultado: {v + 273.15:.2f} K")

def distancia():
    print("1. Km → Millas\n2. Millas → Km\n3. Metros → Pies")
    op = input("Opción: ")
    v = float(input("Valor: "))
    if op == "1": print(f"Resultado: {v * 0.621371:.2f} millas")
    elif op == "2": print(f"Resultado: {v * 1.60934:.2f} km")
    elif op == "3": print(f"Resultado: {v * 3.28084:.2f} pies")

def peso():
    print("1. Kg → Libras\n2. Libras → Kg\n3. Gramos → Onzas")
    op = input("Opción: ")
    v = float(input("Valor: "))
    if op == "1": print(f"Resultado: {v * 2.20462:.2f} lb")
    elif op == "2": print(f"Resultado: {v * 0.453592:.2f} kg")
    elif op == "3": print(f"Resultado: {v * 0.035274:.2f} oz")

if __name__ == "__main__":
    cat = menu()
    if cat == "1": temperatura()
    elif cat == "2": distancia()
    elif cat == "3": peso()
