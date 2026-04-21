"""
EIF203 Estructuras Discretas - Semestre I, 2026
Universidad Nacional

Autores:
   Adrian Muñoz Cisneros
   Marco Vinicio Coto Dall' Anesse
   Gabriel Chavarria Barquero
   Joao Arauz Rodriguez
"""

import unittest
from src.dfa.runner import run_dfa
from src.dfa.model import DFA, State, Transition

class TestRunner(unittest.TestCase):

    def setUp(self):
        # Estados
        s0 = State("q0", False)
        s1 = State("q1", True)

        states = [s0, s1]

        # Transiciones (lista de objetos)
        transitions = [
            Transition("q0", "a", "q1"),
            Transition("q0", "b", "q0"),
            Transition("q1", "a", "q1"),
            Transition("q1", "b", "q0"),
        ]

        # DFA según SU constructor real
        self.dfa = DFA(
            name="test_dfa",
            alphabet={"a", "b"},
            states=states,
            transitions=transitions,
            start_state="q0"
        )

    def test_accepts_valid_string(self):
        self.assertTrue(run_dfa(self.dfa, "a"))
        self.assertTrue(run_dfa(self.dfa, "ba"))
        self.assertTrue(run_dfa(self.dfa, "aa"))

    def test_rejects_invalid_string(self):
        self.assertFalse(run_dfa(self.dfa, "b"))
        self.assertFalse(run_dfa(self.dfa, "bb"))
        self.assertFalse(run_dfa(self.dfa, "bab"))


if __name__ == "__main__":
    unittest.main()
