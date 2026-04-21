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
import os
import subprocess

class TestVisualization(unittest.TestCase):

    def test_png_generation(self):
        # Ejecuta el programa principal
        subprocess.run(
            ["python", "src/dfa/fauna_main.py", "examples/dfa2.json"],
            check=True
        )

        # Verifica que el archivo PNG existe
        self.assertTrue(os.path.exists("examples/dfa2.png"))

        # Verifica que no esté vacío
        self.assertGreater(os.path.getsize("examples/dfa2.png"), 0)


if __name__ == "__main__":
    unittest.main()
