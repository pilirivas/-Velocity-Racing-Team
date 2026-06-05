# Velocity Racing Team - Sistema de Gestión Deportiva

## Descripción
En este codigo dearrollado en Python, se permite administrar información sobre pilotos de Formula 1. Permite registrar, modificar, eliminar y visualizar datos de pilotos mediante un menú de opciones.

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
