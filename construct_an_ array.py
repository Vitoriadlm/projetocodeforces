import sys
 
entrada = sys.stdin.read().split()
t = int(entrada[0])
 
posicao = 1
 
for _ in range(t):
    n = int(entrada[posicao])
    posicao += 1
 
    resposta = []
 
    for numero in range(n + 1, 2 * n + 1):
        resposta.append(numero)
 
    print(*resposta)