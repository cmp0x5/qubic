# Funções auxiliares que transformam posições entre coordenadas 
# (andar, linha, coluna) e número inteiro (entre 1 e 64)

def posicao(
    pos_int
    ):
    """
        Transforma a posição, dada em termos de um número inteiro 
        entre 1 e 64, e uma tupla de coordenadas.
    """
    pos_int -= 1
    posi = int(pos_int/16) #"andar"
    posj = int((pos_int%16)/4) #linha
    posk = int((pos_int%16)%4) #coluna
    return posi, posj, posk 

def pos_inteiro(
    posi,
    posj,
    posk
    ):
    """
        Transforma a posição, dada em termos de uma
        tupla de coordenadas, em um número inteiro.
    """
    return posi*16 + posj*4 + posk + 1 

# Funções de checagem

def checaLinha(
    tabuleiro
    ):
    """
        Checa se todos os elementos da linha são iguais a
        'X' ou 'O', retornando o caractere em caso afirmativo
        e retornando '' caso contrário
    """
    for andar in range(4):
        for linha in range(4):
            if tabuleiro[andar][linha][0] == 'X' and tabuleiro[andar][linha][1] == 'X' and tabuleiro[andar][linha][2] == 'X' and tabuleiro[andar][linha][3] == 'X':
                return 'X', 0, [andar,linha]
            if tabuleiro[andar][linha][0] == 'O' and tabuleiro[andar][linha][1] == 'O' and tabuleiro[andar][linha][2] == 'O' and tabuleiro[andar][linha][3] == 'O':
                return 'O', 0, [andar,linha]
    return ''

def checaColuna(
    tabuleiro
    ):
    """
        Checa se todos os elementos da coluna são iguais a
        'X' ou 'O', retornando o caractere em caso afirmativo
        e retornando '' caso contrário
    """
    for andar in range(4):
        for coluna in range(4):
            if tabuleiro[andar][0][coluna] == 'X' and tabuleiro[andar][1][coluna] == 'X' and tabuleiro[andar][2][coluna] == 'X' and tabuleiro[andar][3][coluna] == 'X':
                return 'X', 1, [andar,coluna]
            if tabuleiro[andar][0][coluna] == 'O' and tabuleiro[andar][1][coluna] == 'O' and tabuleiro[andar][2][coluna] == 'O' and tabuleiro[andar][3][coluna] == 'O':
                return 'O', 1, [andar,coluna]
    return ''

def checaDiagonal1(
    tabuleiro
    ):
    """
        Checa se todos os elementos da diagonal 1 (decrescente)
        são iguais a 'X' ou 'O', retornando o caractere em caso
        afirmativo e retornando '' caso contrário
    """
    for andar in range(4):
        if tabuleiro[andar][0][0] == 'X' and tabuleiro[andar][1][1] == 'X' and tabuleiro[andar][2][2] == 'X' and tabuleiro[andar][3][3] == 'X':
            return 'X', 2, [andar]
        if tabuleiro[andar][0][0] == 'O' and tabuleiro[andar][1][1] == 'O' and tabuleiro[andar][2][2] == 'O' and tabuleiro[andar][3][3] == 'O':
            return 'O', 2, [andar]
    return ''

def checaDiagonal2(
    tabuleiro
    ):
    """
        Checa se todos os elementos da diagonal 2 (crescente)
        são iguais a 'X' ou 'O', retornando o caractere em caso
        afirmativo e retornando '' caso contrário
    """
    for andar in range(4):
        if tabuleiro[andar][3][0] == 'X' and tabuleiro[andar][2][1] == 'X' and tabuleiro[andar][1][2] == 'X' and tabuleiro[andar][0][3] == 'X':
            return 'X', 3, [andar]
        if tabuleiro[andar][3][0] == 'O' and tabuleiro[andar][2][1] == 'O' and tabuleiro[andar][1][2] == 'O' and tabuleiro[andar][0][3] == 'O':
            return 'O', 3, [andar]
    return ''

def checaLinha3D1(
    tabuleiro
    ):
    """
        Checa se todos os elementos da linha 3D 1 (decrescente)
        são iguais a 'X' ou 'O', retornando o caractere em caso
        afirmativo e retornando '' caso contrário
    """
    for linha in range(4):
        if tabuleiro[0][linha][0] == 'X' and tabuleiro[1][linha][1] == 'X' and tabuleiro[2][linha][2] == 'X' and tabuleiro[3][linha][3] == 'X':
            return 'X', 4, [linha]
        if tabuleiro[0][linha][0] == 'O' and tabuleiro[1][linha][1] == 'O' and tabuleiro[2][linha][2] == 'O' and tabuleiro[3][linha][3] == 'O':
            return 'O', 4, [linha]   
    return ''

def checaLinha3D2(
    tabuleiro
    ):
    """
        Checa se todos os elementos da linha 3D 2 (crescente)
        são iguais a 'X' ou 'O', retornando o caractere em caso
        afirmativo e retornando '' caso contrário
    """
    for linha in range(4):
        if tabuleiro[3][linha][0] == 'X' and tabuleiro[2][linha][1] == 'X' and tabuleiro[1][linha][2] == 'X' and tabuleiro[0][linha][3] == 'X':
            return 'X', 5, [linha]
        if tabuleiro[3][linha][0] == 'O' and tabuleiro[2][linha][1] == 'O' and tabuleiro[1][linha][2] == 'O' and tabuleiro[0][linha][3] == 'O':
            return 'O', 5, [linha]
    return ''

def checaColuna3D1(
    tabuleiro
    ):
    """
        Checa se todos os elementos da coluna 3D 1 (decrescente)
        são iguais a 'X' ou 'O', retornando o caractere em caso
        afirmativo e retornando '' caso contrário
    """
    for coluna in range(4):
        if tabuleiro[0][0][coluna] == 'X' and tabuleiro[1][1][coluna] == 'X' and tabuleiro[2][2][coluna] == 'X' and tabuleiro[3][3][coluna] == 'X':
            return 'X', 6, [coluna]
        if tabuleiro[0][0][coluna] == 'O' and tabuleiro[1][1][coluna] == 'O' and tabuleiro[2][2][coluna] == 'O' and tabuleiro[3][3][coluna] == 'O':
            return 'O', 6, [coluna]
    return ''

def checaColuna3D2(
    tabuleiro
    ):
    """
        Checa se todos os elementos da coluna 3D 2 (crescente)
        são iguais a 'X' ou 'O', retornando o caractere em caso
        afirmativo e retornando '' caso contrário
    """
    for coluna in range(4):
        if tabuleiro[3][0][coluna] == 'X' and tabuleiro[2][1][coluna] == 'X' and tabuleiro[1][2][coluna] == 'X' and tabuleiro[0][3][coluna] == 'X':
            return 'X', 7, [coluna] 
        if tabuleiro[3][0][coluna] == 'O' and tabuleiro[2][1][coluna] == 'O' and tabuleiro[1][2][coluna] == 'O' and tabuleiro[0][3][coluna] == 'O':
            return 'O', 7, [coluna]
    return ''

def checaPilar(
    tabuleiro
    ):
    """
        Checa se todos os elementos da coluna são iguais a
        'X' ou 'O', retornando o caractere em caso afirmativo
        e retornando '' caso contrário
    """
    for linha in range(4):
        for coluna in range(4):
            if tabuleiro[0][linha][coluna] == 'X' and tabuleiro[1][linha][coluna] == 'X' and tabuleiro[2][linha][coluna] == 'X' and tabuleiro[3][linha][coluna] == 'X':
                return 'X', 8, [linha,coluna]
            if tabuleiro[0][linha][coluna] == 'O' and tabuleiro[1][linha][coluna] == 'O' and tabuleiro[2][linha][coluna] == 'O' and tabuleiro[3][linha][coluna] == 'O':
                return 'O', 8, [linha,coluna]
    return ''

def checaDiagonal3D1(
    tabuleiro
    ):
    """
        Checa se todos os elementos da diagonal 3D 1 (decrescente|decrescente)
        são iguais a 'X' ou 'O', retornando o caractere em caso
        afirmativo e retornando '' caso contrário
    """   
    if tabuleiro[0][0][0] == 'X' and tabuleiro[1][1][1] == 'X' and tabuleiro[2][2][2] == 'X' and tabuleiro[3][3][3] == 'X':
        return 'X', 9
    if tabuleiro[0][0][0] == 'O' and tabuleiro[1][1][1] == 'O' and tabuleiro[2][2][2] == 'O' and tabuleiro[3][3][3] == 'O':
        return 'O', 9 
    return ''

def checaDiagonal3D2(
    tabuleiro
    ):
    """
        Checa se todos os elementos da diagonal 3D 2 (crescente|crescente)
        são iguais a 'X' ou 'O', retornando o caractere em caso
        afirmativo e retornando '' caso contrário
    """   
    if tabuleiro[3][3][0] == 'X' and tabuleiro[2][2][1] == 'X' and tabuleiro[1][1][2] == 'X' and tabuleiro[0][0][3] == 'X':
        return 'X', 10
    if tabuleiro[3][3][0] == 'O' and tabuleiro[2][2][1] == 'O' and tabuleiro[1][1][2] == 'O' and tabuleiro[0][0][3] == 'O':
        return 'O', 10
    return ''

def checaDiagonal3D3(
    tabuleiro
    ):
    """
        Checa se todos os elementos da diagonal 3D 3 (crescente|decrescente)
        são iguais a 'X' ou 'O', retornando o caractere em caso
        afirmativo e retornando '' caso contrário
    """   
    if tabuleiro[3][0][0] == 'X' and tabuleiro[2][1][1] == 'X' and tabuleiro[1][2][2] == 'X' and tabuleiro[0][3][3] == 'X':
        return 'X', 11
    if tabuleiro[3][0][0] == 'O' and tabuleiro[2][1][1] == 'O' and tabuleiro[1][2][2] == 'O' and tabuleiro[0][3][3] == 'O':
        return 'O', 11
    return ''

def checaDiagonal3D4(
    tabuleiro
    ):
    """
        Checa se todos os elementos da diagonal 3D 4 (decrescente|crescente)
        são iguais a 'X' ou 'O', retornando o caractere em caso
        afirmativo e retornando '' caso contrário
    """   
    if tabuleiro[0][3][0] == 'X' and tabuleiro[1][2][1] == 'X' and tabuleiro[2][1][2] == 'X' and tabuleiro[3][0][3] == 'X':
        return 'X', 12
    if tabuleiro[0][3][0] == 'O' and tabuleiro[1][2][1] == 'O' and tabuleiro[2][1][2] == 'O' and tabuleiro[3][0][3] == 'O':
        return 'O', 12
    return ''

def checagem(
    n,
    tabuleiro
    ):
    """
        Dicionario de funções de checagem 
    """
    dicionario_checagem = {
        0: checaLinha(tabuleiro),
        1: checaColuna(tabuleiro),
        2: checaDiagonal1(tabuleiro),
        3: checaDiagonal2(tabuleiro),
        4: checaLinha3D1(tabuleiro),
        5: checaLinha3D2(tabuleiro),
        6: checaColuna3D1(tabuleiro),
        7: checaColuna3D2(tabuleiro),
        8: checaPilar(tabuleiro),
        9: checaDiagonal3D1(tabuleiro),
        10: checaDiagonal3D2(tabuleiro),
        11: checaDiagonal3D3(tabuleiro),
        12: checaDiagonal3D4(tabuleiro)
    }
    return dicionario_checagem.get(n)

def sequenciaVencedora(
    tipo,
    arg=''
    ):
    """
        Função que devolve as posições da sequência vencedora 
    """
    dicionario_sequencias = {
        0: [pos_inteiro(arg[0],arg[1],0),pos_inteiro(arg[0],arg[1],1),pos_inteiro(arg[0],arg[1],2),pos_inteiro(arg[0],arg[1],3)],
        1: [pos_inteiro(arg[0],0,arg[1]),pos_inteiro(arg[0],1,arg[1]),pos_inteiro(arg[0],2,arg[1]),pos_inteiro(arg[0],3,arg[1])],
        2: [pos_inteiro(arg[0],0,0),pos_inteiro(arg[0],1,1),pos_inteiro(arg[0],2,2),pos_inteiro(arg[0],3,3)],
        3: [pos_inteiro(arg[0],3,0),pos_inteiro(arg[0],2,1),pos_inteiro(arg[0],1,2),pos_inteiro(arg[0],0,3)],
        4: [pos_inteiro(0,arg[0],0),pos_inteiro(1,arg[0],1),pos_inteiro(2,arg[0],2),pos_inteiro(3,arg[0],3)],
        5: [pos_inteiro(3,arg[0],0),pos_inteiro(2,arg[0],1),pos_inteiro(1,arg[0],2),pos_inteiro(0,arg[0],3)],
        6: [pos_inteiro(0,0,arg[0]),pos_inteiro(1,1,arg[0]),pos_inteiro(2,2,arg[0]),pos_inteiro(3,3,arg[0])],
        7: [pos_inteiro(3,0,arg[0]),pos_inteiro(2,1,arg[0]),pos_inteiro(1,2,arg[0]),pos_inteiro(0,3,arg[0])],
        8: [pos_inteiro(0,arg[0],arg[1]),pos_inteiro(1,arg[0],arg[1]),pos_inteiro(2,arg[0],arg[1]),pos_inteiro(3,arg[0],arg[1])],
        9: [pos_inteiro(0,0,0),pos_inteiro(1,1,1),pos_inteiro(2,2,2),pos_inteiro(3,3,3)],
        10: [pos_inteiro(3,3,0),pos_inteiro(2,2,1),pos_inteiro(1,1,2),pos_inteiro(0,0,3)],
        11: [pos_inteiro(3,0,0),pos_inteiro(2,1,1),pos_inteiro(1,2,2),pos_inteiro(0,3,3)],
        12: [pos_inteiro(0,3,0),pos_inteiro(1,2,1),pos_inteiro(2,1,2),pos_inteiro(3,0,3)]
        }
    return dicionario_sequencias.get(tipo)


def checa_tabuleiro(
    tabuleiro
    ):
    n = 0
    resultado = ''
    while resultado == '':
        resultado = checagem(n,tabuleiro)
        n += 1
    if resultado != None:
        if resultado[1] < 2:
            return resultado[0], sequenciaVencedora(resultado[1],resultado[2])
        if resultado[1] < 8:
            return resultado[0], sequenciaVencedora(resultado[1],[resultado[2][0],0])
        if resultado[1] == 8:
            return resultado[0], sequenciaVencedora(resultado[1],resultado[2])
        else:
            return resultado[0], sequenciaVencedora(resultado[1],[0,0])
    return resultado
