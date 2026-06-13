# Sprint 02 - FAuna

## Curso
EIF203 - Estructuras Discretas
Universidad Nacional (UNA)
Semestre I, 2026

## Integrantes
- Adrian Muñoz Cisneros
- Marco Vinicio Coto Dall' Anesse
- Gabriel Chavarria Barquero
- Joao Arauz Rodriguez

---

## Objetivo del Sprint 02

Evolucionar el proyecto FAuna añadiendo sobre el modelo propio del Sprint 01:

1. **Modelo propio sin automata-lib** para la lógica del DFA.
2. **Transiciones extendidas (SRE)**: `.`, `|`, `[a-z]`, `[^a-z]`, `\d`, `\s`, `\w`.
3. **Compiler**: convierte DFA extendido en DFA estándar.
4. **Analyser**: completitud, estados inalcanzables, estados inútiles.
5. **Runner con tracing**: muestra cada transición al ejecutar.
6. **Nuevo main con comandos**: `run`, `view`, `analize`, `compile`.

---

## Comandos disponibles

Para visualizar un DFA:

    python src\dfa\fauna_main.py view --format png examples\contador_hola.json

Para ejecutar con una cadena:

    python src\dfa\fauna_main.py run --input hola examples\contador_hola.json

Para analizar completitud:

    python src\dfa\fauna_main.py analize --complete examples\contador_hola.json

Para ver estados inalcanzables:

    python src\dfa\fauna_main.py analize --unreachable examples\contador_hola.json

Para ver estados inútiles:

    python src\dfa\fauna_main.py analize --useless examples\contador_hola.json

Para compilar un DFA extendido:

    python src\dfa\fauna_main.py compile examples\dfa_extendido.json --o examples\dfa_compilado.json

---

## Estructura del entregable

    fauna/
    ├── src/dfa/
    │   ├── model.py
    │   ├── runner.py
    │   ├── analysis.py
    │   ├── compiler.py
    │   └── fauna_main.py
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
    └── requirements.txt

---

## Librerias autorizadas

- `graphviz`: visualizaciones PNG.
- `argparse`: manejo de comandos (stdlib).
- `logging`: tracing en runner (stdlib).

No se utiliza automata-lib ni ninguna otra libreria externa para la logica del DFA.

---

## Criterios cubiertos en este sprint

- Modelo OOP propio sin dependencias externas para la logica.
- Transiciones con expresiones regulares simples (SRE).
- Compilacion de DFA extendido a DFA estandar.
- Analisis de completitud, estados inalcanzables y estados inutiles con BFS.
- Runner con tracing de cada transicion.
- CLI con argparse: comandos view, run, analize, compile.
- Casos de prueba para cada funcionalidad.
- Documentacion Sphinx en carpeta html/.
