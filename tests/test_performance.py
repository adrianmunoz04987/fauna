"""
EIF203 Estructuras Discretas - Semestre I, 2026
Universidad Nacional

Autores:
   Adrian Muñoz Cisneros
   Marco Vinicio Coto Dall' Anesse
   Gabriel Chavarria Barquero
   Joao Arauz Rodriguez

Pruebas de rendimiento basicas del sistema FAuna.
"""

import unittest
import time
from src.dfa.model import State, Transition, DFA
from src.dfa.runner import run_dfa
from src.dfa.analysis import is_complete, unreachable_states, useless_states
from src.dfa.compiler import compile_dfa


def build_dfa_binario():
    """Construye un DFA que acepta cadenas binarias que terminan en 1."""
    states = [State("q0", False), State("q1", True)]
    transitions = [
        Transition("q0", "0", "q0"),
        Transition("q0", "1", "q1"),
        Transition("q1", "0", "q0"),
        Transition("q1", "1", "q1"),
    ]
    return DFA("binario", ["0", "1"], states, transitions, "q0")


class TestPerformance(unittest.TestCase):

    def test_run_cadena_larga(self):
        """El runner debe procesar 1000 simbolos en menos de 1 segundo."""
        dfa = build_dfa_binario()
        cadena = "01" * 500
        inicio = time.time()
        run_dfa(dfa, cadena)
        self.assertLess(time.time() - inicio, 1.0)

    def test_analysis_rapido(self):
        """El analisis completo debe completarse en menos de 0.5 segundos."""
        dfa = build_dfa_binario()
        inicio = time.time()
        is_complete(dfa)
        unreachable_states(dfa)
        useless_states(dfa)
        self.assertLess(time.time() - inicio, 0.5)

    def test_compile_rapido(self):
        """La compilacion debe completarse en menos de 1 segundo."""
        states = [State("q0", False), State("q1", True)]
        transitions = [Transition("q0", "[a-z]|\\d", "q1")]
        dfa = DFA("extendido", [], states, transitions, "q0")
        inicio = time.time()
        compile_dfa(dfa)
        self.assertLess(time.time() - inicio, 1.0)


if __name__ == "__main__":
    unittest.main()
