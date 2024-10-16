import os
import modulos.validarOpcion as vo
import modulos.mensajes as msg
#cuerpoTecnico = [nombre, rol]
#jugadores = [nombre, posicion, camisa, dorsal]
def addPlantelCT(src:list):
    found = True
    if (len(src) > 0):
        os.system('cls')
        equipo = input('Ingrese el nombre del equipo a buscar: ')
        for nombre in src:
            if (equipo in nombre):
                addCuerpoTecnico(nombre)
                found = True
                print(src)
                os.system('pause')
                break
        if (found == False):
            print('El equipo no se encuentra registrado')
            os.system('pause')
    else:
        os.system('cls')
        print("No hay equipos registrados")
        os.system('pause')

def addCuerpoTecnico(lstperson:list):
    isAddCuerpoTecnico = True
    while(isAddCuerpoTecnico):
        os.system('cls')
        nombreCT = input('Ingrese el nombre del personal del cuerpo tecnico: ')
        rol = input('Ingrese el rol del personal del cuerpo tecnico: ')
        person = [nombreCT,rol]
        lstperson[1].append(person)
        isAddCuerpoTecnico = vo.validarOpcion(msg.msgCuerpoTecnico)

def addPlantelJ(src:list):
    found = True
    if (len(src) > 0):
        os.system('cls')
        equipo = input('Ingrese el nombre del equipo a buscar: ')
        for nombre in src:
            if (equipo in nombre):
                addJugadores(nombre)
                found = True
                print(src)
                os.system('pause')
                break
        if (found == False):
            print('El equipo no se encuentra registrado')
            os.system('pause')
    else:
        os.system('cls')
        print("No hay equipos registrados")
        os.system('pause')

def addJugadores(lstplayers:list):
    isAddJugadores = True
    while(isAddJugadores):
        os.system('cls')
        nombreJ = input('Ingrese el nombre del jugador: ')
        posicion = input('Ingrese la posicion de juego del jugador: ')
        camisa = input('Ingrese el texto a imprimir en la camisa del jugador: ')
        dorsal = input('Ingrese el dorsal del jugador: ')
        players = [nombreJ,posicion,camisa, dorsal]
        lstplayers[2].append(players)
        isAddJugadores = vo.validarOpcion(msg.msgJugador)

def delCuerpoTecnico():
    return

def delJugadores():
    return