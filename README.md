# Velocity Racing Team - Sistema de Gestión Deportiva

## Repositorio
https://github.com/pilirivas/-Velocity-Racing-Team

## Descripción
En este codigo desarrollado en Python, se permite administrar información sobre pilotos de Formula 1. Permite registrar, modificar, eliminar y visualizar datos de pilotos mediante un menú de opciones.

## Alcance
El sistema permite centralizar y administrar la información deportiva de los pilotos de una escudería de Fórmula 1. A través de un menú interactivo, el usuario puede:

- Registrar nuevos pilotos (alta) ingresando sus datos por teclado.
- Eliminar pilotos (baja) que tengan cero puntos acumulados, con confirmación previa.
- Modificar los puntos acumulados de un piloto existente.
- Visualizar un informe general con todos los pilotos ordenados por puntos.

Para cada piloto se administra: nombre, número identificatorio del monoplaza, escudería, puntos acumulados, tiempo promedio por vuelta, presupuesto asignado y cantidad de abandonos en la temporada.

Esta entrega corresponde a la Fase 1 del proyecto: versión inicial con gestión básica y visualización de datos.

## Integrantes
- Pilar Rivas
- Valentina Méndez
- Martina Medina

## Materia
Pensamiento Computacional, Algoritmos y Programación

## Archivos
- `main.py` — archivo principal, contiene los datos iniciales y el menú
- `Funciones.py` — contiene todas las funciones del sistema

## Cómo ejecutar
1. Asegurarse de tener Python instalado
2. Colocar `main.py` y `Funciones.py` en la misma carpeta
3. Ejecutar `main.py`

## Opciones del menú
1. **Alta de Piloto** — registra un nuevo piloto ingresando todos sus datos por teclado
2. **Eliminar Piloto** — elimina un piloto buscándolo por número identificatorio (solo si tiene 0 puntos)
3. **Modificar Puntos** — modifica los puntos acumulados de un piloto buscándolo por número identificatorio
4. **Informe General** — muestra todos los pilotos en una tabla ordenada de mayor a menor por puntos. En caso de empate, de menor a mayor por tiempo promedio
5. **Salir** — finaliza el programa

## Validaciones implementadas
- El nombre debe tener nombre y apellido (dos palabras)
- El número identificatorio debe ser positivo y no puede repetirse
- La escudería debe ser una de las escuderías válidas de la temporada y no puede quedar vacia
- Los puntos y abandonos aceptan 0 o positivos (no negativos)
- El tiempo promedio y presupuesto aceptan decimales no negativos
- Solo se pueden eliminar pilotos con 0 puntos acumulados
- Se solicita confirmación antes de eliminar un piloto



## Fase
Entrega Fase 1 — Versión inicial del producto
