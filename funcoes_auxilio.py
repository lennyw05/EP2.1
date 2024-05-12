import random
import constantes


def cria_mapa(N):
    matriz = []
    for x in range(N):
       matriz.append([' ']*(N))
    return matriz

def posicao_suporta(mapa,blocos,linha,coluna,vh):
    if vh == "h":
        if (coluna)+blocos > len(mapa[linha]):
            return False
    else:
        if (linha)+blocos > len(mapa):
            return False

    for i in range(blocos):
        if vh == "h":
            if mapa[linha][coluna+i] == "N":
                return False
        else:
            if mapa[linha+i][coluna] == "N":
                return False
    
    return True

def aloca_navios(mapa,listablocos):
    for i in range(len(listablocos)):

        pode = False
        while pode == False:
            linha = random.randint(0, (len(mapa)-1))
            coluna = random.randint(0, (len(mapa)-1))
            orientacao = random.choice(['h', 'v'])
            pode = posicao_suporta(mapa,listablocos[i],linha,coluna,orientacao)

        mapa = aloca_navio_jogador(mapa,listablocos[i],linha,coluna,orientacao)

    return mapa

def aloca_navio_jogador(mapa,navio,linha,coluna,orientacao):
    for x in range(navio):
        if orientacao == "h":
            mapa[linha][coluna+x] = "N"
        else:
            mapa[linha+x][coluna] = "N"
    return mapa

def foi_derrotado(matriz):
    for z in matriz:
        for j in z:
            if j == "N":
                return False
    return True



def printar_mapas(matriz_computer,matriz_player):
    print(" ")
    print("           Mapa do Adversário                                  Seu Mapa")            
    print("    A   B   C   D   E   F   G   H   I   J         A   B   C   D   E   F   G   H   I   J")
    for lista_x in range(len(matriz_computer)):
        linha = ""
        linha+=str(lista_x+1)
        for elem in range(len(matriz_computer[lista_x])):
            if matriz_computer[lista_x][elem] == "X":
                if lista_x == 9 and elem == 0:
                    linha+=("  "+"\u001b[31m"+(matriz_computer[lista_x][elem])+"\u001b[0m")
                   
                else:
                    linha+=("   "+"\u001b[31m"+(matriz_computer[lista_x][elem])+"\u001b[0m")

            elif matriz_computer[lista_x][elem] == "A":
                if lista_x == 9 and elem == 0:
                    linha+=("  "+"\u001b[34m"+(matriz_computer[lista_x][elem])+"\u001b[0m")
                   
                else:
                    linha+=("   "+"\u001b[34m"+(matriz_computer[lista_x][elem])+"\u001b[0m")
                   
            else:
                if lista_x == 9 and elem == 0:
                    linha+=("  "+(" "))
                else:
                    linha+=("   "+(" "))

        linha+=" "+str(lista_x+1)
        if lista_x == 9:
            linha+=("  ")
        else:
            linha+=("   ")
        
        linha+=str(lista_x+1)
        
        for elem in range(len(matriz_player[lista_x])):
            if matriz_player[lista_x][elem] == "X":
                if lista_x == 9 and elem == 0:
                    linha+=("  "+"\u001b[31m"+(matriz_player[lista_x][elem])+"\u001b[0m")
                
                else:
                    linha+=("   "+"\u001b[31m"+(matriz_player[lista_x][elem])+"\u001b[0m")
            elif matriz_player[lista_x][elem] == "A":
                if lista_x == 9 and elem == 0:
                    linha+=("  "+"\u001b[34m"+(matriz_player[lista_x][elem])+"\u001b[0m")
                
                else:
                    linha+=("   "+"\u001b[34m"+(matriz_player[lista_x][elem])+"\u001b[0m")
            else:
                if lista_x == 9 and elem == 0:
                    linha+=("  "+"\u001b[32m"+(matriz_player[lista_x][elem])+"\u001b[0m")
                
                else:
                    linha+=("   "+"\u001b[32m"+(matriz_player[lista_x][elem])+"\u001b[0m")
                
        linha+=" "+str(lista_x+1)

        print(linha)
    print("    A   B   C   D   E   F   G   H   I   J         A   B   C   D   E   F   G   H   I   J")
    print(" ")

import time
def rodada(inica,mapa_computer,mapa_player,jogando):
    if inicia == "pc":
        print("Computador Jogando...")
        novo = False
        while novo == False:
            ataque_Linha = random.randint(0,len(mapa_player)-1)
            ataque_Coluna = random.randint(0,len(mapa_player)-1)
            novo = mapa_player[ataque_Linha][ataque_Coluna] == "N" or  mapa_player[ataque_Linha][ataque_Coluna] == " "
            if mapa_player[ataque_Linha][ataque_Coluna] == "N":
                mapa_player[ataque_Linha][ataque_Coluna] = "X"
                print("BOOOOOOOM!!! O computador acertou um navio!")
            elif mapa_player[ataque_Linha][ataque_Coluna] == " ":
                mapa_player[ataque_Linha][ataque_Coluna] = "A"
                print("ERROOOUU! O tiro caiu na água!")

        jogando_player = Checar_se_acabou(jogando,mapa_player)
        
        time.sleep(2)
        print("É sua vez de jogar!!")
        time.sleep(1)
        novo = False
        while novo == False:
            coluna = input("Qual coluna você quer atacar?").upper()
            if coluna not in constantes.Letras:
                print("Coluna Invalida. Tente novamente.")
                continue
            linha = input("Qual linha você quer atacar?")
            if linha.isnumeric() and int(linha) <= 10 and int(linha) >= 1:
                pass
            
            else:
                print("Linha Invalida. Tente novamente.")
                continue

            linha = int(linha)-1
            coluna = ord(coluna)-ord("A")
            novo = mapa_computer[linha][coluna] == "N" or  mapa_computer[linha][coluna] == " "
            if novo == False:
                print("Ataque inválido, tente novamente.")
        if mapa_computer[linha][coluna] == "N":
            mapa_computer[linha][coluna] = "X"
            print("BOOOOOOM!!!!! Você acertou um navio! Ótima jogada!")
        elif mapa_computer[linha][coluna] == " ":
            mapa_computer[linha][coluna] = "A"
            print("ERROOOU! O tiro caiu na água! Continue tentando!")

        jogando_computer = Checar_se_acabou(jogando,mapa_computer)
        time.sleep(2)
    else:
        print("Sua vez de jogar!")
        time.sleep(1)
        novo = False
        while novo == False:
            coluna = input("Qual coluna você quer atacar?").upper()
            if coluna not in constantes.Letras:
                print("Coluna Invalida. Tente novamente.")
                continue
            linha = input("Qual linha você quer atacar?")
            if linha.isnumeric() and int(linha) <= 10 and int(linha) >= 1:
                pass
            
            else:
                print("Linha Invalida. Tente novamente.")
                continue
            linha = int(linha)-1
            coluna = ord(coluna)-ord("A")
            novo = mapa_computer[linha][coluna] == "N" or  mapa_computer[linha][coluna] == " "
            if novo == False:
                print("Ataque inválido, tente novamente.")
        if mapa_computer[linha][coluna] == "N":
            mapa_computer[linha][coluna] = "X"
            print("BOOOOOOM!!!!! Você acertou um navio! Ótima jogada!")
        elif mapa_computer[linha][coluna] == " ":
            mapa_computer[linha][coluna] = "A"
            print("ERROOOU! O tiro caiu na água! Continue tentando!")
        
        jogando_computer = Checar_se_acabou(jogando,mapa_computer)
        time.sleep(2)
        novo = False
        print("Computador Jogando...")
        while novo == False:
            ataque_Linha = random.randint(0,len(mapa_player)-1)
            ataque_Coluna = random.randint(0,len(mapa_player)-1)
            novo = mapa_player[ataque_Linha][ataque_Coluna] == "N" or  mapa_player[ataque_Linha][ataque_Coluna] == " "
            if mapa_player[ataque_Linha][ataque_Coluna] == "N":
                mapa_player[ataque_Linha][ataque_Coluna] = "X"
                print("BOOOOOOM!!! O computador acertou um navio!")
            elif mapa_player[ataque_Linha][ataque_Coluna] == " ":
                mapa_player[ataque_Linha][ataque_Coluna] = "A"
                print("ERROOOU! O tiro caiu na água!")

        
        time.sleep(2)
        
        jogando_player = Checar_se_acabou(jogando,mapa_player)
    
    jogando = jogando_player and jogando_computer
    return mapa_computer,mapa_player,jogando


def Checar_se_acabou(jogando,mapa):
    for linha in mapa:
            if "N" in linha:
                jogando = True
                return jogando
            else:
                jogando = False
    
    return jogando
