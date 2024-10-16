import os
import modulos.validarOpcion as vo
import modulos.mensajes as msg

def addPartidos(equipos: list, partidos: list):
    if len(equipos) < 2:
        print("Debe haber al menos dos equipos registrados para crear un partido.")
        return

    os.system('cls')
    print("Creando un nuevo partido")
    
    # Mostrar los equipos disponibles
    print(equipos)
    
    # Pedir el nombre del equipo local
    equipo_local = input('Ingrese el nombre del equipo local: ')
    equipo_visitante = input('Ingrese el nombre del equipo visitante: ')

    # Verificar que ambos equipos estén registrados
    local_encontrado = False
    visitante_encontrado = False
    for equipo in equipos:
        if equipo_local == equipo[0]:
            local_encontrado = True
        if equipo_visitante == equipo[0]:
            visitante_encontrado = True
    
    if not local_encontrado or not visitante_encontrado:
        print("Uno o ambos equipos no están registrados.")
        os.system('pause')
        return
    
    # Verificar que no se trate del mismo equipo
    if equipo_local == equipo_visitante:
        print("Un equipo no puede jugar contra sí mismo.")
        os.system('pause')
        return

    # Registrar el partido con goles inicializados a 0
    partido = {
        "local": equipo_local,
        "visitante": equipo_visitante,
        "goles_local": 0,
        "goles_visitante": 0
    }
    
    partidos.append(partido)
    print(f"Partido registrado: {equipo_local} vs {equipo_visitante}")
    os.system('pause')

def viewPartidos(partidos: list):
    if len(partidos) == 0:
        print("No hay partidos registrados.")
        return

    os.system('cls')
    print("Partidos registrados:")
    
    # Mostrar los partidos registrados con los resultados
    for partido in partidos:
        print(f"{partido['local']} vs {partido['visitante']} (Goles: {partido['goles_local']} - {partido['goles_visitante']})")
    
    os.system('pause')

def registrarResultado(partidos: list):
    if len(partidos) == 0:
        print("No hay partidos registrados.")
        return

    os.system('cls')
    print("Partidos registrados:")
    
    # Mostrar los partidos registrados
    for idx, partido in enumerate(partidos, start=1):
        print(f"{idx}. {partido['local']} vs {partido['visitante']} (Goles: {partido['goles_local']} - {partido['goles_visitante']})")
    
    try:
        num_partido = int(input(f"Ingrese el número del partido para registrar el resultado (1-{len(partidos)}): "))
        if num_partido < 1 or num_partido > len(partidos):
            print("Número de partido no válido.")
            return
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número.")
        return
    
    # Obtener el partido seleccionado
    partido_seleccionado = partidos[num_partido - 1]
    
    # Registrar los goles de ambos equipos
    try:
        goles_local = int(input(f"Ingrese los goles para el equipo local ({partido_seleccionado['local']}): "))
        goles_visitante = int(input(f"Ingrese los goles para el equipo visitante ({partido_seleccionado['visitante']}): "))
        
        partido_seleccionado["goles_local"] = goles_local
        partido_seleccionado["goles_visitante"] = goles_visitante

        print("Marcador actualizado.")
    except ValueError:
        print("Por favor, ingrese un número válido de goles.")
    
    os.system('pause')

def delPartidos():
    return