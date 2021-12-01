# Primer modulo en Python

def FactoresPrimos(n):
    resultado="Fp: " + str(n) + " = "
    for i in range(2, n + 1):
        while n % i == 0:
            resultado += str(i) + " . "
            n = n / i

    return resultado