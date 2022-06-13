def raiz_digital(numero):
    numero_para_string = str(numero)

    soma = 0

    for n in numero_para_string:
        numero_convertido = int(n)
        soma += numero_convertido

    if soma > 9:
        return raiz_digital(soma)

    return soma