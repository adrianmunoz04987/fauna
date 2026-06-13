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
    """Pruebas para la funcion is_complete."""

    def test_dfa_completo(self):
        """Un DFA con todas las transiciones definidas debe ser completo."""
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
        """Un DFA al que le faltan transiciones debe reportarlas."""
        dfa = DFA(
            name="incompleto",
            alphabet=["a", "b"],
            states=[State("q0", False), State("q1", True)],
            transitions=[
                Transition("q0", "a", "q1"),
                # Falta q0 -b->, q1 -a->, q1 -b->
            ],
            start_state="q0"
        )
        faltantes = is_complete(dfa)
        self.assertGreater(len(faltantes), 0)
        self.assertIn("(q0, b)", faltantes)


class TestUnreachableStates(unittest.TestCase):
    """Pruebas para la funcion unreachable_states."""

    def test_estado_inalcanzable(self):
        """q2 no tiene transiciones que lleguen a el, debe ser inalcanzable."""
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
        """Cuando todos los estados son alcanzables, la lista debe estar vacia."""
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
    """Pruebas para la funcion useless_states."""

    def test_estado_inutil(self):
        """q2 es un estado trampa sin aceptacion, debe ser inutil."""
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
        """Cuando todos los estados pueden llegar a aceptacion, lista vacia."""
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
