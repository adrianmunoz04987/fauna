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

1. Descargar el proyecto y asegurarse de tener la carpeta fauna en tu computadora.

2. Abrir el cmd y entrar a la ruta de la carpeta.  
   cd C:\Users\...\...\fauna-main

3. Asegurarse de tener Python 3.13.x instalado. Para verificar:
   python --version

## Instalación

1. Crear un entorno virtual  
   python -m venv venv

2. Activar el entorno virtual  
   venv\Scripts\activate

3. Instalar dependencias  
   pip install -r requirements.txt

4. Instalar Graphviz  
   Descargar e instalar Graphviz desde su página oficial.

5. Versión de Python recomendada: 3.13.x (requerida según el SPEC del curso)

## Ejecución

Desde la raíz del proyecto ejecutar  
  python src\dfa\fauna_main.py examples\contador_hola.json

Para ejecutar una cadena sobre el DFA, se agrega como segundo argumento:  
python src\dfa\fauna_main.py examples\contador_hola.json 

El programa genera la imagen y además indica si la cadena es ACEPTADA o RECHAZADA.

## Pruebas

Para correr las pruebas unitarias, desde la raíz del proyecto:  
python -m unittest tests.test_model  
python -m unittest tests.test_runner

## Resultado

Si la ejecución es correcta, se debe generar un archivo .png en la carpeta examples con la visualizacion del autómata.

---

### Librerías externas
- Graphviz: Utilizada para generar la representación gráfica del DFA en formato PNG.

---

### Declaración Jurada de uso de IA
Se utilizó inteligencia artificial como apoyo para el desarrollo de los siguientes aspectos del SPEC:

- Orientación sobre la distribución del código entre los distintos archivos del proyecto (`model.py`, `runner.py`, `fauna_main.py`, etc.), de acuerdo a la estructura solicitada en el SPEC.
- Corrección de errores y dudas puntuales durante la implementación.

El código fue totalmente comprendido por los integrantes del grupo y son capaces de defender la composición del mismo.
