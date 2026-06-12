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
from src.dfa.compiler import parse_sre, VOCABULARIO

class TestCompiler(unittest.TestCase):

    def test_dot(self):
        resultado = parse_sre(VOCABULARIO, '.')
        self.assertEqual(resultado, VOCABULARIO)

    def test_digitos(self):
        resultado = parse_sre(VOCABULARIO, '\\d')
        self.assertEqual(resultado, ['0','1','2','3','4','5','6','7','8','9'])

    def test_rango_positivo(self):
        resultado = parse_sre(VOCABULARIO, '[a-z]')
        self.assertEqual(resultado, [chr(c) for c in range(ord('a'), ord('z')+1)])

    def test_rango_negativo(self):
        resultado = parse_sre(VOCABULARIO, '[^a-z]')
        self.assertNotIn('a', resultado)
        self.assertNotIn('z', resultado)

    def test_union(self):
        resultado = parse_sre(VOCABULARIO, '[a-z]|\\d')
        self.assertIn('a', resultado)
        self.assertIn('0', resultado)

if __name__ == "__main__":
    unittest.main()