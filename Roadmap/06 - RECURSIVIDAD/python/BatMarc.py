def countdown(numero: int):
    if numero >= 0:
        print(numero)
        countdown(numero - 1)

countdown(5)

# Extra #

def factorial_2(number: int) -> int: 
    if number < 0:
        print("Els números negatius")
        return 0
    elif number == 0:
        return 1
    
    return number * factorial_2(number - 1)

# Calcular el valor en función de la posición asignada a la función. 
# Partir de una lista, ya que Fibbonacci empieza con 0 y 1
numeros = [0,1]

def fibonnacci(posicio: int)-> int:
    num1 = numeros[(len(numeros)-1)] # sería mejor opción hacerlo sin esas variables auxiliares
    num2 = numeros[(len(numeros)-2)]
    sum_fibo = num1 + num2
    numeros.append(sum_fibo)
    if (len(numeros) <= posicio):
        fibonnacci(posicio)
    else:
        return print(numeros[posicio])
fibonnacci(13)
