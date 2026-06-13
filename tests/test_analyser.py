"""
EIF203 Estructuras Discretas - Semestre I, 2026
Universidad Nacional

Autores:
   Adrian Muñoz Cisneros
   Marco Vinicio Coto Dall' Anesse
   Gabriel Chavarria Barquero
   Joao Arauz Rodriguez

Pruebas unitarias para el modulo de analisis (analysis.py).
Cubre completitud, estados inalcanzables y estados inutiles.
"""

import unittest
from src.dfa.model import State, Transition, DFA
from src.dfa.analysis import is_complete, unreachable_states, useless_states


class TestIsComplete(unittest.TestCase):

    def test_dfa_completo(self):
        dfa = DFA(
            name="completo",
            alphabet=["a", "b"],
            states=[State("q0", False), State("q1", True)],
            transitions=[
                Transition("q0", "a", "q1"),
                Transition("q0", "b", "q0"),
                Transition("q1", "a", "q1"),
                Transition("q1", "b", "q0"),
            ],
            start_state="q0"
        )
        faltantes = is_complete(dfa)
        self.assertEqual(len(faltantes), 0)

    def test_dfa_incompleto(self):
        dfa = DFA(
            name="incompleto",
            alphabet=["a", "b"],
            states=[State("q0", False), State("q1", True)],
            transitions=[
                Transition("q0", "a", "q1"),
            ],
            start_state="q0"
        )
        faltantes = is_complete(dfa)
        self.assertGreater(len(faltantes), 0)
        self.assertIn("(q0, b)", faltantes)


class TestUnreachableStates(unittest.TestCase):

    def test_estado_inalcanzable(self):
        dfa = DFA(
            name="inalcanzable",
            alphabet=["a", "b"],
            states=[
                State("q0", False),
                State("q1", True),
                State("q2", False),
            ],
            transitions=[
                Transition("q0", "a", "q1"),
                Transition("q0", "b", "q0"),
                Transition("q1", "a", "q1"),
                Transition("q1", "b", "q0"),
            ],
            start_state="q0"
        )
        result = unreachable_states(dfa)
        self.assertIn("q2", result)
        self.assertNotIn("q0", result)
        self.assertNotIn("q1", result)

    def test_todos_alcanzables(self):
        dfa = DFA(
            name="todos_alcanzables",
            alphabet=["a", "b"],
            states=[State("q0", False), State("q1", True)],
            transitions=[
                Transition("q0", "a", "q1"),
                Transition("q0", "b", "q0"),
                Transition("q1", "a", "q1"),
                Transition("q1", "b", "q0"),
            ],
            start_state="q0"
        )
        result = unreachable_states(dfa)
        self.assertEqual(len(result), 0)


class TestUselessStates(unittest.TestCase):

    def test_estado_inutil(self):
        dfa = DFA(
            name="inutil",
            alphabet=["a", "b"],
            states=[
                State("q0", False),
                State("q1", True),
                State("q2", False),
            ],
            transitions=[
                Transition("q0", "a", "q1"),
                Transition("q0", "b", "q2"),
                Transition("q2", "a", "q2"),
                Transition("q2", "b", "q2"),
            ],
            start_state="q0"
        )
        result = useless_states(dfa)
        self.assertIn("q2", result)
        self.assertNotIn("q1", result)

    def test_todos_utiles(self):
        dfa = DFA(
            name="todos_utiles",
            alphabet=["a", "b"],
            states=[State("q0", False), State("q1", True)],
            transitions=[
                Transition("q0", "a", "q1"),
                Transition("q0", "b", "q0"),
                Transition("q1", "a", "q1"),
                Transition("q1", "b", "q0"),
            ],
            start_state="q0"
        )
        result = useless_states(dfa)
        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()
