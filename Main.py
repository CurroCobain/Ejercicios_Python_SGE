"""
# Ejercicio 1 ------------------------------------

x = "Buenas Tardes"
# Usar el método len para imprimir la longitud
longitud = len(x)
print("Longitud de la cadena:", longitud)

# Obtener el primer carácter
primer_caracter = x[0]
print("Primer carácter:", primer_caracter)

# Obtener los caracteres de la posición 3 a la 6 (no incluido)
subcadena = x[2:6]
print("Caracteres de la posición 3 a la 6:", subcadena)

# Ejercicio2 ---------------------------------------------

y = " Bienvenidos a crase "

# Devolver la cadena sin los espacios en blanco del principio y final
cadena_sin_espacios = x.strip()
print("Cadena sin espacios en blanco del principio y final:", cadena_sin_espacios)

# Reemplazar el carácter 'r' por 'l'
cadena_reemplazada = x.replace('r', 'l')
print("Cadena con el carácter 'r' reemplazado por 'l':", cadena_reemplazada)

# Ejercicio 3 -------------------------------------------------

Frutas = ["manzana", "platano", "fresa"]

# Imprimir el segundo ítem
segundo_item = Frutas[1]
print("Segundo ítem:", segundo_item)

# Comprobar si "patata" está en la lista e imprimir mensaje en caso negativo
if "patata" not in Frutas:
    print("Patata no es una fruta")

# Cambiar el valor de "manzana" por "kiwi"
Frutas[0] = "kiwi"

# Usar el método append() para añadir a la lista la "naranja"
Frutas.append("naranja")

# Usar el método insert() para añadir el limón en el tercer puesto de la lista
Frutas.insert(2, "limón")

# Usar el método remove() para eliminar la "fresa"
Frutas.remove("fresa")

# Imprimir los ítems de la lista usando un bucle
print("Ítems de la lista:")
for fruta in Frutas:
    print(fruta)

# Ejercicio 4 --------------------------------------

Coche = {"marca": "Ford", "modelo": "Mustang"}
#  Usar el método get para imprimir el valor de la clave “modelo”
print(Coche.get("modelo"))

# Añadir la clave/valor: “color” : “rojo” al diccionario de coche
Coche["color"] = "rojo"
print(Coche)

# Ejercicio 5 ------------------------------------------

# Dados dos números a y b, imprimir “Hola” si a es mayor que b y “Adiós” si a es menor que b

a = int(input("indicame el primer número "))
b = int(input("indicame el segundo número "))
if a > b:
    print("Hola")
else:
    print("Adiós")

# Ejercicio 6 -----------------------------------------

# Imprimir los 6 primeros números enteros
for i in range(1, 7):
    print(i)

# Ejercicio 7 -------------------------------------------

# Dado un número indicar si es par o impar

numero = int(input("introduce un número "))
if numero % 2 == 0:
    print("El número ", numero, " es par")
else:
    print("El número ", numero, " es impar")

# Ejercicio 8 --------------------------------------------

# Imprimir los números impares desde el 50 hasta la unidad y calcular su suma
lista = []
total = 0
for i in range(0, 51):
    if i % 2 != 0:
        lista.append(i)
        print(i)
for j in lista:
    total += j
print("El total es: ", total)




# Ejercicio 9 -----------------------------------------------

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# Ejemplo de uso
numero = int(input("introduce un número: "))
resultado = factorial_iterativo(numero)
print(f"El factorial de {numero} es: {resultado}")



# Ejercicio 10 ---------------------------

# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False

def es_vocal(caracter):
    # Convertimos el carácter a minúsculas para hacer la comparación más flexible
    caracter = caracter.lower()

    # Verificamos si el carácter es una vocal
    return caracter in ['a', 'e', 'i', 'o', 'u']


caracter = input("Introduce una letra: ")
print(caracter, " es una vocal: ", es_vocal(caracter))



# Ejercicio 11 -----------------------------------

# Escribir una funcion sum() y una función multip() que sumen y multipliquen
# respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería
# devolver 10 y multip([1,2,3,4]) debería devolver 24

def sumalista(lista: list):
    suma = 0
    for i in lista:
        suma += i
    return suma


print(sumalista([1, 2, 3, 4]))


def multilista(lista: list):
    total = 1
    for i in lista:
        total = total * i
    return total


print(multilista([1, 2, 3, 4, ]))
"""