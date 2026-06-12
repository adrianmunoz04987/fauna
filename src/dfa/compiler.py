"""
EIF203 Estructuras Discretas - Semestre I, 2026
Universidad Nacional

Autores:
   Adrian Muñoz Cisneros
   Marco Vinicio Coto Dall' Anesse
   Gabriel Chavarria Barquero
   Joao Arauz Rodriguez

Modulo que implementa el compilador de DFA extendido a DFA estandar.
"""

import json
try:
    from src.dfa.model import DFA, Transition
except ModuleNotFoundError:
    from model import DFA, Transition

VOCABULARIO = (
        [chr(c) for c in range(ord('a'), ord('z')+1)] +
        [chr(c) for c in range(ord('A'), ord('Z')+1)] +
        [str(d) for d in range(10)] +
        [' ', '\t', '\n', '.', '\\', '[', ']', '-', '^']
)

def parse_sre(V: list, input: str) -> list:
    """
    Parsea una expresion regular simple (SRE) y devuelve la lista de caracteres que representa.

    :param V: Vocabulario de caracteres validos.
    :type V: list
    :param input: La expresion regular a parsear.
    :type input: str
    :returns: Lista de caracteres que la SRE denota.
    :rtype: list
    """
    if '|' in input:
        partes = input.split('|')
        resultado = []
        for parte in partes:
            for c in parse_sre(V, parte):
                if c not in resultado:
                    resultado.append(c)
        return resultado

    if input == '.':
        return list(V)

    if input == '\\d':
        return [str(d) for d in range(10)]
    if input == '\\s':
        return [' ', '\t', '\n']
    if input == '\\w':
        return [chr(c) for c in range(ord('a'), ord('z')+1)] + \
            [chr(c) for c in range(ord('A'), ord('Z')+1)]

    if input.startswith('[^') and '-' in input:
        inicio = input[2]
        fin = input[4]
        excluidos = [chr(c) for c in range(ord(inicio), ord(fin)+1)]
        return [c for c in V if c not in excluidos]

    if input.startswith('[') and '-' in input:
        inicio = input[1]
        fin = input[3]
        return [chr(c) for c in range(ord(inicio), ord(fin)+1)]

    return [input]

def compile_dfa(dfa: DFA) -> DFA:
    """
    Convierte un DFA extendido en un DFA estándar.

    :param dfa: DFA con transiciones SRE.
    :type dfa: DFA
    :returns: DFA compilado.
    :rtype: DFA
    """

    nuevas_transiciones = []

    for transicion in dfa.transitions:

        simbolos = parse_sre(
            VOCABULARIO,
            transicion.symbol
        )

        for simbolo in simbolos:

            nuevas_transiciones.append(
                Transition(
                    transicion.from_state,
                    simbolo,
                    transicion.to_state
                )
            )

    return DFA(
        name=dfa.name + "_compiled",
        alphabet=VOCABULARIO,
        states=dfa.states,
        transitions=nuevas_transiciones,
        start_state=dfa.start_state
    )

def save_dfa(dfa: DFA, output_path: str):

    data = {
        "name": dfa.name,
        "alphabet": dfa.alphabet,
        "start_state": dfa.start_state,
        "states": [
            {
                "id": s.id,
                "accepting": s.accepting
            }
            for s in dfa.states
        ],
        "transitions": [
            {
                "from": t.from_state,
                "symbol": t.symbol,
                "to": t.to_state
            }
            for t in dfa.transitions
        ]
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )