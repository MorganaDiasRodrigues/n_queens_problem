def verifica_tabuleiro(tabuleiro, linha, coluna):
    tamanho = len(tabuleiro)  # Determina o tamanho do tabuleiro

    print("Verificando tab")
    # Verifica a linha inteira
    for j in range(tamanho):
        if tabuleiro[linha][j] == 'r':
            return False

    # Verifica a coluna inteira
    for i in range(tamanho):
        if tabuleiro[i][coluna] == 'r':
            return False

    c = coluna
    l = linha
    while (c > 0) and (l>0):
        c -= 1
        l -= 1
    while (c < coluna) and (l < linha):
        print(f"Verificando diag c,l: {c, l}")
        if tabuleiro[l][c] == "r":
            return False
        c +=1
        l+=1
    
    
    c = coluna
    l = linha
    while (c < tamanho-1) and (l>0):
        c += 1
        l -= 1
    while (c > coluna) and (l < linha):
        print(f"Verificando diag c,l: {c, l}")
        if tabuleiro[l][c] == "r":
            return False
        c -= 1
        l += 1

    # Se passou por todas as verificações, retorna True
    return True


def backtrack(l:int, c:int,  tab:list, faltantes:int, q_p:list):
    print("Começando o backtrack")
    if faltantes == 0: # condicao de parada
        print("TODAS FORAM COLOCADAS")
        for linha in tabuleiro:
            print(linha)
        return tab    

    if verifica_tabuleiro(tabuleiro=tabuleiro, linha=l, coluna=c) is True:
        print(f"Pode colocar em {l, c}")
        q_p.append((l,c))
        tab[l][c] = "r"
        faltantes -= 1
        if c == (len(tabuleiro) - 1): # se está na última coluna e não tem mais casas pra ir, recomeça da próxima
            backtrack(l=l+1, c=0, tab=tab, faltantes=faltantes, q_p=q_p)
        else:
            backtrack(l=l, c=c+1, tab=tab, faltantes=faltantes, q_p=q_p)
    else:
        if (c == (len(tabuleiro) -1)) and (l == (len(tabuleiro) -1)):
            ultima_queen = q_p.pop()
            tab[ultima_queen[0]][ultima_queen[1]] = 0
            faltantes += 1
            if ultima_queen[1] == (len(tabuleiro) - 1):
                backtrack(l=ultima_queen[0]+1, c=0, tab=tab, faltantes=faltantes, q_p=q_p)
            else:
                backtrack(l=ultima_queen[0], c=ultima_queen[1]+1, tab=tab, faltantes=faltantes, q_p=q_p)
        elif c == (len(tabuleiro) - 1): # se está na última coluna e não tem mais casas pra ir, recomeça da próxima
            backtrack(l=l+1, c=0, tab=tab, faltantes=faltantes, q_p=q_p)
        else:
            backtrack(l=l, c=c+1, tab=tab, faltantes=faltantes, q_p=q_p)

tabuleiro = [[0 for _ in range(4)] for _ in range(4)]
# print(tabuleiro)
print(backtrack(l=0, c=0, tab=tabuleiro, faltantes=4, q_p=[]))