from this import d


def soma(a,b):
    soma = 0
    soma = a + b
    return soma


def main(void):
    a = int(input("a: "))
    b = int(input("b: "))
    temp = soma(a,b)

    print(f'A soma de {a} com {b} é {temp}')