def print_sudoku(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()
    print()


def encontrar_vazio(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def eh_valido(board, num, pos):
    linha, coluna = pos

    # Linha
    if num in board[linha]:
        return False

    # Coluna
    for i in range(9):
        if board[i][coluna] == num:
            return False

    # Bloco 3x3
    inicio_linha = (linha // 3) * 3
    inicio_coluna = (coluna // 3) * 3
    for i in range(inicio_linha, inicio_linha + 3):
        for j in range(inicio_coluna, inicio_coluna + 3):
            if board[i][j] == num:
                return False

    return True


def resolver_sudoku(board):
    vazio = encontrar_vazio(board)
    if not vazio:
        return True
    linha, coluna = vazio

    for num in range(1, 10):
        if eh_valido(board, num, (linha, coluna)):
            board[linha][coluna] = num

            if resolver_sudoku(board):
                return True

            board[linha][coluna] = 0
    return False
