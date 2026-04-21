# Especificación del formato JSON para DFA

Curso: EIF203 Estructuras Discretas - Semestre I, 2026  
Universidad Nacional

Autores:
- Adrian Muñoz Cisneros
- Marco Vinicio Coto Dall' Anesse
- Gabriel Chavarria Barquero
- Joao Arauz Rodriguez

## Descripción general

Este documento describe el formato JSON que usa FAuna para representar un Autómata Finito Determinista (DFA). Cada archivo JSON contiene un único DFA.

### name
Nombre del DFA. Es una cadena de texto que se usa para identificarlo.

Ejemplo: `"name": "ends_ab"`

### alphabet
Lista de símbolos válidos que el DFA puede leer. Cada símbolo es un arco corto, usualmente de un solo carácter.

Ejemplo: `"alphabet": ["a", "b"]`

### start_state
Identificador del estado inicial del DFA.

Ejemplo: `"start_state": "q0"`

### states
Lista de estados del DFA. Cada estado es un objeto con dos campos:

- `id`: identificador único del estado (cadena de texto).
- `accepting`: `true` si es estado de aceptación, `false` si no lo es.

Ejemplo:
"states": [
{"id": "q0", "accepting": false},
{"id": "q1", "accepting": false},
{"id": "q2", "accepting": true}
]

### transitions
Lista de transiciones entre estados. Cada transición es un objeto con
tres campos:

- `from`: id del estado de origen.
- `symbol`: símbolo del alfabeto que causa la transición.
- `to`: id del estado de destino.

Ejemplo:
"transitions": [
{"from": "q0", "symbol": "a", "to": "q1"},
{"from": "q0", "symbol": "b", "to": "q0"}
]

