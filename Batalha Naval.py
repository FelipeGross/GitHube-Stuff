from random import randint
import copy

n = 0
while n < 6:
    try:
        n = int(input("Digite um numero para o total de linhas e colunas. Lembre-se: Quanto maior o \nnumero, maior a dificuldade do jogo.\n\nOBS: O numero deve ser maior do que 6.\n"))
    except:
        print("Use algarismos inteiros")
        
print ("\n-----------------------------------------------------\n")
mapa = []

#pontos_barcos = open('p_barcos.txt', 'r')
#tamanho_barco = open('c_barcos.txt', 'r')


tamanho_barco = eval(open('c_barcos.txt', 'r').read())
#pontos_barcos = eval(open('p_barcos.txt', 'r').read())

#pontos_barcos = open('p_barcos.txt', 'r')
#my_dict = eval(pontos_barcos.read())

#tamanho_barco = open('c_barcos.txt', 'r')
#my_dict = eval(tamanho_barco.read())

#tamanho_barco = {6:6,
#                 5:5,
#                 4:4,
#                 3:3,
#                 2:2,
#                 1:1}

pontos_barcos = {6:15,
                 5:10,
                 4:7,
                 3:5,
                 2:3,
                 1:1}

placar = 0

z = []

for g in range(n):
   z.append(g+1)

s = 0

for f in range(n):
    mapa.append (["~"] * n)
  
mapa_pc = mapa

def print_mapa(s, mapa):
    for row in mapa:
        print (" ".join(row), z[s])
        s += 1
print ("Batalha Naval\n\nBem Vindo!\n\nHá 6 navios no mapa abaixo.\nCada um tem sua medida variando de 1 a 6 pontos no mapa.\n\nSe você acertar todos: PARABÉNS! VOCÊ GANHOU O JOGO!\n\nBoa Sorte!\n\nInsira um valor de 1 a", n,"para linhas e pressione a tecla Enter.\nInsira um valor de 1 a", n, "para colunas e aperte Enter.\n\nTenha um bom divertimento!\n")

if n*n > n*5 + 21:
    print ("Lembre-se: Você só podera errar",n*5, "vezes.\n")

def random_tudo(mapa):
    l = randint(0, len(mapa) - 1)
    c = randint(0, len(mapa) - 1)
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
                while x[0]+tamanho > n:
                    x=random_tudo(mapa)
                if mapa_pc1[x[0]+j][x[1]] == "~":
                    mapa_pc1[x[0]+j][x[1]] = tamanho
                else:
                    return navio_inteiro(tamanho,mapa_pc)
            else:
                while x[1]+tamanho > n:
                    x=random_tudo(mapa)
                if mapa_pc1[x[0]][x[1]+j] == "~":
                    mapa_pc1[x[0]][x[1]+j] = tamanho
                else:
                    return navio_inteiro(tamanho,mapa_pc)
        
    except:
        return navio_inteiro(tamanho, mapa_pc)
    #print (tamanho)    
    return mapa_pc1
        

def posicao(navios):
    mapa_pc = []
    for x in range(n):
        mapa_pc.append(["~"]*n)
    for i in navios:
        mapa_pc = navio_inteiro(i, mapa_pc)
    
        
    return mapa_pc
        
        
mapa_pc = posicao(navios)
print(mapa_pc)

erro = n*5
rodada = 1
acertos = 0

while erro > 0 :
    
    if placar == 41:
        print ("Você afundou todos os meus navios!")        
        print ("\nPARABÉNS! VOCÊ GANHOU O JOGO!\n")
        break    

    print ("\nRodada", rodada,"    Placar:",placar,"\n")
    print_mapa(s, mapa)
            
    l_guess = int(input("\nLinha:\n")) -1
    while l_guess < 0 or l_guess > n-1:
        print ("\nFora da área! Jogue novamente\n")
        l_guess = int(input("\nLinha:\n")) -1
        
    c_guess = int(input("Coluna:\n")) - 1
    while c_guess < 0 or c_guess > n-1:
        print ("\nFora da área! Jogue novamente\n")    
        c_guess = int(input("Coluna:\n")) - 1
        
    print ("\n-----------------------------------------------------")
    print ("Rodada",rodada, "    Placar:",placar)

    if(mapa[l_guess][c_guess] == "X" or mapa[l_guess][c_guess] == "o"):
            print ("\nJá atirou ai! Jogue novamente")
            
    else:    
        if mapa_pc[l_guess][c_guess] == "~":
            print ("\nÁgua!")
            mapa[l_guess][c_guess] = "o"
            erro -= 1
    
        elif mapa_pc[l_guess][c_guess] != "~":
            print ("\nAcertou meu navio!")
            barco = mapa_pc[l_guess][c_guess]
            tamanho_barco[barco] -= 1
            
            if tamanho_barco[barco]==0:
                print ("\nAfundou meu navio!")
                placar += pontos_barcos[barco]
            mapa[l_guess][c_guess] = "X"
    
        if n*n > n*5 + 21:    
            print ("\nChances de Errar:",erro)
    print ("-----------------------------------------------------\n")
    rodada += 1
    
print ("Acabaram suas chances!\n","\nFIM DE JOGO!\n")