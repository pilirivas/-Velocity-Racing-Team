# ============================================
# Proyecto: Velocity Racing Team - TPO
# Materia: Pensamiento Computacional, Algoritmia y Programación
# Equipo 06
# Integrantes: Pilar Rivas, Martina Medina, Valentina Mendez
# ============================================

# Funciones de ingreso y validacion 
def ingresarPositivo(msg):
    '''Pide un entero por teclado y valida que sea positivo (> 0).
    Repite hasta recibir un valor valido y lo retorna.'''
    num = input(msg)
    while not num.isdigit() or int(num) <= 0:
        print("Error debe ser positivo")
        num = input(msg)
    return int(num)

def ingresarNoNegativo(msg):
    '''Pide un entero por teclado y valida que no sea negativo (acepta 0).
    Repite hasta recibir un valor valido y lo retorna.'''
    num = input(msg)
    while not num.isdigit():
        print("Error debe ser positivo o cero")
        num = input(msg)
    return int(num)

def ingresarNoNegativoFloat(msg):
    '''Pide un decimal por teclado, valida formato y que no sea negativo.'''
    num = input(msg)
    while not esDecimalValido(num):
        print("Error: debe ingresar un numero decimal valido (positivo o cero).")
        num = input(msg)
    return float(num)

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

# Subfunciones de altaPiloto
def pedirNombre(nombres):
    '''Pide nombre y apellido. Repite si no tiene espacio o ya existe en la lista.'''
    while True:
        nombre = input("Ingrese el Nombre del piloto: ").upper()
        if " " not in nombre:
            print("Error: debe ingresar nombre y apellido.")
        elif nombre in nombres:
            print("Error: ya existe un piloto con ese nombre.")
        else:
            return nombre

def pedirNumeroNuevo(numero_identificatorio):
    '''Pide un numero identificatorio positivo y unico.
    Repite si ya existe en la lista.'''
    numero = ingresarPositivo("Ingrese el numero identificatorio del piloto: ")
    while numero in numero_identificatorio:
        print("Error: ya existe un piloto con ese numero identificatorio.")
        numero = ingresarPositivo("Ingrese el numero identificatorio del piloto: ")
    return numero

def pedirEscuderia():
    '''Pide una escuderia valida. Repite si esta vacia o no pertenece a la lista.'''
    escuderias_validas = ["MCLAREN", "FERRARI", "MERCEDES", "RED BULL RACING", "ASTON MARTIN",
                          "ALPINE", "WILLIAMS", "RACING BULLS", "HAAS", "AUDI", "CADILLAC"]
    escu = input("Ingrese la escuderia del piloto: ").upper()
    while escu == "" or escu not in escuderias_validas:
        if escu == "":
            print("Error: la escuderia no puede quedar vacia.")
        else:
            print("Error: la escuderia no es valida.")
        escu = input("Ingrese la escuderia del piloto: ").upper()
    return escu

# Subfunciones de eliminarPiloto
def pedirNumeroAEliminar():
    '''Solicita y retorna el numero identificatorio del piloto a eliminar.'''
    return ingresarPositivo("Ingrese el numero identificatorio del piloto a eliminar: ")

def validarEliminacion(nombres, puntos_acumulados, indice):
    '''Verifica que el piloto tenga 0 puntos. Retorna True si se puede eliminar.'''
    if puntos_acumulados[indice] != 0:
        print("Error: no se puede eliminar a un piloto con puntos acumulados.")
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

# Subfunciones de informeGeneral 
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
    print("=" * 95)
    print(f"{'POS':<5} {'PILOTO':<22} {'N':<5} {'ESCUDERIA':<20} {'PUNTOS':>7} {'T.PROM(s)':>10} {'PRESUPUESTO':>13} {'ABAND.':>7}")
    print("-" * 95)
    pos = 1
    for i in indices:
        print(f"{pos:<5} {nombres[i]:<22} {num_identificatorio[i]:<5} {escuderia[i]:<20} {puntos_acumulados[i]:>7} {tiempo_promedio[i]:>10.2f} ${presupuesto_asignado[i]:>12,.0f} {abandonos[i]:>7}")
        pos = pos + 1
    print("=" * 95)
