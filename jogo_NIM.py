
# funcao que inicia o jogo e determina se sera uma partida isolada ou um campeonato
def main():
    print("Bem vindo ao jogo do NIM! Escolha: ","\n1 - para jogar uma partida isolada", "\n2 - para jogar um compeonato (3 partidas)")
    jogo = int(input())
    if jogo == 2:
        print("Você escolheu um campeonato!")
        campeonato()
    elif jogo == 1:
        print("Você escolheu uma partida isolada.")
        partida()
    else: 
        print("Comando inválido.")

# funcao que inicia o campeonato
def campeonato():
    rodada = 1
    while rodada <= 3:
        print('**** Rodada', rodada,"****")
        partida()
        rodada +=1
    print('Placar: Você 0 x 3 Computador')

# funcao que inicia uma partida
def partida():
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    computador = False #dispositivo para intercalar as jogadas

    #verificar quem vai começar
    if n  % (m + 1) == 0: #verificando estrategia vencedora
        print("Voce começa!")  
    else:
        print("Computador começa!")
        computador = True

    
    while n > 0:
        
        #determinar a vez de quem na partida
        if computador:
            y = computador_escolhe_jogada(n, m)
            n -= y #retirar do total o numero de peças escolhidas pelo computador
            if y == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", y, "peças.")
            computador = False
        else:
            x = usuario_escolhe_jogada(n, m)
            n -= x #retirar do total o numero de peças escolhidas pelo usuario
            if x == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou", x, "peças.")
            computador = True
        
        #verifica quantas peças há no tabuleiro
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else: 
            print("Agora restam apenas", n, "peças no tabuleiro.")

    print("Fim do jogo! O computador ganhou!")


# funcao que executa a vez do computador
def computador_escolhe_jogada(n,m):
    y = 1 #y = numero de peças que o computador vai escolher
    while y <= m:
        if (n - y) % (m + 1) == 0: #verificando estrategia vencedora para o computador 
            return y
        else:
            y += 1

# funcao que executa a vez do usuario
def usuario_escolhe_jogada(n, m):
    usuario = True
    while usuario:
        x = int(input("Quantas peças você vai tirar? "))
        if  x > m or x <1:
            print("Oops ! Jogada inválida! Tente de novo.")
        else:
            usuario = False
    return x

main()