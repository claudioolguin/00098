"""# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Cuenta de números impares:", odd_numbers)
print("Cuenta de números pares:", even_numbers)



+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
"""


"""while(True):
    secret_number = 777
    pregunta=int(input("ingrese numero: "))

    if pregunta == secret_number : 
        print (secret_number)
        print("¡Bien hecho, muggle! Eres libre ahora")
        break
    else:
        print("atrapado en mi bucle!")
        print("---------------------------------------------------")
    continue """
    
"""for i in range(10):
    print("El valor de i es actualmente", i)"""
"""for i in range(5,20,5):
    print("El valor de i es actualmente", i)"""
"""for i in range(5, 50,5):
    print("---------------------------------------------------------")
    print("El valor de i es actualmente", i)"""

#encuentra la potencia de un numero
"""power = 1
for expo in range(16):
    print("5 a la potencia de", expo, "es", power)
    power *= 5"""

        
"""m=[3,1,-2]    
print(m[m[-1]])    """
"""
x=1
x=x==x
print(x)"""

m=[1, 2, 3, 4]
print(m[-3:-2])