"""
EIF203 Estructuras Discretas - Semestre I, 2026
Universidad Nacional

Autores:
   Adrian Muñoz Cisneros
   Marco Vinicio Coto Dall' Anesse
   Gabriel Chavarria Barquero
   Joao Arauz Rodriguez
"""


import json
import sys
from graphviz import Digraph


def load_dfa(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_graph(dfa):
    dot = Digraph()

    start_state = dfa["start_state"]

    # agregar estados
    for state in dfa["states"]:
        shape = "doublecircle" if state["accepting"] else "circle"
        dot.node(state["id"], shape=shape)

    # nodo inicio
    dot.node("", shape="none")
    dot.edge("", start_state)

    # transiciones
    for t in dfa["transitions"]:
        dot.edge(t["from"], t["to"], label=t["symbol"])

    return dot


def save_graph(graph, json_path):
    output_path = json_path.replace(".json", "")
    graph.render(output_path, format="png", cleanup=True)
    print(f"Imagen generada: {output_path}.png")


def main():
    if len(sys.argv) != 2:
        print("Uso: python src\\dfa\\fauna_main.py <archivo_json>")
        return

    path = sys.argv[1]
    dfa = load_dfa(path)
    graph = build_graph(dfa)
    save_graph(graph, path)


if __name__ == "__main__":
    main()