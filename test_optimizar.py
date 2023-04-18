from optimizar import Optimizar

def test_añadir_valor_array():
    optimizar = Optimizar([])
    optimizar.añadir_valor_array(1)
    optimizar.añadir_valor_array(2)
    optimizar.añadir_valor_array(3)
    optimizar.añadir_valor_array(4)
    optimizar.añadir_valor_array(5)
    optimizar.añadir_valor_array(6)
    optimizar.añadir_valor_array(7)
    assert len(optimizar.array) == 7 #Comprobamos si la condicion es verdadera, en este caso que el array tiene 7 datos

def test_media():
    optimizar = Optimizar([3, 2, 5, 3, 7, 10])
    assert optimizar.media() == 5
