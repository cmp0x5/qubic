import checa

class Tabuleiro:
    """
        Objeto tabuleiro 4x4x4
    """
    def __init__(
        self
        ):
        """
            Controi e inicializa tabuleiro vazio (caractere nulo '')
        """
        self.tab = [[['','','',''],
                     ['','','',''],
                     ['','','',''],
                     ['','','','']],
                    [['','','',''],
                     ['','','',''],
                     ['','','',''],
                     ['','','','']],
                    [['','','',''],
                     ['','','',''],
                     ['','','',''],
                     ['','','','']],
                    [['','','',''],
                     ['','','',''],
                     ['','','',''],
                     ['','','','']]]
    
    def insereItem(
        self,
        item,
        pos
        ):
        """
            Insere um item (item - caractere 'X' ou 'O' - na posição pos (inteiro entre 1 e 64))
        """
        posi, posj, posk = checa.posicao(pos)[0], checa.posicao(pos)[1], checa.posicao(pos)[2]
        self.tab[posi][posj][posk] = item

    def checaTab(
        self
        ):
        """
            Checa tabuleiro
        """
        return checa.checa_tabuleiro(self.tab)

    def reiniciaTab(
        self
        ):
        """
            Reinicia tabuleiro (caractere nulo '')
        """
        self.tab = [[['','','',''],
                     ['','','',''],
                     ['','','',''],
                     ['','','','']],
                    [['','','',''],
                     ['','','',''],
                     ['','','',''],
                     ['','','','']],
                    [['','','',''],
                     ['','','',''],
                     ['','','',''],
                     ['','','','']],
                    [['','','',''],
                     ['','','',''],
                     ['','','',''],
                     ['','','','']]]
    def checa_posicao(self, pos):
        posi, posj, posk = checa.posicao(pos)[0], checa.posicao(pos)[1], checa.posicao(pos)[2]
        return self.tab[posi][posj][posk]
