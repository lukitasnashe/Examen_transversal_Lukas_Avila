import random
import statistics
import csv

trabajadores = [
    {"nombre": "Juan Pérez", "cargo": "Consultor TI"},
    {"nombre": "María García", "cargo": "Analista"},
    {"nombre": "Carlos López", "cargo": "Programador"},
    {"nombre": "Ana Martínez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Pedro Rodríguez", "cargo": "Consultor TI"},
    {"nombre": "Laura Hernández", "cargo": "Analista"},
    {"nombre": "Miguel Sánchez", "cargo": "Programador"},
    {"nombre": "Isabel Gómez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Francisco Díaz", "cargo": "Consultor TI"},
    {"nombre": "Elena Fernández", "cargo": "Analista"}
]

def asignar_sueldo():
    for empleado in trabajadores:
        empleado["sueldo"] = random.randint(300000, 2500000)

def clasificar():
    for empleado in trabajadores:
        nom = empleado["nombre"]
        sueldo = empleado["sueldo"]
        if sueldo < 800000:
            print(f"{nom}: {empleado['cargo']}, ${sueldo} - Sueldo bajo")
        elif 800000 <= sueldo <= 2000000:
            print(f"{nom}: {empleado['cargo']}, ${sueldo} - Sueldo medio")
        else:
            print(f"{nom}: {empleado['cargo']}, ${sueldo} - Sueldo alto")

def estadisticas():
    sueldos = [empleado["sueldo"] for empleado in trabajadores]
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio_sueldo = statistics.mean(sueldos)
    medida_G = statistics.geometric_mean(sueldos)

    print("Estadísticas:")
    print(f"Sueldo más alto: ${sueldo_max}")
    print(f"Sueldo más bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${promedio_sueldo}")
    print(f"Medida geométrica de sueldos: ${medida_G}")

def reporte():
    nom_archivo = "reporte_sueldo.csv"
    with open(nom_archivo, mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['nombre', 'cargo', 'sueldo_base', 'descuento_salud', 'descuento_afp', 'sueldo_liquido'])

        for empleado in trabajadores:
            nom = empleado['nombre']
            cargo = empleado['cargo']
            sueldo_base = empleado['sueldo']
            descuento_salud = sueldo_base * 0.07
            descuento_AFP = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - descuento_salud - descuento_AFP
            
            writer.writerow([nom, cargo, sueldo_base, descuento_salud, descuento_AFP, sueldo_liquido])
            print(f"\nNombre empleado: {nom} Cargo: {cargo} Sueldo Base: ${sueldo_base} Descuento Salud: ${descuento_salud} Descuento AFP: ${descuento_AFP} Sueldo Líquido: ${sueldo_liquido}")

while True:
    print("\nMenú")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Generar reporte de sueldos")
    print("5. Salir del programa")

    op = input("Seleccione una opción: \n")
    
    if op == "1":
        asignar_sueldo()
        print("Sueldos asignados aleatoriamente")
    elif op == "2":
        clasificar()
    elif op == "3":
        estadisticas()
    elif op == "4":
        reporte()
    elif op == "5":
        print("Finalizando programa...")
        print("\nDesarrollado por: Lukas Avila")
        print("Rut: 21.078.969-3\n")
        break
    else:
        print("Opción no válida, intente nuevamente.")
        