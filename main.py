import Funciones

def main():
    nombres=["FRANCO COLAPINTO", "LANDO NORRIS", "MAX VERSTAPPEN", "SERGIO PEREZ"]
    num_identificatorio=[43, 1, 3, 11]
    escuderia=["ALPINE", "MCLAREN", "RED BULL RACING", "CADILLAC"]
    puntos_acumulados=[110, 215, 200, 100]
    tiempo_promedio=[80.30, 85.25, 95.20, 85.10]
    presupuesto_asignado=[2500000, 3800000, 2600000, 2000000]
    abandonos=[0,2,4,1]
    Funciones.opciones_menu()
    opcion = Funciones.ingresar_opcionMenu(1,5)
    while opcion != 5:
        if opcion == 1:
            print("Alta de Pilotos")
            Funciones.altaPiloto(nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos)
        elif opcion == 2:
            print("Eliminar Piloto")
            Funciones.eliminarPiloto(nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos)
        elif opcion == 3:
            print("Modificar puntos")
            Funciones.modificarPuntos(nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos)
        elif opcion == 4:
            print("Informe General")
            Funciones.informeGeneral(nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos)
        Funciones.opciones_menu()
        opcion = Funciones.ingresar_opcionMenu(1,5)
main()