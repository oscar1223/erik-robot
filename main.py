import requests
import csv
from datetime import datetime
from openpyxl import Workbook

# CONFIGURACIÓN
API_URL = "https://ejemplo.com/api/coordinates"  # ← Cambia por tu URL real

# Obtener fecha actual
fecha_actual = datetime.now().strftime("%Y-%m-%d")
CSV_FILE = f"coordenadas_{fecha_actual}.csv"
EXCEL_FILE = f"coordenadas_{fecha_actual}.xlsx"

# Obtener datos desde API
def obtener_coordenada():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error al obtener datos: {e}")
        return None

# Guardar en CSV (crear nuevo cada vez)
def guardar_en_csv(coordenada):
    try:
        headers = list(coordenada.keys())
        with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerow(coordenada)
        print(f"Archivo CSV creado: {CSV_FILE}")
    except Exception as e:
        print(f"Error al guardar en CSV: {e}")

# Guardar en Excel (crear nuevo cada vez)
def guardar_en_excel(coordenada):
    try:
        headers = list(coordenada.keys())
        wb = Workbook()
        ws = wb.active
        ws.title = "Coordenadas"
        ws.append(headers)
        ws.append([coordenada.get(h, "") for h in headers])
        wb.save(EXCEL_FILE)
        print(f"Archivo Excel creado: {EXCEL_FILE}")
    except Exception as e:
        print(f"Error al guardar en Excel: {e}")

# Ejecutar flujo principal
def main():
    coordenada = obtener_coordenada()
    if coordenada:
        guardar_en_csv(coordenada)
        guardar_en_excel(coordenada)
    else:
        print("No se recibió ninguna coordenada.")

if __name__ == "__main__":
    main()
