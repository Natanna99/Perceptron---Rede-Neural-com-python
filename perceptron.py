def calculaerro(valor1,valor2):
    return int(valor1) - int(valor2)

def somaponderada(entradas,pesos,bias):
    saida = 0
    for i in range(15):
        saida += int(entradas[i])*int(pesos[i])
    saida+=bias
    return saida

def limiar(valor):
    if valor >= 0:
        return 1
    return 0

def atualizapesos(entradas,pesos,bias,erro):
    for i in range(15):
        pesos[i] += erro * int(entradas[i])
    bias += erro
    return [pesos,bias]

def Analise(entrada,pesos,bias):
    return limiar(somaponderada(entrada,pesos,bias))
