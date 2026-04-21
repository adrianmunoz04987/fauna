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

class State: #Esta clase se usara para definir un estado del DFA
    def __init__(self, id, accepting):
        self.id = id
        self.accepting = accepting


class Transition: #Esta clase se usara para definir una transicion del DFA
    def __init__(self, from_state, symbol, to_state):
        self.from_state = from_state
        self.symbol = symbol
        self.to_state = to_state

class DFA: #Esta clase es la definicion completa de un DFA
    def __init__(self, name, alphabet, states, transitions, start_state):
        self.name = name
        self.alphabet = alphabet
        self.states = states
        self.transitions = transitions
        self.start_state = start_state