import os
import modulos.menus as m
import modulos.equipos as eq
import modulos.plantel as pt
import modulos.partidos as pa
import modulos.resultados as rs
import modulos.tabla as tb
import modulos.validarOpcion as vo
import modulos.mensajes as msg

isAllow = True

if (__name__ == "__main__"):
    liga = []
    isLiga = True
    while (isLiga):
        os.system('cls')
        print(m.menu)
        try:
            opcMenu = int(input(': '))
            match opcMenu:
                case 1:
                    isEquipos = True
                    while isEquipos:
                        os.system('cls')
                        print(m.menuEquipos)
                        try:
                            opcSubMenu = int(input(': '))
                            match opcSubMenu:
                                case 1:
                                    eq.addEquipos(liga)
                                case 2:
                                    eq.viewEquipos(liga)
                                    os.system('pause')
                                case 3:
                                    eq.delEquipos(liga)
                                case 4:
                                    isEquipos = False
                                case _:
                                    print('Opcion invalida...')
                                    os.system('pause')
                        except ValueError:
                            print("Entrada inválida, por favor ingrese un número entero.")
                            os.system('pause')
                case 2:
                    isPlantel = True
                    while isPlantel:
                        os.system('cls')
                        print(m.menuPlantel)
                        try:
                            opcSubMenu = int(input(': '))
                            match opcSubMenu:
                                case 1:
                                    pt.addPlantelCT(liga)
                                case 2:
                                    pt.addPlantelJ(liga)
                                case 3:
                                    pt.delCuerpoTecnico()
                                case 4:
                                    pt.delJugadores()
                                case 5:
                                    isPlantel = False
                                case _:
                                    print('Opcion invalida...')
                                    os.system('pause')
                        except ValueError:
                            print("Entrada inválida, por favor ingrese un número entero.")
                            os.system('pause')
                case 3:
                    isPartidos = True
                    while isPartidos:
                        os.system('cls')
                        print(m.menuPartidos)
                        try:
                            opcSubMenu = int(input(': '))
                            match opcSubMenu:
                                case 1:
                                    pa.addPartidos(liga,partidos=list)
                                case 2:
                                    pa.viewPartidos(liga)
                                case 3:
                                    pa.registrarResultado(liga)
                                case 4:
                                    isPartidos = False
                                case _:
                                    print('Opcion invalida...')
                                    os.system('pause')
                        except ValueError:
                            print("Entrada inválida, por favor ingrese un número entero.")
                            os.system('pause')
                case 4:
                    isResultados = True
                    while isResultados:
                        os.system('cls')
                        print(m.menuPartidos)
                        try:
                            opcSubMenu = int(input(': '))
                            match opcSubMenu:
                                case 1:
                                    rs.addResultados()
                                case 2:
                                    rs.viewResultados()
                                case 3:
                                    rs.delResultados()
                                case 4:
                                    isResultados = False
                                case _:
                                    print('Opcion invalida...')
                                    os.system('pause')
                        except ValueError:
                            print("Entrada inválida, por favor ingrese un número entero.")
                            os.system('pause')
                case 5:
                    isTabla = True
                    while isTabla:
                        os.system('cls')
                        print(m.menuTabla)
                        try:
                            opcSubMenu = int(input(': '))
                            match opcSubMenu:
                                case 1:
                                    tb.viewTabla()
                                case 2:
                                    isTabla = False
                                case _:
                                    print('Opcion invalida...')
                                    os.system('pause')
                        except ValueError:
                            print("Entrada inválida, por favor ingrese un número entero.")
                            os.system('pause')
                case 6:
                    isLiga = vo.validarSalida(msg.msgSalir)
                    print('Nos veremos proximamente...')
                case _:
                    print('Opcion invalida...')
                    os.system('pause')
        except ValueError:
            print("Entrada inválida, por favor ingrese un número entero.")
            os.system('pause')