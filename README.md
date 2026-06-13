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

FAuna es una aplicación de consola en Python que permite trabajar con Autómatas Finitos Deterministas (DFA). A partir de un archivo JSON que define el autómata, el programa puede:

- **Visualizar** el DFA como imagen PNG usando Graphviz.
- **Ejecutar** (run) el DFA con una cadena de entrada, mostrando cada transición (tracing).
- **Analizar** el DFA: verificar completitud, encontrar estados inalcanzables y estados inútiles.
- **Compilar** un DFA extendido (con expresiones regulares en transiciones) a un DFA estándar.

El modelo es totalmente propio (sin automata-lib para la lógica) e implementado con POO en Python 3.13.

---

## Estructura del Proyecto

    fauna/
    ├── src/dfa/
    │   ├── model.py        # Clases State, Transition, DFA
    │   ├── runner.py       # Ejecucion con tracing
    │   ├── analysis.py     # Completitud, inalcanzables, inutiles
    │   ├── compiler.py     # Compilador DFA extendido -> estandar
    │   └── fauna_main.py   # CLI principal (view, run, analize, compile)
    ├── tests/
    │   ├── test_model.py
    │   ├── test_runner.py
    │   ├── test_analyser.py
    │   ├── test_visualization.py
    │   ├── test_compilation.py
    │   └── test_performance.py
    ├── docs/
    │   ├── sprint_1_spec.md
    │   └── sprint_2_spec.md
    ├── html/
    ├── examples/
    ├── README.md
    ├── requirements.txt
    └── .gitignore

---

## Instalación

1. Asegurarse de tener Python 3.13.x instalado:

       python --version

2. Crear un entorno virtual:

       python -m venv venv

3. Activar el entorno virtual:

       venv\Scripts\activate

4. Instalar dependencias:

       pip install -r requirements.txt

5. Instalar Graphviz desde su página oficial y agregar al PATH.

---

## Ejecución

### Comandos disponibles

El programa acepta 4 comandos: `view`, `run`, `analize` y `compile`.  Todos los comandos se ejecutan desde la raíz del proyecto.

**Visualizar un DFA (genera PNG):**

    python src\dfa\fauna_main.py view --format png examples\contador_hola.json

**Ejecutar un DFA con una cadena:**

    python src\dfa\fauna_main.py run --input hola examples\contador_hola.json

Muestra cada transición (tracing) e indica si la cadena es ACEPTADA o RECHAZADA.

**Analizar completitud:**

    python src\dfa\fauna_main.py analize --complete examples\contador_hola.json

**Ver estados inalcanzables:**

    python src\dfa\fauna_main.py analize --unreachable examples\contador_hola.json

**Ver estados inútiles:**

    python src\dfa\fauna_main.py analize --useless examples\contador_hola.json

**Compilar un DFA extendido a estándar:**

    python src\dfa\fauna_main.py compile examples\dfa_extendido.json --o examples\dfa_compilado.json

---

## Expresiones regulares soportadas en transiciones

| Expresión | Descripción                        |
|-----------|------------------------------------|
| .         | Cualquier carácter del vocabulario |
| \d        | Dígitos 0-9                        |
| \s        | Espacios en blanco                 |
| \w        | Letras a-z y A-Z                   |
| [a-z]     | Rango de caracteres                |
| [^a-z]    | Negación de rango                  |
| x\|y      | Unión de dos expresiones           |

---

## Pruebas

Ejecutar todos los tests desde la raíz del proyecto:

    python -m unittest discover tests

O individualmente:

    python -m unittest tests.test_model
    python -m unittest tests.test_runner
    python -m unittest tests.test_analyser
    python -m unittest tests.test_visualization
    python -m unittest tests.test_compilation
    python -m unittest tests.test_performance

---

## Librerías externas

- **graphviz**: Generación de visualizaciones PNG del DFA.
- **argparse**: Manejo de comandos y opciones (librería estándar de Python).
- **logging**: Tracing durante la ejecución (librería estándar de Python).

No se utiliza automata-lib ni ninguna otra librería externa para la lógica del DFA.

---

## Declaración Jurada de uso de IA

Se utilizó inteligencia artificial como apoyo para el desarrollo de los siguientes aspectos del SPEC:

- Orientación sobre la distribución del código entre los distintos archivos del proyecto (model.py, runner.py, fauna_main.py, etc.), de acuerdo a la estructura solicitada en el SPEC.
- Corrección de errores y dudas puntuales durante la implementación.
- Corrección del algoritmo BFS para unreachable_states y useless_states en analysis.py.
- Generación de test_analyser.py, test_performance.py y docs/sprint_2_spec.md.

El código fue totalmente comprendido por los integrantes del grupo y son capaces de defender la composición del mismo.
