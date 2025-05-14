import unittest
from juego import determinar_ganador

class TestDeterminarGanador(unittest.TestCase):
    """Clase para probar la función determinar_ganador del juego Piedra, Papel, Tijeras"""

    def test_piedra_vs_piedra(self):
        """Prueba: Piedra vs. Piedra = Empate (0)"""
        resultado = determinar_ganador("piedra", "piedra")
        self.assertEqual(resultado, 0)

    def test_piedra_vs_papel(self):
        """Prueba: Piedra vs. Papel = Papel gana (-1)"""
        resultado = determinar_ganador("piedra", "papel")
        self.assertEqual(resultado, -1)

    def test_piedra_vs_tijera(self):
        """Prueba: Piedra vs. Tijera = Piedra gana (1)"""
        resultado = determinar_ganador("piedra", "tijera")
        self.assertEqual(resultado, 1)

    def test_papel_vs_piedra(self):
        """Prueba: Papel vs. Piedra = Papel gana (1)"""
        resultado = determinar_ganador("papel", "piedra")
        self.assertEqual(resultado, 1)

    def test_papel_vs_papel(self):
        """Prueba: Papel vs. Papel = Empate (0)"""
        resultado = determinar_ganador("papel", "papel")
        self.assertEqual(resultado, 0)

    def test_papel_vs_tijera(self):
        """Prueba: Papel vs. Tijera = Tijera gana (-1)"""
        resultado = determinar_ganador("papel", "tijera")
        self.assertEqual(resultado, -1)

    def test_tijera_vs_piedra(self):
        """Prueba: Tijera vs. Piedra = Piedra gana (-1)"""
        resultado = determinar_ganador("tkjdfsñ", "piedra")
        self.assertEqual(resultado, -1)

    def test_tijera_vs_papel(self):
        """Prueba: Tijera vs. Papel = Tijera gana (1)"""
        resultado = determinar_ganador("tijera", "papel")
        self.assertEqual(resultado, 1)

    def test_tijera_vs_tijera(self):
        """Prueba: Tijera vs. Tijera = Empate (0)"""
        resultado = determinar_ganador("tijera", "tijera")
        self.assertEqual(resultado, 0)

if __name__ == "__main__":
    unittest.main()