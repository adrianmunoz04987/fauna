# Proyecto DFA - FAuna

## Curso
EIF 203 - Estructuras Discretas
Universidad Nacional (UNA)
Semestre I, 2026

## Integrantes
- Adrian Muñoz Cisneros
- Marco Vinicio Coto Dall' Anesse
- Gabriel Chavarria Barquero
- Joao Arauz Rodriguez

---

## Descripción

En este proyecto se desarrolló una aplicación de consola de Python, consiste en un programa que permite leer un autómata finito determinista (DFA) desde un archivo en formato JSON y generar una representación gráfica en formato PNG.

El programa procesa: 
- Los estados.
- El estado inicial.
- Los estados de aceptación.
- Las transiciones.

Luego construye el autómata utilizando Graphviz.

---
## Estructura del Proyecto
```
fauna/
├── src/dfa/
│   ├── model.py        # Representación del DFA
│   ├── runner.py       # Lógica de ejecución
│   ├── analysis.py     # Funciones básicas de análisis
│   ├── compiler.py     # Procesamiento del autómata
│   └── fauna_main.py   # Archivo principal
├── examples/           # Ejemplos de DFAs en JSON
├── tests/              # Pruebas del sistema
├── docs/               # Documentación del sprint
├── html/               # Documentación generada
├── README.md
├── requirements.txt
└── .gitignore
```
---

## Cómo ejecutar

Descargar el proyecto y asegurarse de tener la carpeta fauna en tu computadora.

Abrir el cmd y entrar a la ruta de la carpeta.
  cd C:\Users\...\...\fauna-main

## Instalación
1. Crear un entorno virtual
   python -m venv venv

2. Activar el entorno virtual
   venv\Scripts\activate

3. Instalar dependencias
   pip install -r requirements.txt

4. Instalar Graphviz
   Descargar e instalar Graphviz desde su página oficial.

## Ejecución

Desde la raíz del proyecto ejecutar
  python src\dfa\fauna_main.py examples\dfa2.json

## Resultado

Si la ejecución es correcta, se debe generar un archivo .png en la carpeta examples con la visualizacion del autómata.

### Uso de herramientas externas e IA

### Librerías externas
- graphviz: utilizada para generar la representación gráfica del DFA en formato PNG.

### Uso de inteligencia artificial
Se utilizo inteligenci artificial como apoyo para el desarrollo de los siguientes aspectos del SPEC:

- Orientación sobre la distribución del código entre los distintos archivos del proyecto (`model.py`, `runner.py`, `fauna_main.py`, etc.), de acuerdo a la estructura solicitada en el SPEC.
- Corrección de errores y dudas puntuales durante la implementación.

El codigo fue totalmente comprendido por los integrantes del grupo y son capaces de defender la composicion del mismo.
