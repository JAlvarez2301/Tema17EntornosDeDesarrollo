array = []
for i in range(3):
    n = int(input("Introduzca un número: "))
    array.append(n)
media = sum(array) / len(array)
print("La media es " + str(media))
