"""
EIF203 Estructuras Discretas - Semestre I, 2026
Universidad Nacional

Autores:
   Adrian Muñoz Cisneros
   Marco Vinicio Coto Dall' Anesse
   Gabriel Chavarria Barquero
   Joao Arauz Rodriguez
"""

#En este archivo se implementa el uso de POO como indica el Spec del sprint 1

class State:
    """
    Representa un estado del DFA.

    :param id: Identificador unico del estado.
    :type id: str
    :param accepting: Indice si el estado es de aceptacion.
    :type accepting: bool
    """
    def __init__(self, id, accepting):
        self.id = id
        self.accepting = accepting


class Transition:
    """
    Representa una transicion del DFA.

    :param from_state: Estado de origen.
    :type from_state: str
    :param symbol: Simbolo que dispara la transicion.
    :type symbol: str
    :param to_state: Estado destino.
    :type to_state: str
    """
    def __init__(self, from_state, symbol, to_state):
        self.from_state = from_state
        self.symbol = symbol
        self.to_state = to_state

class DFA:
   """
   Representa un Automata Finito Determinista completo.

   :param name: Nombre del DFA.
   :type name: str
   :param alphabet: Lista de simbolos del alfabeto.
   :type alphabet: list
   :param states: Lista de estados.
   :type states: list
   :param transitions: Lista de transiciones.
   :type transitions: list
   :param start_state: ID del estado inicial.
   :type start_state: str
   """
   def __init__(self, name, alphabet, states, transitions, start_state):
    self.name = name
    self.alphabet = alphabet
    self.states = states
    self.transitions = transitions
    self.start_state = start_state