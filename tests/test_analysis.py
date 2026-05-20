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
from src.dfa.model import State, Transition, DFA
from src.dfa.analysis import is_complete, unreachable_states, useless_states


class TestAnalysis(unittest.TestCase):

    def setUp(self):
        # DFA simple para pruebas
        self.dfa = DFA(
            name="test",
            alphabet=["a", "b"],
            states=[
                State("q0", False),
                State("q1", True),
                State("q2", False)
            ],
            transitions=[
                Transition("q0", "a", "q1"),
                Transition("q0", "b", "q0"),
                Transition("q1", "a", "q1"),
                Transition("q1", "b", "q0"),
                # q2 no tiene transiciones → inalcanzable
            ],
            start_state="q0"
        )

    def test_is_complete(self):
        self.assertFalse(is_complete(self.dfa))

    def test_unreachable_states(self):
        result = unreachable_states(self.dfa)
        self.assertIn("q2", result)

    def test_useless_states(self):
        result = useless_states(self.dfa)
        self.assertIn("q2", result)


if __name__ == "__main__":
    unittest.main()