"""
EIF203 Estructuras Discretas - Semestre I, 2026
Universidad Nacional

Autores:
   Adrian Muñoz Cisneros
   Marco Vinicio Coto Dall' Anesse
   Gabriel Chavarria Barquero
   Joao Arauz Rodriguez
"""
import logging

logging.basicConfig(
    filename='fauna_run.log',
    level=logging.INFO,
    format='%(message)s'
)

def run_dfa(dfa, cadena):
    """
    Ejecuta un DFA con una cadena de entrada.

    :param dfa: El automata a ejecutar.
    :type dfa: DFA
    :param cadena: La cadena de entrada a procesar.
    :type cadena: str
    :returns: True si la cadena es aceptada, False si es rechazada.
    :rtype: bool
    """
    estado_actual = dfa.start_state

    for simbolo in cadena:
        if simbolo not in dfa.alphabet:
            print(f"  Simbolo '{simbolo}' no esta en el alfabeto.")
            logging.info(f"Simbolo '{simbolo}' no esta en el alfabeto.")
            return False

        siguiente = None
        for t in dfa.transitions:
            if t.from_state == estado_actual and t.symbol == simbolo:
                siguiente = t.to_state
                break

        if siguiente is None:
            print(f"  No hay transicion desde {estado_actual} con '{simbolo}'.")
            logging.info(f"No hay transicion desde {estado_actual} con '{simbolo}'.")
            return False

        print(f"  {estado_actual} --{simbolo}--> {siguiente}")
        logging.info(f"{estado_actual} --{simbolo}--> {siguiente}")
        estado_actual = siguiente

    for state in dfa.states:
        if state.id == estado_actual and state.accepting:
            return True

    return False
