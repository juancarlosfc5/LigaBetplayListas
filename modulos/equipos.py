import os
import modulos.validarOpcion as vo
import modulos.mensajes as msg
#equipos = [nombre, cuerpoTecnico, jugadores, estadisticas]
def addEquipos(src:list):
    isAddEquipos = True
    while(isAddEquipos):
        os.system('cls')
        nombre = input('Ingrese el nombre del equipo: ')
        equipo = [nombre,[],[],[],[]]
        src.append(equipo)
        isAddEquipos = vo.validarOpcion(msg.msgEquipo)
    return

def viewEquipos(src:list):
    os.system('cls')
    if (len(src) == 0):
        print("No hay equipos registrados")
    else:
        print("Equipos registrados:")
        for idx, equipo in enumerate(src):
            print(f"{idx+1}. {equipo[0]}")
        return (int(input(': '))-1)

def delEquipos(src:list):
    print('Seleccione el equipo que desea borrar: ')
    delete = viewEquipos(src)
    if (len(src) == 0):
        os.system('pause')
    else:
        if (vo.validarOpcion(msg.msgDelete)):
            src.pop(delete)
        else:
            print(msg.msgCancel)
