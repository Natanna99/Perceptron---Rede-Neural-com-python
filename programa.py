from perceptron import *
mudar = True
entradas = ['111101101101111',
            '010010010010010',
            '111001111100111',
            '111001111001111',
            '101101111001001',
            '111100111001111',
            '111100111101111',
            '111001001001001',
            '111101111101111',
            '111101111001111']

objetivos = '0101010101'

pesos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bias = 0
loop = 0
while mudar:
    x=0
    loop+=1
    print(25*'-','GERAÇÃO:',loop,25*'-')
    print('|X| Pesos = ',pesos)
    for i in range(len(entradas)):
        print(5*'=','digito:',i,5*'=')
        soma = somaponderada(entradas[i],pesos,bias)
        print('|| Soma = ',soma)
        lim=limiar(soma)
        print('|| Limiar = ',lim)
        erro = calculaerro(objetivos[i],lim)
        print('|| Erro = ',erro)
        if erro != 0:
            x = 1
            saida = atualizapesos(entradas[i],pesos,bias,erro)
            pesos = saida[0]
            bias = saida[1]
        print('|| Bias = ',bias)
        print('|| Pesos = ',pesos)
        print(20*'=')
    if x == 1:
        mudar = True
    else:
        mudar = False
print(60*'-','\n')
print(20*'|#|','\n')    
print(4*'  ','resultado em ',loop,'atualizações de pesos!')
print('\nPesos:',pesos)
print('Bias:',bias,'\n')
for i in range(len(entradas)):
    analise = Analise(entradas[i],pesos,bias)
    if analise == 1:
        print(4*'  ','digito',i,'igual a',analise,'(impar)')
    else:
        print(4*'  ','digito',i,'igual a',analise,'(par)')
print()
print(20*'|#|')

