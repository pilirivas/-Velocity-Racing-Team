# Velocity Racing Team - Sistema de Gestión Deportiva

## Repositorio
https://github.com/pilirivas/-Velocity-Racing-Team

## Descripción
Sistema desarrollado en Python que permite administrar información sobre pilotos de Fórmula 1. Permite registrar, modificar, eliminar y visualizar datos de pilotos y escuderías mediante un menú interactivo con colores en consola.

## Alcance
El sistema centraliza y administra la información deportiva de los pilotos de una escudería de Fórmula 1. A través de un menú interactivo, el usuario puede:

- Registrar nuevos pilotos ingresando sus datos por teclado.
- Eliminar pilotos con cero puntos acumulados, con confirmación previa.
- Modificar los puntos acumulados de un piloto existente.
- Visualizar un informe general con todos los pilotos ordenados por puntos.
- Gestionar escuderías: agregar, eliminar y modificar escuderías y sus sponsors.
- Visualizar un informe de carreras con los días restantes para cada una, calculados automáticamente desde la fecha del sistema.

Para cada piloto se administra: nombre, número identificatorio del monoplaza, escudería, puntos acumulados, tiempo promedio por vuelta, presupuesto asignado y cantidad de abandonos en la temporada.

Para cada escudería se administra: nombre, país de origen y sponsors.

Esta entrega corresponde a la Fase 2 del proyecto: versión con gestión de escuderías, informe de carreras, colores en consola y robustez ante errores de ingreso.

## Integrantes
- Pilar Rivas
- Valentina Méndez
- Martina Medina

## Materia
Pensamiento Computacional, Algoritmos y Programación

## Archivos
- `main.py` — archivo principal, contiene los datos iniciales y el flujo del menú
- `Funciones.py` — contiene las funciones principales del sistema
- `subfunciones.py` — contiene las funciones auxiliares, de validación y de soporte

## Cómo ejecutar
1. Asegurarse de tener Python instalado
2. Colocar `main.py`, `Funciones.py` y `subfunciones.py` en la misma carpeta
3. Ejecutar `main.py`

## Opciones del menú
1. **Alta de Piloto** — registra un nuevo piloto ingresando todos sus datos por teclado
2. **Eliminar Piloto** — elimina un piloto buscándolo por número identificatorio (solo si tiene 0 puntos)
3. **Modificar Puntos** — modifica los puntos acumulados de un piloto buscándolo por número identificatorio
4. **Informe General** — muestra todos los pilotos en una tabla ordenada de mayor a menor por puntos. En caso de empate, de menor a mayor por tiempo promedio
5. **Gestión de Escuderías** — permite ver, agregar, eliminar y modificar escuderías y la escudería asignada a un piloto
6. **Informe de Carreras** — muestra los circuitos, países y fechas de las carreras con los días restantes calculados automáticamente
7. **Salir** — finaliza el programa

## Validaciones implementadas
- El nombre debe tener nombre y apellido (dos palabras)
- El número identificatorio debe ser positivo y no puede repetirse
- La escudería debe pertenecer a las escuderías registradas en el sistema
- Los puntos y abandonos aceptan 0 o positivos (no negativos)
- El tiempo promedio y presupuesto aceptan decimales no negativos
- Solo se pueden eliminar pilotos con 0 puntos acumulados
- Se solicita confirmación antes de eliminar un piloto
- El programa no se interrumpe ante ingresos incorrectos: informa el error y vuelve a pedir el dato
- Al eliminar una escudería con pilotos asignados, se solicita confirmación para darlos de baja también
- Cada escudería debe tener al menos un sponsor y no se permiten sponsors repetidos
- El nombre de la escudería y el país de origen no pueden quedar vacíos al agregar una nueva

## Autoría por archivo
- **subfunciones.py**
  - Valentina Méndez: `ROJO`, `VERDE`, `NORMAL`, `ingresarPositivo`, `ingresarNoNegativo`, `ingresarNoNegativoFloat`, `pedirNombre`, `pedirNumeroNuevo`, `calcularDiasRestantes`, `imprimirTablaCarreras`
  - Pilar Rivas: `pedirNumeroAEliminar`, `validarEliminacion`, `confirmarEliminacion`, `borrarPilotoDeListas`, `crearIndices`, `ordenarIndicesPorPuntosYTiempo`, `imprimirTabla`
  - Martina Medina: `esDecimalValido`, `buscarPorNumero`, `pedirEscuderia`, `pedirSponsors`, `subMenuEscuderias`, `escuderiasDisponibles`, `agregarEscuderia`, `eliminarEscuderia`, `modificarEscuderiaPiloto`, `buscarPorEscuderia`

- **Funciones.py**
  - Valentina Méndez: `opciones_menu`, `informeCarreras`
  - Pilar Rivas: `ingresar_opcionMenu`, `altaPiloto`, `eliminarPiloto`, `informeGeneral`
  - Martina Medina: `modificarPuntos`, `gestionEscuderias`

- **main.py**
  - Valentina Méndez: datos de circuitos, países y fechas; opción 6 (Informe de Carreras)
  - Pilar Rivas: flujo del while principal; opciones 1 (Alta de Piloto), 2 (Eliminar Piloto), 4 (Informe General)
  - Martina Medina: inicialización de listas de pilotos y escuderías, función `main`; opciones 3 (Modificar Puntos), 5 (Gestión de Escuderías)

## Fase
Entrega Fase 2 — Versión con gestión de escuderías, informe de carreras, colores e interfaz robusta

