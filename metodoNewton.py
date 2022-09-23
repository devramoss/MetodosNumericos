import math

def f(x):
    return(math.cos(x))

def df(x):
    h = 0.001
    return((f(x + h) - f(x))/h)

a = 1.0
b = 2.0

# Valor inicial 
x0 = a 

precisao = 0.001
valorEsperado = math.pi/2.0 

x = 0.0

# Número máximo de interações
N = 100 
i = 1

while(math.fabs(f(x0)) > precisao):
    # Função de interação
    x = x0 - (f(x0)/df(x0)) 
    
    x0 = x
    i = i + 1

    if(i >= N):
        print("Infelizmente a raíz não foi encontrada")
        break

if(i < N):
    erroAbsoluto = valorEsperado - x0
    erroRelativo = erroAbsoluto/valorEsperado

    print("Valor da função é: %.4f" %(x0))
    print("O número de interações foi: ", i)
    print("O erro absoluto é: ", erroAbsoluto)
    print("O erro relativo é: ", erroRelativo)