# ============================================
# Proyecto: Velocity Racing Team - TPO
# Materia: Pensamiento Computacional, Algoritmia y Programación
# Equipo 06
# Integrantes: Pilar Rivas, Martina Medina, Valentina Mendez
# Autoría: El equipo trabajó de forma colaborativa. No se dividieron tareas por función ni por módulo.
# ============================================

def ingresarPositivo(msg):
    '''Pide un entero por teclado y valida que sea positivo (> 0).
    Repite hasta recibir un valor valido y lo retorna.'''
    num = input(msg) # no usamos int() porque .isdigit() solol funciona con texto
    while not num.isdigit() or int(num) <= 0:
        print("Error debe ser positivo")
        num =input(msg)
    return int(num)


def ingresarNoNegativo(msg):
    '''Pide un entero por teclado y valida que no sea negativo (acepta 0).
    Repite hasta recibir un valor valido y lo retorna.'''
    num = input(msg)
    while not num.isdigit(): #no hace falta especifiar el or num<0 porque el - en un numero negativo ya no es un digito
        print("Error debe ser positivo o cero")
        num = input(msg)
    return int(num)


def ingresarNoNegativoFloat(msg):
    '''Pide un decimal por teclado y valida que no sea negativo (acepta 0).
    Repite hasta recibir un valor valido y lo retorna.'''
    num = float(input(msg))
    while num < 0:
        print("Error debe ser positivo o cero")
        num = float(input(msg))
    return num


def buscarPorNumero(numero_identificatorio, numero_buscado):
    '''Busqueda SECUENCIAL desarrollada manualmente.
    Recorre la lista de numeros uno por uno y retorna el indice donde
    encuentra una coincidencia. Si recorre toda la lista sin encontrarlo,
    retorna -1. Ese indice sirve para acceder al mismo piloto en todas
    las listas paralelas (estan relacionadas por posicion).'''
    for i in range(len(numero_identificatorio)):
        if numero_identificatorio[i] == numero_buscado:
            return i  # encontrado: devuelvo la posicion
    return -1  # no se encontro el piloto


def escuderias():
    '''Retorna la lista de escuderias validas de la temporada.
    Se usa para validar que la escuderia ingresada exista.'''
    lista = ["MCLAREN", "FERRARI", "MERCEDES", "RED BULL RACING", "ASTON MARTIN",
             "ALPINE", "WILLIAMS", "RACING BULLS", "HAAS", "AUDI", "CADILLAC"]
    return lista


def opciones_menu():
    '''Muestra por pantalla las opciones del menu principal.
    Solo imprime: no procesa datos (responsabilidad separada).'''
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
    '''Pide una opcion del menu y valida que este dentro del rango
    [desde, hasta]. Repite hasta recibir un valor valido y lo retorna.'''
    op = int(input("Seleccione una opcion:"))
    while op.isdigit() or int(op) < desde or int(op) > hasta:
        print("La opcion seleccionada no es valida")
        op = input("Seleccione una opcion:")
    return int(op)


def altaPiloto(nombres, numero_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos):
    '''Da de alta a un piloto. Recibe las listas paralelas donde se
    almacenan los datos. Valida cada campo antes de agregarlo y recien
    al final hace el append a todas las listas (asi no quedan datos
    "a medias" si una validacion falla).'''
    # Nombre: debe contener nombre y apellido (al menos un espacio).
    while True:
        nombre = input("Ingrese el Nombre del piloto: ").upper()
        if " " in nombre:
            break
        print("Error: debe ingresar nombre y apellido.")

    # Numero: debe ser positivo y no estar repetido en la lista.
    numero = ingresarPositivo("Ingrese el numero identificatorio del piloto: ")
    while numero in numero_identificatorio:
        print("Error: ya existe un piloto con ese numero identificatorio. Ingrese todos los datos nuevamente.")
        while True:
            nombre = input("Ingrese el Nombre del piloto: ").upper()
            if " " in nombre:
                break
            print("Error: debe ingresar nombre y apellido.")
        numero = ingresarPositivo("Ingrese el numero identificatorio del piloto: ")

    # Escuderia: no puede quedar vacia y debe pertenecer a la lista valida.
    escu = input("Ingrese la escuderia del piloto: ").upper()
    while escu == "" or escu not in escuderias():
        if escu == "":
            print("Error: la escuderia no puede quedar vacia.")
        elif escu not in escuderias():
            print("Error: la escuderia no es valida.")
        escu = input("Ingrese la escuderia del piloto: ").upper()

    # Resto de los campos numericos, cada uno con su validacion.
    puntos = ingresarNoNegativo("Ingrese los puntos acumulados del piloto: ")
    tiempo = ingresarNoNegativoFloat("Ingrese el tiempo promedio del piloto: ")
    presupuesto = ingresarNoNegativoFloat("Ingrese el presupuesto asignado al piloto: ")
    aband = ingresarNoNegativo("Ingrese el numero de abandonos del piloto: ")

    # Se agregan todos los datos juntos al final, manteniendo el mismo
    # indice en todas las listas paralelas (relacion por posicion).
    nombres.append(nombre)
    numero_identificatorio.append(numero)
    escuderia.append(escu)
    puntos_acumulados.append(puntos)
    tiempo_promedio.append(tiempo)
    presupuesto_asignado.append(presupuesto)
    abandonos.append(aband)


def informeGeneral(nombres, num_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos):
    '''Muestra los pilotos en formato de tabla, ordenados de mayor a menor
    por puntos. Ante empate, de menor a mayor por tiempo promedio.
    El orden se calcula con ORDENAMIENTO POR SELECCION desarrollado a mano,
    ordenando una lista de indices para no desarmar las listas paralelas.'''
    # Armo una lista de indices [0, 1, 2, ...] que voy a reordenar.
    # Ordeno indices (no los datos) para que las listas paralelas
    # sigan alineadas entre si.
    indices = []
    for i in range(len(nombres)):
        indices.append(i)

    # Ordenamiento por seleccion: en cada pasada busco el "mejor" y lo
    # llevo al frente. Criterio: mas puntos primero; si empatan, menor tiempo.
    for i in range(len(indices)):
        mejor = i
        for j in range(i + 1, len(indices)):
            if puntos_acumulados[indices[j]] > puntos_acumulados[indices[mejor]]:
                mejor = j
            elif puntos_acumulados[indices[j]] == puntos_acumulados[indices[mejor]]:
                # empate en puntos: gana el de menor tiempo promedio
                if tiempo_promedio[indices[j]] < tiempo_promedio[indices[mejor]]:
                    mejor = j
        # intercambio (swap) la posicion i con la del mejor encontrado
        aux = indices[i]
        indices[i] = indices[mejor]
        indices[mejor] = aux

    # Impresion de la tabla recorriendo los indices ya ordenados.
    print()
    print("=" * 95)
    print(f"{'POS':<5} {'PILOTO':<22} {'N':<5} {'ESCUDERIA':<20} {'PUNTOS':>7} {'T.PROM(s)':>10} {'PRESUPUESTO':>13} {'ABAND.':>7}")
    print("-" * 95)
    pos = 1
    for i in indices:
        print(f"{pos:<5} {nombres[i]:<22} {num_identificatorio[i]:<5} {escuderia[i]:<20} {puntos_acumulados[i]:>7} {tiempo_promedio[i]:>10.2f} ${presupuesto_asignado[i]:>12,.0f} {abandonos[i]:>7}")
        pos = pos + 1
    print("=" * 95)


def eliminarPiloto(nombres, numero_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos):
    '''Elimina un piloto buscado por su numero identificatorio.
    Solo se permite si tiene 0 puntos, y pide confirmacion antes de borrar.
    Usa el mismo indice para sacar al piloto de TODAS las listas paralelas.'''
    numeroEliminar = ingresarPositivo("Ingrese el numero identificatorio del piloto a eliminar: ")
    indice = buscarPorNumero(numero_identificatorio, numeroEliminar)
    if indice != -1:
        # Regla del negocio: solo se puede eliminar si tiene 0 puntos.
        if puntos_acumulados[indice] != 0:
            print("Error: no se puede eliminar a un piloto con puntos acumulados.")
            return
        # Confirmacion antes de eliminar (operacion irreversible).
        confirmacion = input("Confirma que desea eliminar a '" + nombres[indice] + "'? (s/n): ").lower()
        if confirmacion == "s":
            # Se elimina la misma posicion en todas las listas paralelas.
            nombres.pop(indice)
            numero_identificatorio.pop(indice)
            escuderia.pop(indice)
            puntos_acumulados.pop(indice)
            tiempo_promedio.pop(indice)
            presupuesto_asignado.pop(indice)
            abandonos.pop(indice)
            print("Piloto eliminado exitosamente.")
        else:
            print("Operacion cancelada.")
    else:
        print("No se encontro un piloto con ese numero identificatorio.")


def modificarPuntos(nombres, numero_identificatorio, escuderia, puntos_acumulados, tiempo_promedio, presupuesto_asignado, abandonos):
    '''Modifica los puntos acumulados de un piloto buscado por su numero.
    Reemplaza el valor en la posicion encontrada por la busqueda secuencial.'''
    numeroModificar = ingresarPositivo("Ingrese el numero identificatorio del piloto para modificar sus puntos: ")
    indice = buscarPorNumero(numero_identificatorio, numeroModificar)
    if indice != -1:
        nuevosPuntos = ingresarNoNegativo("Ingrese los nuevos puntos acumulados del piloto: ")
        puntos_acumulados[indice] = nuevosPuntos  # reemplaza los puntos en la posicion encontrada
        print("Puntos acumulados del piloto modificados exitosamente.")
    else:
        print("No se encontro un piloto con ese numero identificatorio.")
