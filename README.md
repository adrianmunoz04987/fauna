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

1. Descargar o abrir el proyecto

Primero asegúrate de tener la carpeta del proyecto (fauna) en tu computadora.

2. Abrir la carpeta en la terminal

Puedes abrir la carpeta y en la barra escribir cmd para abrir la terminal directamente ahí.

3. Crear el entorno virtual
python -m venv venv
4. Activar el entorno
venv\Scripts\activate
5. Instalar dependencias
pip install -r requirements.txt
6. Instalar Graphviz (importante)

Además de lo anterior, hay que instalar Graphviz en la computadora.
Si no, el programa no va a poder generar la imagen.
