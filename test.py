import unittest

class TestMedia(unittest.TestCase):
    
    def test_media_simple(self):
        array = [1, 2, 3]
        media_esperada = 2.0
        media_obtenida = sum(array) / len(array)
        self.assertEqual(media_esperada, media_obtenida)
        
    def test_media_negativos(self):
        array = [-1, -2, -3]
        media_esperada = -2.0
        media_obtenida = sum(array) / len(array)
        self.assertEqual(media_esperada, media_obtenida)
        
    def test_media_ceros(self):
        array = [0, 0, 0]
        media_esperada = 0.0
        media_obtenida = sum(array) / len(array)
        self.assertEqual(media_esperada, media_obtenida)
        
    def test_media_decimales(self):
        array = [1.5, 2.5, 3.5]
        media_esperada = 2.5
        media_obtenida = sum(array) / len(array)
        self.assertEqual(media_esperada, media_obtenida)
        
if __name__ == '__main__':
    unittest.main()
