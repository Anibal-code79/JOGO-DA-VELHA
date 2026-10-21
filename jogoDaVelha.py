from random import randrange

def mostar_tabuleiro(tabuleiro):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")

def analisar_quadros_livres(tabuleiro):
    quadrado_livre=[]
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] not in ["X","O"]:
                quadrado_livre.append((linha,coluna))
    return quadrado_livre

def movimentar_jogo_utilizador(tabuleiro):
    posicao = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
    }
    while True:
        try:
            usuario = int(input("Digite seu movimento: "))
        except ValueError:
            print("Digite um número inteiro válido.")
            continue
        if usuario < 1 or usuario > 9:
            print("Escolha um número entre 1 e 9.")
            continue
        linha, coluna = posicao[usuario]
        if tabuleiro[linha][coluna] in ["X", "O"]:
            print("Essa posição já está ocupada.")
            continue
        tabuleiro[linha][coluna] = "O"
        break

def vitoria_para(tabuleiro, jogador):
    if tabuleiro[0][0] == jogador and tabuleiro[0][1] == jogador and tabuleiro[0][2] == jogador:
        return True
    if tabuleiro[1][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[1][2] == jogador:
        return True
    if tabuleiro[2][0] == jogador and tabuleiro[2][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][0] == jogador and tabuleiro[2][0] == jogador:
        return True
    if tabuleiro[0][1] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][1] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][2] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False

def movimento_computador(tabuleiro):
    free_fields = analisar_quadros_livres(tabuleiro)
    if free_fields:

        index = randrange(len(free_fields))

        row, col = free_fields[index]

        tabuleiro[row][col] = "X"
    
    
tabuleiro = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

tabuleiro[1][1] = "X"

mostar_tabuleiro(tabuleiro)

while True:

    movimentar_jogo_utilizador(tabuleiro)

    mostar_tabuleiro(tabuleiro)

    if vitoria_para(tabuleiro, "O"):
        print("Você ganhou!")
        break

    if not analisar_quadros_livres(tabuleiro):
        print("Empate!")
        break

    movimento_computador(tabuleiro)
    mostar_tabuleiro(tabuleiro)

    if vitoria_para(tabuleiro, "X"):
        print("O computador ganhou!")
        break

    if not analisar_quadros_livres(tabuleiro):
        print("Empate!")
        break