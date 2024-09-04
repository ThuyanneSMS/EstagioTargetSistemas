def verifica_fibonacci(numero):
    fib1, fib2 = 0, 1

    fibonacci_sequencia = [fib1, fib2]

    while fib2 < numero:
        fib1, fib2 = fib2, fib1 + fib2
        fibonacci_sequencia.append(fib2)

    if numero in fibonacci_sequencia:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."


numero_informado = int(input("Digite um número: "))

resultado = verifica_fibonacci(numero_informado)

print(resultado)
