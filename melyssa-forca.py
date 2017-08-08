#importando a biblioteca random
import random
#lista das possíveis palavras que serão sorteadas
palavras= []
#função que receberá as palavras 
def p():
    while True:
        palavrasnovas= input("Digite as palavras que você deseja que sejam usadas no jogo: ")# pede ao jogador para falar quais palavras ele quer 
        palavras.append(palavrasnovas)# adiciona a palavra que você digitou na lista
        if palavrasnovas== "":
            # comando para parar se o jogador não digitar nada
            break
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# o def define a função pricipal onde terá uma sequencia de comandos
def principal():
    """
    Função Princial do programa
    """
    #vai exibir na tela a palavra forca
    print('F O R C A')
    p()
    palavraSecreta = sortearPalavra()
    #atribui função à variável
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)

#se a condição for verdadeira, o while true vai executar todos os comandos que estão indentados nele
    while True:
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        #se a condição não for verdadeira, será exibido na tela você perdeu.
        if perdeuJogo():
            print('Voce Perdeu!!!')
            #o break corta o loop
            break
        #se a condição for verdadeira, será exibido na tela você ganhou.
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
        
def perdeuJogo():
    #o global mostra que essa variável criada vale no programa inteiro e não somente nessa função
    global FORCAIMG
    #o len mostra o tanto de caracteres tem dentro da lista
    if len(letrasErradas) == len(FORCAIMG):
        return True
    else:
        return False
    

def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
    for letra in palavraSecreta:
        #se a letra informada nao estiver entre as letras certas a variável ganhou é falsa.
        if letra not in letrasCertas:
            ganhou = False
    #o return chama a variável de novo
    return ganhou        
        

# função onde se recebe o palpite do jogador
def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
        #quando o jogador diz uma letra repetida 
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
        #quando o jogador não escolhe letras
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
    else:
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        #percorrre a lista para ver se a letra escolhida tem na palavra secreta
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()

#chama de volta a função principal
principal()
