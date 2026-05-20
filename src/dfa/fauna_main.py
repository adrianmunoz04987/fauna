"""
EIF203 Estructuras Discretas - Semestre I, 2026
Universidad Nacional

Autores:
   Adrian Muñoz Cisneros
   Marco Vinicio Coto Dall' Anesse
   Gabriel Chavarria Barquero
   Joao Arauz Rodriguez
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import json
from graphviz import Digraph
from model import State, Transition, DFA
from runner import run_dfa


def load_dfa(path):
    """
    Carga un DFA desde un archivo JSON.

    :param path: Ruta al archivo JSON.
    :type path: str
    :returns: El DFA cargado.
    :rtype: DFA
    """

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    states = [] #Convierte los diccionarios de .json en objetos state
    for s in data["states"]:
        states.append(State(s["id"], s["accepting"]))

    transitions = [] #Convierte los diccionarios de .json en objetos Transitions
    for t in data["transitions"]:
        transitions.append(Transition(t["from"], t["symbol"], t["to"]))

    return DFA(
        name = data["name"],
        alphabet = data["alphabet"],
        states = states,
        transitions = transitions,
        start_state = data["start_state"],
    )


def build_graph(dfa):
    """
    Construye un grafo visual a partir de un DFA.

    :param dfa: El automata a visualizar.
    :type dfa: DFA
    :returns: El grafo generado.
    :rtype: Digraph
    """

    dot = Digraph()



    # agregar estados
    for state in dfa.states:
        shape = "doublecircle" if state.accepting else "circle"
        dot.node(state.id, shape=shape)

    # nodo inicio
    dot.node("", shape="none")
    dot.edge("", dfa.start_state)

    # transiciones
    for t in dfa.transitions:
        dot.edge(t.from_state, t.to_state, label=t.symbol)

    return dot


def save_graph(graph, json_path):
    """
    Guarda el grafo como imagen PNG en disco.

    :param graph: El grafo a guardar.
    :type graph: Digraph
    :param json_path: Ruta del archivo JSON original.
    :type json_path: str
    """

    output_path = json_path.replace(".json", "")
    graph.render(output_path, format="png", cleanup=True)
    print(f"Imagen generada: {output_path}.png")


def main():
    """
    Funcion principal del programa.
    """
    
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Uso: python src\\dfa\\fauna_main.py <archivo_json>")
        return

    path = sys.argv[1]
    dfa = load_dfa(path)
    graph = build_graph(dfa)
    save_graph(graph, path)

    if len(sys.argv) == 3:
        cadena = sys.argv[2]
        print(f"\nEjecutando DFA '{dfa.name}' con la cadena: '{cadena}'")
        resultado = run_dfa(dfa, cadena)
        if resultado:
            print("Resultado: ACEPTADA")
        else:
            print("Resultado: RECHAZADA")


if __name__ == "__main__":
    main()