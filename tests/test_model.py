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
from src.dfa.model import DFA, State, Transition

class TestModel(unittest.TestCase):

    def test_state_creation(self):
        s = State("q0", True)
        self.assertEqual(s.id, "q0")
        self.assertTrue(s.accepting)

    def test_transition_creation(self):
        t = Transition("q0", "a", "q1")
        self.assertEqual(t.from_state, "q0")
        self.assertEqual(t.symbol, "a")
        self.assertEqual(t.to_state, "q1")

    def test_dfa_creation(self):
        states = [State("q0", False), State("q1", True)]
        transitions = [Transition("q0", "a", "q1")]

        dfa = DFA(
            name="test",
            alphabet={"a"},
            states=states,
            transitions=transitions,
            start_state="q0"
        )

        self.assertEqual(dfa.name, "test")
        self.assertIn("a", dfa.alphabet)
        self.assertEqual(dfa.start_state, "q0")


if __name__ == "__main__":
    unittest.main()
