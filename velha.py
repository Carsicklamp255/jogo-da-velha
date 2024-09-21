import random

tabuleiro = [
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   ']
]

def exibe_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-'*11)

def movimento_humano(tabuleiro):
    while True:
        try:
            linha = int(input('Escolha uma linha entre (0, 1, 2): '))
            coluna = int(input('Escolha uma coluna entre (0, 1, 2): '))
            if tabuleiro[linha][coluna] == '   ':
                return linha, coluna
            else:
                print('Esta casa está ocupada, tente outra!')
        except (ValueError, IndexError):
            print('Entrada inválida! Utilize apenas números entre 0 e 2.')

def minimax(tabuleiro, depth, is_maximizing):
    vencedor = vitoria(tabuleiro)
    if vencedor == ' X ':
        return -1
    elif vencedor == ' O ':
        return 1
    elif velha(tabuleiro):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == '   ':
                    tabuleiro[i][j] = ' O '
                    score = minimax(tabuleiro, depth + 1, False)
                    tabuleiro[i][j] = '   '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == '   ':
                    tabuleiro[i][j] = ' X '
                    score = minimax(tabuleiro, depth + 1, True)
                    tabuleiro[i][j] = '   '
                    best_score = min(score, best_score)
        return best_score

def movimento_robo(tabuleiro):
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == '   ':
                tabuleiro[i][j] = ' O '
                score = minimax(tabuleiro, 0, False)
                tabuleiro[i][j] = '   '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def vitoria(tabuleiro):
    n = len(tabuleiro)

    for linha in tabuleiro:
        if all(casa == linha[0] != '   ' for casa in linha):
            return linha[0]

    for col in range(n):
        if all(tabuleiro[linha][col] == tabuleiro[0][col] != '   ' for linha in range(n)):
            return tabuleiro[0][col]

    if all(tabuleiro[i][i] == tabuleiro[0][0] != '   ' for i in range(n)):
        return tabuleiro[0][0]

    if all(tabuleiro[i][n - 1 - i] == tabuleiro[0][n - 1] != '   ' for i in range(n)):
        return tabuleiro[0][n - 1]

    return None

def velha(tabuleiro):
    return all('   ' not in linha for linha in tabuleiro)

player = ' X '
robo = ' O '

while True:
    print(f'Turno do Jogador {player}')
    exibe_tabuleiro(tabuleiro)

    if player == ' X ':
        x, y = movimento_humano(tabuleiro)
    else:
        x, y = movimento_robo(tabuleiro)
        print(f"Robô escolheu a posição ({x}, {y})")

    tabuleiro[x][y] = player

    vencedor = vitoria(tabuleiro)
    if vencedor:
        if vencedor.strip() == ' O ':
            print(" o robo ganhou")
        else:
          print(f'Jogador {vencedor.strip()} venceu!')
        exibe_tabuleiro(tabuleiro)
        break

    if velha(tabuleiro):
        print("Deu velha!")
        exibe_tabuleiro(tabuleiro)
        break

    player = ' O ' if player == ' X ' else ' X '