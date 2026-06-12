# ============================================
# Proyecto: Velocity Racing Team - TPO
# Materia: Pensamiento Computacional, Algoritmia y Programación
# Equipo 06
# Integrantes: Pilar Rivas, Martina Medina, Valentina Mendez
#
# Autoria:
# - Valentina Mendez: circuitos, paises, fechas
# - Pilar Rivas:      flujo del while principal
# - Martina Medina:   inicializacion de listas de pilotos y escuderias, main
# ============================================

import Funciones
import subfunciones

def main():
    # Martina Medina
    nombres             = ["FRANCO COLAPINTO", "LANDO NORRIS", "MAX VERSTAPPEN", "SERGIO PEREZ"]
    num_identificatorio = [43, 1, 3, 11]
    escuderia           = ["ALPINE", "MCLAREN", "RED BULL RACING", "CADILLAC"]
    esc_nombres  = ["MCLAREN", "FERRARI", "MERCEDES", "RED BULL RACING", "ASTON MARTIN",
                    "ALPINE", "WILLIAMS", "RACING BULLS", "HAAS", "AUDI", "CADILLAC"]
    esc_paises   = ["INGLATERRA", "ITALIA", "ALEMANIA", "AUSTRIA", "INGLATERRA",
                    "FRANCIA", "INGLATERRA", "ITALIA", "ESTADOS UNIDOS", "ALEMANIA", "ESTADOS UNIDOS"]
    esc_sponsors = [["GOOGLE"], ["SHELL"], ["PETRONAS"], ["ORACLE"], ["ARAMCO"],
                    ["BWT"], ["DURACELL"], ["VISA"], ["MONSTER"], ["ADIDAS"], ["TBD"]]
    puntos_acumulados    = [110, 215, 200, 100]
    tiempo_promedio      = [80.30, 85.25, 95.20, 85.10]
    presupuesto_asignado = [2500000, 3800000, 2600000, 2000000]
    abandonos            = [0, 2, 4, 1]

    # Valentina Mendez
    circuitos = ["MONZA", "SILVERSTONE", "MONACO", "SUZUKA"]
    paises    = ["ITALIA", "REINO UNIDO", "MONACO", "JAPON"]
    fechas    = ["2026-09-07", "2026-07-06", "2026-05-25", "2026-10-04"]

    # Pilar Rivas
    Funciones.opciones_menu()
    opcion = Funciones.ingresar_opcionMenu(1, 7)
    while opcion != 7:
        if opcion == 1:
            print("Alta de Pilotos")
            Funciones.altaPiloto(esc_nombres, nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos)
        elif opcion == 2:
            print("Eliminar Piloto")
            Funciones.eliminarPiloto(nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos)
        elif opcion == 3:
            print("Modificar puntos")
            Funciones.modificarPuntos(nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos)
        elif opcion == 4:
            print("Informe General")
            Funciones.informeGeneral(nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos)
        elif opcion == 5:
            print("Gestion de escuderias")
            Funciones.gestionEscuderias(esc_nombres, esc_paises, esc_sponsors, nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos)
        elif opcion == 6:
            print("Informe de Carreras")
            Funciones.informeCarreras(circuitos, paises, fechas)
        Funciones.opciones_menu()
        opcion = Funciones.ingresar_opcionMenu(1, 7)

main()
