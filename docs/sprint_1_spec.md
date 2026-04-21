# Sprint 1 - Especificación del Proyecto DFA

## Curso
EIF203 Estructuras Discretas - Semestre I, 2026  
Universidad Nacional

## Integrantes
- Adrian Muñoz Cisneros
- Marco Vinicio Coto Dall' Anesse
- Gabriel Chavarria Barquero
- Joao Arauz Rodriguez

---

## Descripción del Sprint

En este sprint se desarrolló la base del proyecto para trabajar con autómatas finitos deterministas (DFA).  
El sistema permite leer la definición de un DFA desde un archivo JSON, construir su modelo en memoria y generar una representación gráfica en formato PNG utilizando Graphviz.

---

## Funcionalidades Implementadas

- Lectura de archivos JSON con la definición de un DFA
- Creación de clases usando Programación Orientada a Objetos:
  - `State`
  - `Transition`
  - `DFA`
- Ejecución de cadenas sobre el DFA (`runner.py`)
- Generación de representación gráfica del DFA (`Graphviz`)
- Interfaz de ejecución desde consola (`fauna_main.py`)

---

## Pruebas

Se implementaron pruebas unitarias básicas para validar el funcionamiento del sistema:

- `test_model.py`: Verifica la correcta creación de objetos (`State`, `Transition`, `DFA`)
- `test_runner.py`: Valida la ejecución del DFA con cadenas aceptadas y rechazadas
- `test_visualization.py`: Verifica la generación correcta del archivo PNG

---

## Estructura del Proyecto
```
fauna-main/
│
├── src/dfa/
│ ├── fauna_main.py
│ ├── model.py
│ ├── runner.py
│ ├── analysis.py
│ ├── compiler.py
│
├── examples/
│ ├── dfa2.json
│ ├── dfa2.png
│
├── tests/
│ ├── test_model.py
│ ├── test_runner.py
│ ├── test_visualization.py
│
├── docs/
│ └── sprint_1_spec.md
│
├── README.md
└── requirements.txt
```

---

## Observaciones

Algunos módulos (`analysis.py`, `compiler.py`) fueron incluidos como parte de la arquitectura del sistema, pero su implementación completa se desarrollará en futuros sprints.

---

## Conclusión

El Sprint 1 cumple con los objetivos planteados, proporcionando una base funcional para la representación y ejecución de autómatas DFA, así como su visualización gráfica.
