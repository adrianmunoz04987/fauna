# Proyecto DFA - FAuna

## Curso
Estructuras Discretas

## Integrantes
- Adrian Muñoz Cisneros
- Marco Vinicio Coto Dall' Anesse
- Gabriel Chavarria Barquero
- Joao Arauz Rodriguez

---

## Descripción

Este proyecto consiste en crear un programa que permite leer un autómata finito determinista (DFA) desde un archivo JSON y generar una imagen que lo represente.

El programa toma los estados, el estado inicial, los estados de aceptación y las transiciones, y luego construye el autómata utilizando Graphviz.

---

## Cómo ejecutar

Cómo ejecutar
Descargar o abrir el proyecto
Asegúrate de tener la carpeta fauna en tu computadora.
Abrir la carpeta en la terminal
Puedes abrir la carpeta y escribir cmd en la barra para abrir la terminal directamente ahí.
Crear el entorno virtual
python -m venv venv

Activar el entorno
venv\Scripts\activate

Instalar dependencias
pip install -r requirements.txt

Instalar Graphviz (importante)
Descargar e instalar Graphviz desde su página oficial.

Si da error, agregar esta línea al inicio de fauna_main.py:
import os
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

Ejecutar el programa
python src\dfa\fauna_main.py examples\dfa2.json
