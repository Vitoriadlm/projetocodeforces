# Desafio Codeforces — Mentoria Codificadas | Além do Código
 
## Sobre este repositório
 
Este repositório contém minha resolução para o desafio de programação proposto na mentoria, utilizando problemas da plataforma [Codeforces](https://codeforces.com/) com auxílio de Inteligência Artificial.
 
---
 
## Problemas escolhidos
 
| # | Nome do problema | Link | Dificuldade |
|---|-----------------|------|-------------|
| 1 | 2231A - Construct an Array | https://codeforces.com/problemset/problem/2231/A | 800 |
| 2 | 2178A - Yes or Yes | https://codeforces.com/problemset/problem/2178/A | 800 |
 
 
---
 
## Problema 1 — 2231A - Construct an Array
 
### O que o problema pede?
O problema pede para construir um vetor de tamanho n utilizando números entre 1 e 2n. Além disso, todos os elementos do vetor e as somas de elementos vizinhos devem ser diferentes entre si.
 
### Como eu resolvi?
Utilizei uma construção simples escolhendo números maiores que n. Dessa forma, todos os elementos são distintos e as somas dos elementos adjacentes também não se repetem nem coincidem com os valores do vetor.
 
 
### Código
```python
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
```
 
---
 
## Problema 2 —  2178A - Yes or Yes
 
### O que o problema pede?
O problema apresenta uma sequência formada pelas letras Y e N. É necessário verificar se é possível reduzir toda a sequência para apenas um caractere sem nunca combinar dois caracteres Y ao mesmo tempo.
 
### Como eu resolvi?
Observei que a resposta depende apenas da quantidade de letras Y na string. Se houver mais de uma letra Y, em algum momento será necessário combinar dois Ys, o que é proibido. Portanto, a resposta é YES apenas quando existe no máximo um Y. 
 
### Código
```python
import sys


def pode_reduzir_sem_juntar_yy(texto):
    quantidade_de_y = 0

    for caractere in texto:
        if caractere == "Y":
            quantidade_de_y += 1

    if quantidade_de_y <= 1:
        return "YES"
    else:
        return "NO"


def main():
    dados = sys.stdin.read().split()

    quantidade_de_testes = int(dados[0])
    posicao = 1

    respostas = []

    for _ in range(quantidade_de_testes):
        texto = dados[posicao]
        posicao += 1

        resultado = pode_reduzir_sem_juntar_yy(texto)
        respostas.append(resultado)

    print("\n".join(respostas))


if __name__ == "__main__":
    main()
```
 
---
 
 
## IA utilizada
 
**Qual IA você usou?**
ChatGPT
 
**Como a IA te ajudou?**
Utilizei o ChatGPT para compreender melhor os enunciados, identificar padrões nas soluções e revisar os códigos em Python. A IA ajudou a entender a lógica necessária para resolver os problemas, mas procurei compreender cada etapa antes de implementar.
 
---
 
## Reflexão
 
### Dificuldades encontradas
A maior dificuldade foi interpretar corretamente os enunciados e encontrar uma estratégia que atendesse todas as condições exigidas pelo problema.
 
 
### O que aprendi
Aprendi mais sobre construção de algoritmos, manipulação de vetores e análise de condições lógicas. Também aprendi como utilizar a IA como ferramenta de apoio para estudar programação.

 
### Como foi a experiência?
A experiência foi muito positiva. Gostei de resolver problemas de programação competitiva e perceber como pequenas observações podem simplificar bastante uma solução. Além disso, foi interessante aprender a organizar um repositório no GitHub e documentar o processo de resolução.<!-- Conta um pouco como foi no geral. O que mais gostou? O que mudaria? -->
