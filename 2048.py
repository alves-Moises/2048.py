from main import main
import random
import copy

#******************************************************************************
#
#                             Trabalho
#                              2048
# 
#                             Grupo:
# 
#       Nome:                                                    DRE:
#
#      *João Gabriel de Oliveira Viana Garcia Justo              120042154
#      *Lucas Cuello de Medeiro                                  118196848
#      *Livia Campos da Silva                                    119095990
#
#
#******************************************************************************


def main():
    '''função principal'''

    def jogo():
        '''imprimir a matriz'''
        print('\n' * 20)
        print('=' * 50)
        maior = tabuleiro[0][0]
        for linha in tabuleiro:
            for elemento in linha:
                if elemento > maior:
                    maior = elemento
                    
        numEspacos = len(str(maior))
        
                    
        for linha in tabuleiro:
            linhaAtual = '|'
            for elemento in linha:
                if elemento == 0:
                    linhaAtual += ' ' * numEspacos + '|'
                else:
                    linhaAtual +=(' ' * (numEspacos - len(str(elemento))))+ str(elemento) + '|'
            print(linhaAtual)
        print()
    
    def pega_valor():
        '''entrada e validação de valor'''
        valid = False
        while not valid:
            try:
                x = int(input('Escolha a potência de 2 em que se deseja atingir a pontuação, (ex:.3 será 2**3 = 8): '))
            except ValueError:
                print('Valor inválido. Digite novamente.')
            else:
                valid = True
        return x

    def empurraLinhas(linha):
        '''movimenta os itens na matriz'''
        for i in range(3):
            for j in range(3,0,-1):
                if linha[j - 1] == 0:
                    linha[j - 1] = linha[j]
                    linha[j] = 0
        for j in range(3):
            if linha[j] == linha[j + 1]:
                linha[j] *= 2
                linha[j+1] = 0
        for j in range(3,0,-1):
            if linha[j-1] == 0:
                linha[j-1] = linha[j]
                linha[j] = 0
        return linha

    def empurraEsquerda(tabuleiroAtual):
        '''move os itens para a esquerda'''
        for j in range(4):
            tabuleiroAtual[j] = empurraLinhas(tabuleiroAtual[j])
        return tabuleiroAtual

    def inversa(linha):
        '''inverte a matriz'''
        novo = []
        for j in range(3, -1, -1):
            novo.append(linha[j])
        return novo

    def empurraDireita(tabuleiroAtual):
        '''move os intens para a direita'''
        for j in range(4):
            tabuleiroAtual[j] = inversa(tabuleiroAtual[j])
            tabuleiroAtual[j] = empurraLinhas(tabuleiroAtual[j])
            tabuleiroAtual[j] = inversa(tabuleiroAtual[j])
        return tabuleiroAtual

    def transposta(tabuleiroAtual):
        '''transportar os itens na matriz'''
        for i in range(4):
            for j in range(i,4):
                if not j == i:
                    trans = tabuleiroAtual[i][j]
                    tabuleiroAtual[i][j] = tabuleiroAtual[j][i]
                    tabuleiroAtual[j][i] = trans
        return tabuleiroAtual

    def empurraCima(tabuleiroAtual):
        '''move os itens para cima'''
        tabuleiroAtual = transposta(tabuleiroAtual)
        tabuleiroAtual = empurraEsquerda(tabuleiroAtual)
        tabuleiroAtual = transposta(tabuleiroAtual)
        return tabuleiroAtual

    def empurraBaixo(tabuleiroAtual):
        '''move para baixo'''
        tabuleiroAtual = transposta(tabuleiroAtual)
        tabuleiroAtual = empurraDireita(tabuleiroAtual)
        tabuleiroAtual = transposta(tabuleiroAtual)
        return tabuleiroAtual

    def novoValor():
        '''adicionar um novo valor a cada turno'''
        if random.randint(1,10) == 1:
            return 4
        else:
            return 2

    def addNovoValor():
        '''posição do novo valor na matriz'''
        linNum = random.randint(0, 3)
        colNum = random.randint(0, 3)
        while not tabuleiro[linNum][colNum] == 0:
            linNum = random.randint(0, 3)
            colNum = random.randint(0, 3)
        tabuleiro[linNum][colNum] = novoValor()

    def semMovimentos():
        '''verifica se não há movimentos disponíveis'''
        transTab1 = copy.deepcopy(tabuleiro)
        transTab2 = copy.deepcopy(tabuleiro)
        transTab1 = empurraBaixo(transTab1)
        if transTab1 == transTab2:
            transTab1 = empurraCima(transTab1)
            if transTab1 == transTab2:
                transTab1 = empurraEsquerda(transTab1)
                if transTab1 == transTab2:
                    transTab1 = empurraDireita(transTab1)
                    if transTab1 == transTab2:
                        return True
        return False

    def vitoria():
        '''verifica se atingiu a pontuação objetivo'''
        for linha in tabuleiro:
            if 2**int(x) in linha:
                return True      
        return False

    def pergunta_continua():
        '''pergunta ao usuário se quer continuar'''
        valid = False
        while not valid:
            y = str(input('Deseja continuar a jogar? [s] [n]  '))         
            y = y.lower()
            if (y[0] == 'n') or (y[0] == 's'):
                if y[0] == 'n':
                    print('Obrigado por jogar')
                    resposta = False
                    valid = True

                elif y[0] == 's':
                    print('continuando......')
                    resposta = True
                    valid = True

            else:
                print('Por favor digite uma resposta válida')
                
        return resposta
    
    def pergunta_recomeca():
        '''pergunta ao usuário se quer recomeçar'''
        valid = False
        while not valid:
            y = str(input('Deseja iniciar outro jogo? [s] [n]  '))         
            y = y.lower()
            if (y[0] == 'n') or (y[0] == 's'):
                if y[0] == 'n':
                    print('Obrigado por jogar')
                    valid = True
                elif y[0] == 's':
                    print('recomeçando...')
                    valid = True
                    main()
            else:
                print('Por favor digite uma resposta válida')
                
        return fimDeJogo

    ''' ================= inicio do jogo ======================= '''       

    tabuleiro = []
    for j in range(4):
        linha = []
        for i in range(4):
            linha.append(0)
        tabuleiro.append(linha)
    numPrec = 2
    
    while numPrec > 0:
        linNum = random.randint(0, 3)
        colNum = random.randint(0, 3)
        if tabuleiro[linNum][colNum] == 0:
            tabuleiro[linNum][colNum] = novoValor()
            numPrec -= 1
   
    print('Bem vindo ao jogo 2048! Seu objetivo é juntar as peças de mesmo valor até se chegar a 2048 (ou o valor selecionado).Para isso, para mover o tabuleiro à esquerda, use a tecla "a";para cima, use a tecla "w";para direita, usa a tecla "d"; para baixo, use a tecla "s". Divirta-se!!:')
    x  = pega_valor()
    if x == 0:
        x = 11
    jogo()
    fimDeJogo = False

    '''=================== jogo em looping ======================='''
    while not fimDeJogo:
        
        print("'q' para sair")
        print("'r' para recomeçar")
        print('=' * 50)
        
        movimento = str(input('Para qual lado deseja mover o tabuleiro? '))

        valida = True
        transTab = copy.deepcopy(tabuleiro)
        if movimento == 'd':
            tabuleiro = empurraDireita(tabuleiro)
        elif movimento == 'w':
            tabuleiro = empurraCima(tabuleiro)
        elif movimento == 'a':
            tabuleiro = empurraEsquerda(tabuleiro)
        elif movimento == 's':
            tabuleiro = empurraBaixo(tabuleiro)
        elif movimento.lower() == 'q':
            print('Encerrando...')
            fimDeJogo == True
            return
        elif movimento.lower() == 'r':
            print('Recomençando...')
            print('=' * 50, '\n')
            main()
        else:
            valida = False
        if not valida:
            print('Oops,tecla errada! Tente outra tecla válida!! ')
        else:
            
            if tabuleiro == transTab:
                print('Oops,tente uma direção diferente!! ')
            else:
                if vitoria != True:    
                    if vitoria():
                        vitoria = True
                        jogo()
                        print('Parabéns! Você venceu!! ')
                        if pergunta_continua():  #quer continuar?
                            addNovoValor()
                        else:
                            main()
                    else:
                        addNovoValor()
                else:
                    addNovoValor()
                    
            jogo()
            if semMovimentos():
                print('Vish, não há movimentos possíveis, você perdeu :( !')
                if not pergunta_recomeca():
                    fimDeJogo = True
                else:
                    main()
                fimDeJogo = True

main()