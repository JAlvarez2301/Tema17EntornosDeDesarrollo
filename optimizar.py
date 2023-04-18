class optimizar:

    
    array = []
for i in range(3):
    n = int(input("Introduzca un número: ")) #Pedimos al usuario que de un valor a la variable
    array.append(n) #Añade un elemento al final del array
media = sum(array) / len(array) #Media va a ser igual a: la suma de los valores del array dividido entre la longitud del array
print("La media es " + str(media)) #Importante hacer el casting con str para que no de error el hacer el print
