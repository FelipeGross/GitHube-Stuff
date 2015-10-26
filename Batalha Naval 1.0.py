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
        
print ("\nBatalha Naval \nBem Vindo & Boa Sorte!\n")
print_mapa(mapa)

def random_tudo(mapa):
    l = randint(0, len(mapa) - 1)
    c = randint(0, len(mapa[0]) - 1)
    x=[l,c]
    return x    
print (random_tudo(mapa))

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
    print (tamanho)    
    return mapa_pc1
        

def posicao(navios):
    mapa_pc = []
    for x in range(15):
        mapa_pc.append(["~"]*15)
    for i in navios:
        mapa_pc = navio_inteiro(i, mapa_pc)
    
        
    return mapa_pc
        
        
mapa_pc = posicao(navios)
print(mapa_pc)


for rodada in range(30):
    print ("Rodada", rodada + 1)
    
    l_guess = int(input("\nFileira:\n"))
    c_guess = int(input("Coluna:\n"))

    if mapa_pc[l_guess][c_guess] != "~":
        print ("Acertou meu navio!")
        barco = mapa_pc[l_guess][c_guess]
        tamanho_barco[barco] -= 1
        
        if tamanho_barco[barco]==0:
            print ("Afundou meu Navio!")
            placar += pontos_barcos[barco]
        mapa_pc[l_guess][c_guess] = "A"
        mapa[l_guess][c_guess] = "X"
        print ("Placar: ",placar)

        
    else:
        if (l_guess < 0 or l_guess > 15) or (c_guess < 0 or c_guess > 15):
            print ("Fora da area! Jogue novamente")
        elif(mapa_pc[l_guess][c_guess] == "A" or mapa[l_guess][c_guess] == "o"):
            print ("Ja atirou ai!")
        else:
            print ("Errou!\n")
            mapa[l_guess][c_guess] = "o"
    print_mapa(mapa)

