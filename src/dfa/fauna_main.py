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
from analysis import is_complete, unreachable_states, useless_states
import argparse


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

    parser = argparse.ArgumentParser(description="FAuna - Herramienta para DFAs")
    subparsers = parser.add_subparsers(dest="comando")

    view_parser = subparsers.add_parser("view", help="Visualizar un DFA")
    view_parser.add_argument("archivo", help="Ruta al archivo JSON del DFA")
    view_parser.add_argument("--format", default="png", help="Formato de salida")

    run_parser = subparsers.add_parser("run", help="Ejecutar un DFA con una cadena")
    run_parser.add_argument("archivo", help="Ruta al archivo JSON del DFA")
    run_parser.add_argument("--input", required=True, help="Cadena de entrada")

    analize_parser = subparsers.add_parser("analize", help="Analizar un DFA")
    analize_parser.add_argument("archivo", help="Ruta al archivo JSON del DFA")
    analize_parser.add_argument("--complete", action="store_true", help="Verificar completitud")
    analize_parser.add_argument("--unreachable", action="store_true", help="Ver estados inalcanzables")
    analize_parser.add_argument("--useless", action="store_true", help="Ver estados inutiles")

    args = parser.parse_args()

    if args.comando is None:
        parser.print_help()
        return

    dfa = load_dfa(args.archivo)

    if args.comando == "view":
        graph = build_graph(dfa)
        save_graph(graph, args.archivo)
    elif args.comando == "run":
        resultado = run_dfa(dfa, args.input)
        if resultado:
            print("Resultado: ACEPTADA")
        else:
            print("Resultado: RECHAZADA")
    elif args.comando == "analize":
        if args.complete:
            faltantes = is_complete(dfa)
            if not faltantes:
                print("El DFA es completo.")
            else:
                print("El DFA NO es completo. Transiciones faltantes: ")
                for f in faltantes:
                    print(f)
        if args.unreachable:
            estados = unreachable_states(dfa)
            if estados:
                print(f"Estados inalcanzables: {estados}")
            else:
                print("No hay estados inalcanzables.")
        if args.useless:
            estados = useless_states(dfa)
            if estados:
                print(f"Estados inutiles: {estados}")
            else:
                print("No hay estados inutiles.")
if __name__ == "__main__":
    main()