class Optimizar:

    '''
    Creamos el array para almacenar los números introducidos, y creamos un constructor
    con sus parametros. Crearemos varios métodos:
    '''
    
    array = []
    def __init__(self,array):
        self.array = array

    # Método que imprime "introduzca un numero", escanea 
    # por teclado y devuelvo el num introducido
    
    def introducir_numero(self) -> int:
        print("Introduzca un número:")
        n = int(input())
        return n
    
    # Este método añade un valor al array, y lo imprime por pantalla
    
    def añadir_valor_array(self, n):
        self.array.append(n) #Añadimos el valor a la variable array
        return n

    # Método para sumar todos los números del array y hacer la media
    
    def media(self) -> int:
        sumaTotal = 0       #Inicializamos la variable sumaTotal
        for n in self.array:
            sumaTotal = sumaTotal + n  #Creamos un for para sumar los números del array
        media = sumaTotal/len(self.array) #Calculamos la media, len indica la cantidad de elementos del array
        return media
