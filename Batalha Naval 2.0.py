from random import randint
import copy

mapa = []

tamanho_barco = {6:6,
                 5:5,
                 4:4,
                 3:3,
                 2:2,
                 1:1}
 
pontos_barcos = {6:15,
                 5:10,
                 4:7,
                 3:5,
                 2:3,
                 1:2}

placar = 0

for x in range(15):
    mapa.append(["~"] * 15)
mapa_pc = mapa

def print_mapa(mapa):
    for row in mapa:
        print (" ".join(row))
        
print ("\nBatalha Naval\n\nBem Vindo!\n\nCuidado! Se voce errar mais de 40 vezes: FIM DE JOGO!\n\nSe voce acertar todos os navios: PARABENS! VOCE GANHOU O JOGO!\n\nInsira valores de 1 a 15 para fileiras e colunas\n\nBoa Sorte!\n")
print_mapa(mapa)

def random_tudo(mapa):
    l = randint(0, len(mapa) - 1)
    c = randint(0, len(mapa[0]) - 1)
    x=[l,c]
    return x    
#print (random_tudo(mapa))

def random_pos():
    p = randint(0,1) # 0 = vertical; 1= horaizontal
    return p
navios=[6,5,4,3,2,1] #Tamanho dos Navios


def navio_inteiro(tamanho, mapa_pc):
    p = random_pos()
    x = random_tudo(mapa)
    mapa_pc1 = copy.deepcopy(mapa_pc)
    
   
    try:
        for j in range(tamanho):
            if p == 0:
                while x[0]+tamanho > 15:
                    x=random_tudo(mapa)
                if mapa_pc1[x[0]+j][x[1]] == "~":
                    mapa_pc1[x[0]+j][x[1]] = tamanho
                else:
                    return navio_inteiro(tamanho,mapa_pc)
            else:
                while x[1]+tamanho > 15:
                    x=random_tudo(mapa)
                if mapa_pc1[x[0]+j][x[1]] == "~":
                    mapa_pc1[x[0]][x[1]+j] = tamanho
                else:
                    return navio_inteiro(tamanho,mapa_pc)
        
    except:
        return navio_inteiro(tamanho, mapa_pc)
#    print (tamanho)    
    return mapa_pc1
        

def posicao(navios):
    mapa_pc = []
    for x in range(15):
        mapa_pc.append(["~"]*15)
    for i in navios:
        mapa_pc = navio_inteiro(i, mapa_pc)
    
        
    return mapa_pc
        
        
mapa_pc = posicao(navios)
#print(mapa_pc)

erro = 0
rodada = 1
acertos = 0

while erro <= 59:
    print ("\nRodada", rodada)
    print ("\nPlacar:",placar)
            
    l_guess = int(input("\nLinha:\n")) -1
    c_guess = int(input("Coluna:\n")) - 1


    if l_guess < 0 or l_guess > 15 or c_guess < 0 or c_guess > 15:
        print ("\nFora da area! Jogue novamente\n")

    else:
        if(mapa[l_guess][c_guess] == "X" or mapa[l_guess][c_guess] == "o"):
            print ("\nJa atirou ai!\n")
        
        elif mapa_pc[l_guess][c_guess] == "~":
            print ("\nErrou!\n")
            mapa[l_guess][c_guess] = "o"
            erro += 1
    
        if mapa_pc[l_guess][c_guess] != "~":
            print ("\nAcertou meu navio!\n")
            barco = mapa_pc[l_guess][c_guess]
            tamanho_barco[barco] -= 1
            
            if tamanho_barco[barco]==0:
                print ("\nAfundou meu navio!\n")
                placar += pontos_barcos[barco]
            mapa[l_guess][c_guess] = "X"
    if placar == 41:
        print ("\nPARABENS! VOCE GANHOU O JOGO!\n")
        break
    
    print ("Total de Erros:\n",erro)
    rodada += 1
    

    print_mapa(mapa)
print ("\nFIM DE JOGO!\n")

