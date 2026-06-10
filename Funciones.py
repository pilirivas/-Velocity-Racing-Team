# ============================================
# Proyecto: Velocity Racing Team - TPO
# Materia: Pensamiento Computacional, Algoritmia y Programación
# Equipo 06
# Integrantes: Pilar Rivas, Martina Medina, Valentina Mendez
# Autoría: El equipo trabajó de forma colaborativa. No se dividieron tareas por función ni por módulo.
# ============================================

import subfunciones

def escuderias():
    '''Retorna la lista de escuderias validas de la temporada.'''
    lista = ["MCLAREN", "FERRARI", "MERCEDES", "RED BULL RACING", "ASTON MARTIN",
             "ALPINE", "WILLIAMS", "RACING BULLS", "HAAS", "AUDI", "CADILLAC"]
    return lista

def opciones_menu():
    '''Muestra por pantalla las opciones del menu principal.'''
    print()
    print("=" * 50)
    print("            Velocity Racing Team ")
    print("=" * 50)
    print("1: Alta de Piloto")
    print("2: Eliminar Piloto")
    print("3: Modificar puntos")
    print("4: Informe general (datos)")
    print("5: Salida")
    print("=" * 50)

def ingresar_opcionMenu(desde, hasta):
    '''Valida ingresar un valor en el rango desde-hasta.
    Retorna el valor ingresado del teclado.'''
    op = input("Seleccione una opcion:")
    while not op.isdigit() or int(op) < desde or int(op) > hasta:
        print("La opcion seleccionada no es valida")
        op = input("Seleccione una opcion:")
    return int(op)

def altaPiloto(nombres, numero_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos):
    '''Da de alta a un piloto. Valida cada campo antes de agregarlo y recien
    al final hace el append a todas las listas.'''
    nombre     = subfunciones.pedirNombre(nombres)
    numero     = subfunciones.pedirNumeroNuevo(numero_identificatorio)
    escu       = subfunciones.pedirEscuderia()
    puntos     = subfunciones.ingresarNoNegativo("Ingrese los puntos acumulados del piloto: ")
    tiempo     = subfunciones.ingresarNoNegativoFloat("Ingrese el tiempo promedio del piloto: ")
    presupuesto = subfunciones.ingresarNoNegativoFloat("Ingrese el presupuesto asignado al piloto: ")
    aband      = subfunciones.ingresarNoNegativo("Ingrese el numero de abandonos del piloto: ")

    nombres.append(nombre)
    numero_identificatorio.append(numero)
    escuderia.append(escu)
    puntos_acumulados.append(puntos)
    tiempo_promedio.append(tiempo)
    presupuesto_asignado.append(presupuesto)
    abandonos.append(aband)

def eliminarPiloto(nombres, numero_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos):
    '''Elimina un piloto buscado por su numero identificatorio.
    Solo se permite si tiene 0 puntos, y pide confirmacion antes de borrar.'''
    numeroEliminar = subfunciones.pedirNumeroAEliminar()
    indice = subfunciones.buscarPorNumero(numero_identificatorio, numeroEliminar)
    if indice == -1:
        print("No se encontro un piloto con ese numero identificatorio.")
        return
    if not subfunciones.validarEliminacion(nombres, puntos_acumulados, indice):
        return
    if subfunciones.confirmarEliminacion(nombres, indice):
        subfunciones.borrarPilotoDeListas(nombres, numero_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos, indice)
        print("Piloto eliminado exitosamente.")
    else:
        print("Operacion cancelada.")

def informeGeneral(nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos):
    '''Muestra los pilotos en formato de tabla, ordenados de mayor a menor
    por puntos. Ante empate, de menor a mayor por tiempo promedio.'''
    indices = subfunciones.crearIndices(nombres)
    subfunciones.ordenarIndicesPorPuntosYTiempo(indices, puntos_acumulados, tiempo_promedio)
    subfunciones.imprimirTabla(indices, nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos)

def modificarPuntos(nombres, numero_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos):
    '''Modifica los puntos acumulados de un piloto buscado por su numero.'''
    numeroModificar = subfunciones.ingresarPositivo("Ingrese el numero identificatorio del piloto para modificar sus puntos: ")
    indice = subfunciones.buscarPorNumero(numero_identificatorio, numeroModificar)
    if indice != -1:
        nuevosPuntos = subfunciones.ingresarNoNegativo("Ingrese los nuevos puntos acumulados del piloto: ")
        puntos_acumulados[indice] = nuevosPuntos
        print("Puntos acumulados del piloto modificados exitosamente.")
    else:
        print("No se encontro un piloto con ese numero identificatorio.")
