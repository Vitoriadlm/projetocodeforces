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