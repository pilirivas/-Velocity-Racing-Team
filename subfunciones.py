# ============================================
# Proyecto: Velocity Racing Team - TPO
# Materia: Pensamiento Computacional, Algoritmia y Programación
# Equipo 06
# Integrantes: Pilar Rivas, Martina Medina, Valentina Mendez
#
# Autoria:
# - Valentina Mendez: ROJO, VERDE, NORMAL, ingresarPositivo, ingresarNoNegativo,
#					  ingresarNoNegativoFloat, pedirNombre, pedirNumeroNuevo,
#					  calcularDiasRestantes, imprimirTablaCarreras
# - Pilar Rivas:      pedirNumeroAEliminar, validarEliminacion, confirmarEliminacion,
#                     borrarPilotoDeListas, crearIndices, ordenarIndicesPorPuntosYTiempo,
#                     imprimirTabla
# - Martina Medina:   esDecimalValido, buscarPorNumero, pedirEscuderia, pedirSponsors,
#                     subMenuEscuderias, escuderiasDisponibles, agregarEscuderia,
#                     eliminarEscuderia, modificarEscuderiaPiloto, buscarPorEscuderia
# ============================================
import time

# Valentina Mendez
ROJO   = "\033[91m"
VERDE  = "\033[92m"
NORMAL = "\033[0m"

def ingresarPositivo(msg):
    '''Pide un entero por teclado y valida que sea positivo (> 0).
    Repite hasta recibir un valor valido y lo retorna.'''
    num = input(msg)
    while not num.isdigit() or int(num) <= 0:
        print(ROJO + "Error debe ser positivo" + NORMAL)
        num = input(msg)
    return int(num)

def ingresarNoNegativo(msg):
    '''Pide un entero por teclado y valida que no sea negativo (acepta 0).
    Repite hasta recibir un valor valido y lo retorna.'''
    num = input(msg)
    while not num.isdigit():
        print(ROJO + "Error debe ser positivo o cero" + NORMAL)
        num = input(msg)
    return int(num)

def ingresarNoNegativoFloat(msg):
    '''Pide un decimal por teclado, valida formato y que no sea negativo.'''
    num = input(msg)
    while not esDecimalValido(num):
        print(ROJO + "Error: debe ingresar un numero decimal valido (positivo o cero)." + NORMAL)
        num = input(msg)
    return float(num)
    
def pedirNombre(nombres):
    '''Pide nombre y apellido. Repite si no tiene espacio o ya existe en la lista.'''
    while True:
        nombre = input("Ingrese el Nombre del piloto: ").upper()
        if " " not in nombre:
            print(ROJO + "Error: debe ingresar nombre y apellido." + NORMAL)
        elif nombre in nombres:
            print(ROJO + "Error: ya existe un piloto con ese nombre." + NORMAL)
        else:
            return nombre

def pedirNumeroNuevo(numero_identificatorio):
    '''Pide un numero identificatorio positivo y unico.
    Repite si ya existe en la lista.'''
    numero = ingresarPositivo("Ingrese el numero identificatorio del piloto: ")
    while numero in numero_identificatorio:
        print(ROJO + "Error: ya existe un piloto con ese numero identificatorio." + NORMAL)
        numero = ingresarPositivo("Ingrese el numero identificatorio del piloto: ")
    return numero

def calcularDiasRestantes(fecha_str):
    '''Recibe una fecha en formato texto y calcula los dias que faltan usando el time.
    Retorna un entero. Si la fecha ya paso, retorna 0.'''
    anio = int(fecha_str[0:4])
    mes  = int(fecha_str[5:7])
    dia  = int(fecha_str[8:10])
    hoy      = time.localtime()
    anio_hoy = hoy.tm_year
    mes_hoy  = hoy.tm_mon
    dia_hoy  = hoy.tm_mday
    dias_carrera = anio * 365 + mes * 30 + dia
    dia_hoy      = anio_hoy * 365 + mes_hoy * 30 + dia_hoy
    restantes = dias_carrera - dia_hoy
    if restantes < 0:
        return 0
    return restantes

def imprimirTablaCarreras(circuitos, paises, fechas):
    '''Imprime la tabla de carreras con los dias restantes para cada una.'''
    print()
    print(VERDE + "=" * 65 + NORMAL)
    print(f"{'#':<5} {'CIRCUITO':<20} {'PAIS':<18} {'FECHA':<12} {'DIAS REST.':>10}")
    print(VERDE + "-" * 65 + NORMAL)
    for i in range(len(circuitos)):
        dias = calcularDiasRestantes(fechas[i])
        print(f"{i+1:<5} {circuitos[i]:<20} {paises[i]:<18} {fechas[i]:<12} {dias:>10}")
    print(VERDE + "=" * 65 + NORMAL)

# Pilar Rivas
def pedirNumeroAEliminar():
    '''Solicita y retorna el numero identificatorio del piloto a eliminar.'''
    return ingresarPositivo("Ingrese el numero identificatorio del piloto a eliminar: ")

def validarEliminacion(nombres, puntos_acumulados, indice):
    '''Verifica que el piloto tenga 0 puntos. Retorna True si se puede eliminar.'''
    if puntos_acumulados[indice] != 0:
        print(ROJO + "Error: no se puede eliminar a un piloto con puntos acumulados." + NORMAL)
        return False
    return True

def confirmarEliminacion(nombres, indice):
    '''Pide confirmacion al usuario. Retorna True si confirma con s.'''
    confirmacion = input("Confirma que desea eliminar a '" + nombres[indice] + "'? (s/n): ").lower()
    return confirmacion == "s"

def borrarPilotoDeListas(nombres, numero_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos, indice):
    '''Elimina la posicion indicada en todas las listas paralelas.'''
    nombres.pop(indice)
    numero_identificatorio.pop(indice)
    escuderia.pop(indice)
    puntos_acumulados.pop(indice)
    tiempo_promedio.pop(indice)
    presupuesto_asignado.pop(indice)
    abandonos.pop(indice)

def crearIndices(nombres):
    '''Retorna una lista de indices [0, 1, 2, ...] con un elemento por piloto.'''
    indices = []
    for i in range(len(nombres)):
        indices.append(i)
    return indices

def ordenarIndicesPorPuntosYTiempo(indices, puntos_acumulados, tiempo_promedio):
    '''Ordena la lista de indices por seleccion: mayor puntos primero;
    ante empate, menor tiempo promedio primero.'''
    for i in range(len(indices)):
        mejor = i
        for j in range(i + 1, len(indices)):
            if puntos_acumulados[indices[j]] > puntos_acumulados[indices[mejor]]:
                mejor = j
            elif puntos_acumulados[indices[j]] == puntos_acumulados[indices[mejor]]:
                if tiempo_promedio[indices[j]] < tiempo_promedio[indices[mejor]]:
                    mejor = j
        aux = indices[i]
        indices[i] = indices[mejor]
        indices[mejor] = aux

def imprimirTabla(indices, nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos):
    '''Imprime la tabla de pilotos recorriendo los indices ya ordenados.'''
    print()
    print(VERDE + "=" * 95 + NORMAL)
    print(f"{'POS':<5} {'PILOTO':<22} {'N':<5} {'ESCUDERIA':<20} {'PUNTOS':>7} {'T.PROM(s)':>10} {'PRESUPUESTO':>13} {'ABAND.':>7}")
    print(VERDE + "-" * 95 + NORMAL)
    pos = 1
    for i in indices:
        print(f"{pos:<5} {nombres[i]:<22} {num_identificatorio[i]:<5} {escuderia[i]:<20} {puntos_acumulados[i]:>7} {tiempo_promedio[i]:>10.2f} ${presupuesto_asignado[i]:>12,.0f} {abandonos[i]:>7}")
        pos = pos + 1
    print(VERDE + "=" * 95 + NORMAL)

# Martina Medina 
def esDecimalValido(texto):
    '''Valida manualmente que un texto represente un decimal no negativo.
    Acepta digitos y a lo sumo un punto. No acepta signos ni espacios.'''
    if texto == "":
        return False
    cantPuntos = 0
    for caracter in texto:
        if caracter == ".":
            cantPuntos = cantPuntos + 1
        elif not caracter.isdigit():
            return False
    if cantPuntos > 1:
        return False
    if texto == ".":
        return False
    return True

def buscarPorNumero(numero_identificatorio, numero_buscado):
    '''Busqueda SECUENCIAL desarrollada manualmente.
    Retorna el indice si lo encuentra, -1 si no.'''
    for i in range(len(numero_identificatorio)):
        if numero_identificatorio[i] == numero_buscado:
            return i
    return -1

def pedirEscuderia(esc_nombres):
    '''Pide una escuderia valida de entre las escuderias registradas.
    Repite si esta vacia o no pertenece a la lista.'''
    escu = input("Ingrese la escuderia del piloto: ").upper().strip()
    while escu == "" or escu not in esc_nombres:
        if escu == "":
            print(ROJO + "Error: la escuderia no puede quedar vacia." + NORMAL)
        else:
            print(ROJO + "Error: la escuderia no es valida." + NORMAL)
        escu = input("Ingrese la escuderia del piloto: ").upper().strip()
    return escu

def pedirSponsors():
    '''Carga uno o varios sponsors. Exige al menos uno y no admite repetidos.'''
    sponsors = []
    while True:
        sponsor = input("Ingrese el nombre de un sponsor (o deje vacio para terminar): ").upper().strip()
        if sponsor == "":
            if len(sponsors) == 0:
                print(ROJO + "Error: debe cargar al menos un sponsor." + NORMAL)
            else:
                break
        elif sponsor in sponsors:
            print(ROJO + "Ese sponsor ya fue cargado para esta escuderia." + NORMAL)
        else:
            sponsors.append(sponsor)
    return sponsors

def subMenuEscuderias():
    '''Muestra por pantalla las opciones del submenu de escuderias.'''
    print()
    print(VERDE + "=" * 50 + NORMAL)
    print(VERDE + "        Gestion de Escuderias " + NORMAL)
    print(VERDE + "=" * 50 + NORMAL)
    print("1: Ver escuderias disponibles")
    print("2: Agregar nueva escuderia")
    print("3: Eliminar escuderia")
    print("4: Modificar escuderia de un piloto")
    print("5: Volver al menu principal")
    print(VERDE + "=" * 50 + NORMAL)

def escuderiasDisponibles(esc_nombres, esc_paises, esc_sponsors):
    '''Muestra todas las escuderias con su pais y sponsors.'''
    print("Escuderias disponibles:")
    for i in range(len(esc_nombres)):
        print(esc_nombres[i], "-", esc_paises[i])
        for sponsor in esc_sponsors[i]:
            print("   *", sponsor)
        print(VERDE + "*" * 30 + NORMAL)

def agregarEscuderia(esc_nombres, esc_paises, esc_sponsors):
    '''Agrega una nueva escuderia con pais y sponsors.'''
    nuevaEscuderia = input("Ingrese el nombre de la nueva escuderia: ").upper().strip()
    while nuevaEscuderia == "":
        print(ROJO + "Error: el nombre de la escuderia no puede quedar vacio." + NORMAL)
        nuevaEscuderia = input("Ingrese el nombre de la nueva escuderia: ").upper().strip()
    if nuevaEscuderia in esc_nombres:
        print(ROJO + "La escuderia ya existe." + NORMAL)
    else:
        pais = input("Ingrese el pais de origen: ").upper().strip()
        while pais == "":
            print(ROJO + "Error: el pais no puede quedar vacio." + NORMAL)
            pais = input("Ingrese el pais de origen: ").upper().strip()
        sponsors = pedirSponsors()
        esc_nombres.append(nuevaEscuderia)
        esc_paises.append(pais)
        esc_sponsors.append(sponsors)
        print("Nueva escuderia agregada exitosamente.")

def eliminarEscuderia(esc_nombres, esc_paises, esc_sponsors, nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos):
    '''Elimina una escuderia. Si tiene pilotos, pregunta si darlos de baja tambien.'''
    nombreEliminar = input("Ingrese el nombre de la escuderia a eliminar: ").upper().strip()
    indiceEsc = -1
    for i in range(len(esc_nombres)):
        if esc_nombres[i] == nombreEliminar:
            indiceEsc = i
    if indiceEsc == -1:
        print(ROJO + "No se encontro esa escuderia." + NORMAL)
        return
    indicePiloto = buscarPorEscuderia(escuderia, nombreEliminar)
    if indicePiloto != -1:
        respuesta = input("La escuderia tiene pilotos asignados. Desea darlos de baja tambien? (s/n): ").lower()
        if respuesta != "s":
            print(ROJO + "Operacion cancelada." + NORMAL)
            return
        indicePiloto = buscarPorEscuderia(escuderia, nombreEliminar)
        while indicePiloto != -1:
            borrarPilotoDeListas(nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos, indicePiloto)
            indicePiloto = buscarPorEscuderia(escuderia, nombreEliminar)
    esc_nombres.pop(indiceEsc)
    esc_paises.pop(indiceEsc)
    esc_sponsors.pop(indiceEsc)
    print("Escuderia eliminada exitosamente.")

def modificarEscuderiaPiloto(esc_nombres, numero_identificatorio, escuderia):
    '''Modifica la escuderia de un piloto buscado por su numero.'''
    numeroPiloto = ingresarPositivo("Ingrese el numero identificatorio del piloto para modificar su escuderia: ")
    indice = buscarPorNumero(numero_identificatorio, numeroPiloto)
    if indice != -1:
        nuevaEscu = input("Ingrese el nombre de la nueva escuderia del piloto: ").upper().strip()
        if nuevaEscu in esc_nombres:
            escuderia[indice] = nuevaEscu
            print("Escuderia del piloto modificada exitosamente.")
        else:
            print(ROJO + "No se encontro esa escuderia." + NORMAL)
    else:
        print(ROJO + "No se encontro un piloto con ese numero identificatorio." + NORMAL)

def buscarPorEscuderia(escuderia, nombre_buscado):
    '''Busqueda secuencial: retorna el indice del PRIMER piloto cuya
    escuderia coincide con nombre_buscado, o -1 si no hay ninguno.'''
    for i in range(len(escuderia)):
        if escuderia[i] == nombre_buscado:
            return i
    return -1
