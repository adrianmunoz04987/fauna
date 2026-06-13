"""
EIF203 Estructuras Discretas - Semestre I, 2026
Universidad Nacional

Autores:
   Adrian Muñoz Cisneros
   Marco Vinicio Coto Dall' Anesse
   Gabriel Chavarria Barquero
   Joao Arauz Rodriguez

Pruebas unitarias para la visualizacion del DFA.
Verifica que el comando 'view' genera correctamente archivos PNG.
"""

import unittest
import os
import subprocess


class TestVisualization(unittest.TestCase):
    """Pruebas de generacion de imagenes PNG via comando 'view'."""

    def test_png_contador_hola(self):
        """Debe generar un PNG valido para el DFA contador_hola."""
        result = subprocess.run(
            ["python", "src/dfa/fauna_main.py", "view",
             "--format", "png", "examples/contador_hola.json"],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists("examples/contador_hola.png"))
        self.assertGreater(os.path.getsize("examples/contador_hola.png"), 0)

    def test_png_contiene_101(self):
        """Debe generar un PNG valido para el DFA contiene_101."""
        result = subprocess.run(
            ["python", "src/dfa/fauna_main.py", "view",
             "--format", "png", "examples/contiene_101.json"],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertTrue(os.path.exists("examples/contiene_101.png"))
        self.assertGreater(os.path.getsize("examples/contiene_101.png"), 0)


if __name__ == "__main__":
    unittest.main()
