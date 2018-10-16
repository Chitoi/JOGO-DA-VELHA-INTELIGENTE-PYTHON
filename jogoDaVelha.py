import random

tabuleiro = [[0,0,0], [0,0,0], [0,0,0]]
jogo_atual = 0
cont2=0

#-----------inicia tabuleiro ---------
def imprime_tabuleiro():
    cont=1
    for l in range(0,3):
        for c in range(0,3):
            if tabuleiro[l][c] == 0:
                print(f'[{cont:^5}]', end='' )
            elif tabuleiro[l][c]==1:
                print(f'[{"X":^5}]', end='')
            elif tabuleiro[l][c]==2:
                print(f'[{"O":^5}]', end='')
            cont+=1
        print()
#------------------//---------------------------#

#----------verifica tabuleiro completo ----------------
def tabuleiro_completo():

    aux=1
    for l in range(0,3):
        for c in range(0,3):
            if tabuleiro[l][c]==0:
                aux=0
    return aux
#-------------------------------//---------------

#------------verifica jogada valida ----------------------------
def verifica_jogada(jogada, jogador):
    if jogada == 1:
        if tabuleiro[0][0] == 0:
            tabuleiro[0][0]=jogador
            return 1
        else:
            return 0
        
    elif jogada == 2:
        if tabuleiro[0][1] == 0:
            tabuleiro[0][1] = jogador
            return 1
        else:
            return 0

    elif jogada == 3:
        if tabuleiro[0][2] == 0:
            tabuleiro[0][2] = jogador
            return 1
        else:
            return 0

    elif jogada == 4:
        if tabuleiro[1][0] == 0:
            tabuleiro[1][0] = jogador
            return 1
        else:
            return 0

    elif jogada == 5:
        if tabuleiro[1][1] == 0:
            tabuleiro[1][1] = jogador
            return 1
        else:
            return 0
    
    elif jogada == 6:
        if tabuleiro[1][2] == 0:
            tabuleiro[1][2] = jogador
            return 1
        else:
            return 0
    
    elif jogada == 7:
        if tabuleiro[2][0] == 0:
            tabuleiro[2][0] = jogador
            return 1
        else:
            return 0
    
    elif jogada == 8:
        if tabuleiro[2][1] == 0:
            tabuleiro[2][1] = jogador
            return 1
        else:
            return 0

    elif jogada == 9:
        if tabuleiro[2][2] == 0:
            tabuleiro[2][2] = jogador
            return 1
        else:
            return 0
#--------------------------------//-------------------

#----------verifica quem ganhou ----------------------------
def verifica_termino():
	if((tabuleiro[0][0]==tabuleiro[0][1] and tabuleiro[0][0]==tabuleiro[0][2]) and (tabuleiro[0][0]==1)) or ((tabuleiro[1][0]==tabuleiro[1][1] and tabuleiro[1][0]==tabuleiro[1][2])and
	  (tabuleiro[1][0]==1)) or ((tabuleiro[2][0]==tabuleiro[2][1] and tabuleiro[2][0]==tabuleiro[2][2])and
	  (tabuleiro[2][0]==1)) or ((tabuleiro[0][0]==tabuleiro[1][0] and tabuleiro[0][0]==tabuleiro[2][0])and
	  (tabuleiro[0][0]==1)) or ((tabuleiro[0][1]==tabuleiro[1][1] and tabuleiro[0][1]==tabuleiro[2][1])and
	  (tabuleiro[0][1]==1)) or ((tabuleiro[0][2]==tabuleiro[1][2] and tabuleiro[0][2]==tabuleiro[2][2])and
	  (tabuleiro[0][2]==1)) or ((tabuleiro[0][0]==tabuleiro[1][1] and tabuleiro[0][0]==tabuleiro[2][2])and
	  (tabuleiro[0][0]==1)) or ((tabuleiro[2][0]==tabuleiro[1][1] and tabuleiro[0][2]==tabuleiro[2][0])and
	  (tabuleiro[2][0]==1)):
	   return 1
	
	elif((tabuleiro[0][0]==tabuleiro[0][1] and tabuleiro[0][0]==tabuleiro[0][2])and
	  (tabuleiro[0][0]==2)) or ((tabuleiro[1][0]==tabuleiro[1][1] and tabuleiro[1][0]==tabuleiro[1][2])and
	  (tabuleiro[1][0]==2)) or ((tabuleiro[2][0]==tabuleiro[2][1] and tabuleiro[2][0]==tabuleiro[2][2])and
	  (tabuleiro[2][0]==2)) or ((tabuleiro[0][0]==tabuleiro[1][0] and tabuleiro[0][0]==tabuleiro[2][0])and
	  (tabuleiro[0][0]==2)) or ((tabuleiro[0][1]==tabuleiro[1][1] and tabuleiro[0][1]==tabuleiro[2][1])and
	  (tabuleiro[0][1]==2)) or ((tabuleiro[0][2]==tabuleiro[1][2] and tabuleiro[0][2]==tabuleiro[2][2])and
	  (tabuleiro[0][2]==2)) or ((tabuleiro[0][0]==tabuleiro[1][1] and tabuleiro[0][0]==tabuleiro[2][2])and
	  (tabuleiro[0][0]==2)) or ((tabuleiro[2][0]==tabuleiro[1][1] and tabuleiro[0][2]==tabuleiro[2][0])and
	  (tabuleiro[2][0]==2)):
	  return 2
	  
	elif tabuleiro_completo():
	    return 3
	  
	else:
	    return 0
#---------------------------------//---------------------        

#----JOGADA ALEATORIA----------------------
def jogadaAleatoria():
    lin=0
    col=0
    for l in range(0,3):
        for c in range(0,3):
            if tabuleiro[l][c]==0:
                lin = l
                col = c

    tabuleiro[lin][col]=1
#-----------//------------------------------

#-----------ganharJOGO----------------------------
def ganharJogo():
    if tabuleiro[0][0]==1 and tabuleiro[0][2]==1 and tabuleiro[0][1]==0:
        tabuleiro[0][1]=1
        return 1
    elif tabuleiro[1][1]==1 and tabuleiro[2][1]==1 and tabuleiro[0][1]==0:
        tabuleiro[0][1]=1
        return 1
    elif tabuleiro[1][0]==1 and tabuleiro[1][1]==1 and tabuleiro[1][2]==0:
        tabuleiro[1][2]=1
        return 1	
    elif tabuleiro[1][1]==1 and tabuleiro[0][1]==1 and tabuleiro[2][1]==0:
        tabuleiro[2][1]=1
        return 1
    elif tabuleiro[2][1]==1 and tabuleiro[0][1]==1 and tabuleiro[1][1]==0:
        tabuleiro[1][1]=1
        return 1				
    elif tabuleiro[0][0]==1 and tabuleiro[2][0]==1 and tabuleiro[1][0]==0:
        tabuleiro[1][0]=1
        return 1
    elif tabuleiro[1][2]==1 and tabuleiro[1][1]==1 and tabuleiro[1][0]==0:
        tabuleiro[1][0]=1
        return 1
    elif tabuleiro[1][0]==1 and tabuleiro[1][2]==1 and tabuleiro[1][1]==0:
        tabuleiro[1][1]=1
        return 1	
    elif tabuleiro[0][2]==1 and tabuleiro[2][2]==1 and tabuleiro[1][2]==0:
        tabuleiro[1][2]=1
        return 1
    elif tabuleiro[2][0]==1 and tabuleiro[2][2]==1 and tabuleiro[2][1]==0:
        tabuleiro[2][1]=1
        return 1
    elif (tabuleiro[0][0]==1 and tabuleiro[2][2]==1 and tabuleiro[1][1]==0) or (tabuleiro[0][2]==1 and tabuleiro[2][0]==1 and tabuleiro[1][1]==0):
        tabuleiro[1][1]=1
        return 1
    elif (tabuleiro[0][0]==1 and tabuleiro[0][1]==1 and tabuleiro[0][2]==0) or (tabuleiro[1][2]==1 and tabuleiro[2][2]==1 and tabuleiro[0][2]==0) or (tabuleiro[2][0]==1 and tabuleiro[1][1]==1 and tabuleiro[0][2]==0):
        tabuleiro[0][2]=1
        return 1
    elif (tabuleiro[0][0]==1 and tabuleiro[1][0]==1 and tabuleiro[2][0]==0) or (tabuleiro[2][1]==1 and tabuleiro[2][2]==1 and tabuleiro[2][0]==0) or (tabuleiro[0][2]==1 and tabuleiro[1][1]==1 and tabuleiro[2][0]==0):
        tabuleiro[2][0]=1
        return 1
    elif (tabuleiro[0][1]==1 and tabuleiro[0][2]==1 and tabuleiro[0][0]==0) or (tabuleiro[1][0]==1 and tabuleiro[2][0]==1 and tabuleiro[0][0]==0) or (tabuleiro[1][1]==1 and tabuleiro[2][2]==1 and tabuleiro[0][0]==0):
        tabuleiro[0][0]=1
        return 1
    elif (tabuleiro[0][2]==1 and tabuleiro[1][2]==1 and tabuleiro[2][2]==0) or (tabuleiro[2][0]==1 and tabuleiro[2][1]==1 and tabuleiro[2][2]==0) or (tabuleiro[0][0]==1 and tabuleiro[1][1]==1 and tabuleiro[2][2]==0):
        tabuleiro[2][2]=1
        return 1
    else:
        return 0
#-----------------//------------------------

#-----------Fechar Jogador-----------------
def fecharJogador():
    if tabuleiro[0][0]==2 and tabuleiro[0][2]==2 and tabuleiro[0][1]==0:
        tabuleiro[0][1]=1
        return 1
    elif tabuleiro[1][1]==2 and tabuleiro[2][1]==2 and tabuleiro[0][1]==0:
        tabuleiro[0][1]=1
        return 1
    elif tabuleiro[1][0]==2 and tabuleiro[1][1]==2 and tabuleiro[1][2]==0:
        tabuleiro[1][2]=1
        return 1	
    elif tabuleiro[1][1]==2 and tabuleiro[0][1]==2 and tabuleiro[2][1]==0:
        tabuleiro[2][1]=1
        return 1
    elif tabuleiro[2][1]==2 and tabuleiro[0][1]==2 and tabuleiro[1][1]==0:
        tabuleiro[1][1]=1
        return 1				
    elif tabuleiro[0][0]==2 and tabuleiro[2][0]==2 and tabuleiro[1][0]==0:
        tabuleiro[1][0]=1
        return 1
    elif tabuleiro[1][2]==2 and tabuleiro[1][1]==2 and tabuleiro[1][0]==0:
        tabuleiro[1][0]=1
        return 1
    elif tabuleiro[1][0]==2 and tabuleiro[1][2]==2 and tabuleiro[1][1]==0:
        tabuleiro[1][1]=1
        return 1	
    elif tabuleiro[0][2]==2 and tabuleiro[2][2]==2 and tabuleiro[1][2]==0:
        tabuleiro[1][2]=1
        return 1
    elif tabuleiro[2][0]==2 and tabuleiro[2][2]==2 and tabuleiro[2][1]==0:
        tabuleiro[2][1]=1
        return 1
    elif (tabuleiro[0][0]==2 and tabuleiro[2][2]==2 and tabuleiro[1][1]==0) or (tabuleiro[0][2]==2 and tabuleiro[2][0]==2 and tabuleiro[1][1]==0):
        tabuleiro[1][1]=1
        return 1
    elif (tabuleiro[0][0]==2 and tabuleiro[0][1]==2 and tabuleiro[0][2]==0) or (tabuleiro[1][2]==2 and tabuleiro[2][2]==2 and tabuleiro[0][2]==0) or (tabuleiro[2][0]==2 and tabuleiro[1][1]==2 and tabuleiro[0][2]==0):
        tabuleiro[0][2]=1
        return 1
    elif (tabuleiro[0][0]==2 and tabuleiro[1][0]==2 and tabuleiro[2][0]==0) or (tabuleiro[2][1]==2 and tabuleiro[2][2]==2 and tabuleiro[2][0]==0) or (tabuleiro[0][2]==2 and tabuleiro[1][1]==2 and tabuleiro[2][0]==0):
        tabuleiro[2][0]=1
        return 1
    elif (tabuleiro[0][1]==2 and tabuleiro[0][2]==2 and tabuleiro[0][0]==0) or (tabuleiro[1][0]==2 and tabuleiro[2][0]==2 and tabuleiro[0][0]==0) or (tabuleiro[1][1]==2 and tabuleiro[2][2]==2 and tabuleiro[0][0]==0):
        tabuleiro[0][0]=1
        return 1
    elif (tabuleiro[0][2]==2 and tabuleiro[1][2]==2 and tabuleiro[2][2]==0) or (tabuleiro[2][0]==2 and tabuleiro[2][1]==2 and tabuleiro[2][2]==0) or (tabuleiro[0][0]==2 and tabuleiro[1][1]==2 and tabuleiro[2][2]==0):
        tabuleiro[2][2]=1
        return 1
    else:
        return 0
#-----------------//------------------------

#--------Primeria Jogada-----------
def comecarJogada():
    aux = random.randint(1,4)

    if aux == 1:
        tabuleiro[0][0]=1
    elif aux == 2:
        tabuleiro[0][2]=1
    elif aux == 3:
        tabuleiro[2][0]=1
    elif aux == 4:
        tabuleiro[2][2]=1
#----------------//---------------------------

#--------Segunda Jogada-------------------------------
def segundaJogada():
    if tabuleiro[0][0]==2 or tabuleiro[0][2]==2 or tabuleiro[2][0]==2 or tabuleiro[2][2]==2:
        tabuleiro[1][1]=1
    elif tabuleiro[0][1]==2 or tabuleiro[1][0]==2:
        tabuleiro[0][0]=1
    elif tabuleiro[1][2]==2 or tabuleiro[2][1]==2:
        tabuleiro[2][2]=1
    elif tabuleiro[1][1]==2:
        comecarJogada()
#----------------------//------------------------
        
#-----------Terceira Jogada -----------------------
def terceiraJogada():
    #Caso jogador jogue no meio -------
    if tabuleiro[1][1]==2: 
        if tabuleiro[0][0]==1:
            tabuleiro[2][2]=1
        elif tabuleiro[0][2]==1:
            tabuleiro[2][0]=1
        elif tabuleiro[2][0]==1:
            tabuleiro[0][2]=1
        elif tabuleiro[2][2]==1:
            tabuleiro[0][0]=1
    else:
    #Caso jogador jogue algum canto ou nos lados do centro ------
             
        if tabuleiro[0][0]==1:
    #Verificando se A PRIMEIRA HORIZONTAL E VERTICAL superior ESTA LIVRE!!!!
            if tabuleiro[0][1]==0 and tabuleiro[0][2]==0:
                tabuleiro[0][2]=1
            elif tabuleiro[1][0]==0 and tabuleiro[2][0]==0:
                tabuleiro[2][0]=1
				
	    #----------//-------------	
        elif tabuleiro[0][2]==1:
	#VERIFICANDO SE A TERCEIRA HORIZONTAL E VERTICAL superior ESTA LIVRE!!!!!!
            if tabuleiro[0][1]==0 and tabuleiro[0][0]==0:
                tabuleiro[0][0]=1
            elif tabuleiro[1][2]==0 and tabuleiro[2][2]==0:
                tabuleiro[2][2]=1
    		#-------//------------	
        elif tabuleiro[2][0]==1:
	#Verificando se A PRIMEIRA HORIZONTAL E VERTICAL inferior ESTA LIVRE!!!!
            if tabuleiro[1][0]==0 and tabuleiro[0][0]==0:
                tabuleiro[0][0]=1
            elif tabuleiro[2][1]==0 and tabuleiro[2][2]==0:
                tabuleiro[2][2]=1
        elif tabuleiro[2][2]==1:
	#VERIFICANDO SE A TERCEIRA HORIZONTAL E VERTICAL inferior ESTA LIVRE!!!!!!
            if tabuleiro[1][2]==0 and tabuleiro[0][2]==0:
                tabuleiro[0][2]=1
            elif tabuleiro[2][1]==0 and tabuleiro[2][0]==0:
                tabuleiro[2][0]=1
#---------------------//----------------------------------			
			
#-------Quarta Jogada----------------------------------
def quartaJogada():
    #------TENTAR FECHAR JOGADOR---------
    if fecharJogador()==0:
        #-----TENTAR JOGADA--------------
        if tabuleiro[1][1]==1:
        #--------Caso jogador tenha jogado em algum canto e IA JOGA NO MEIO-------
	#--------JOGADA DE  DEFESA----
            if tabuleiro[0][0]==2 and tabuleiro[0][1]==2:
                tabuleiro[0][2]=1
            elif tabuleiro[0][1]==2 and tabuleiro[0][2]==2:
                tabuleiro[0][0]=1
            elif tabuleiro[2][0]==2 and tabuleiro[2][1]==2:
                tabuleiro[2][2]=1
            elif tabuleiro[2][1]==2 and tabuleiro[2][2]==2:
                tabuleiro[2][0]=1
            elif tabuleiro[0][0]==2 and tabuleiro[1][0]==2:
                tabuleiro[2][0]=1
            elif tabuleiro[2][0]==2 and tabuleiro[1][0]==2:
                tabuleiro[0][0]=1
            elif tabuleiro[2][2]==2 and tabuleiro[1][2]==2:
                tabuleiro[0][2]=1
            elif tabuleiro[0][2]==2 and tabuleiro[1][2]==2:
                tabuleiro[2][2]=1
            elif tabuleiro[0][0]==2 and tabuleiro[0][2]==2:
                tabuleiro[0][1]=1
            elif tabuleiro[0][0]==2 and tabuleiro[2][0]==2:
                tabuleiro[1][0]=1
            elif tabuleiro[2][0]==2 and tabuleiro[2][2]==2:
                tabuleiro[2][1]=1
            elif tabuleiro[2][2]==2 and tabuleiro[0][2]==2:
                tabuleiro[1][2]=1
            elif tabuleiro[0][0]==2 and tabuleiro[1][2]==2:
                #----AQUI PODE  TER 3 OPC DE JOGADA---
		#----A JOGADA ESCOLHIDA SERA ALETORIA--
                jogada_temp=random.randint(1,3)
                
                if jogada_temp==1:
                    tabuleiro[0][2]=1
                elif jogada_temp==2:
                    tabuleiro[2][1]=1
                elif jogada_temp==3:
                    tabuleiro[2][2]=1
                #------//-------------
            elif tabuleiro[0][2]==2 and tabuleiro[1][0]==2:
                jogada_temp=random.randint(1,3)

                if jogada_temp==1:
                    tabuleiro[0][0]=1
                elif jogada_temp==2:
                    tabuleiro[0][1]=1
                elif jogada_temp==3:
                    tabuleiro[2][0]=1
                #------//-------------
            elif tabuleiro[2][0]==2 and tabuleiro[1][2]==2:
                jogada_temp=random.randint(1,3)

                if jogada_temp==1:
                    tabuleiro[0][1]=1
                elif jogada_temp==2:
                    tabuleiro[2][1]=1
                elif jogada_temp==3:
                    tabuleiro[0][2]=1
                #------//-------------
            elif tabuleiro[1][0]==2 and tabuleiro[2][2]==2:
                jogada_temp=random.randint(1,3)

                if jogada_temp==1:
                    tabuleiro[0][0]=1
                elif jogada_temp==2:
                    tabuleiro[0][1]=1
                elif jogada_temp==3:
                    tabuleiro[2][1]=1
                #------//-------------
            elif (tabuleiro[0][0]==2 and tabuleiro[2][2]==2) or (tabuleiro[2][0]==2 and tabuleiro[0][2]==2):
                #---------Defesa em diagonal----------principal------
                jogada_temp=random.randint(1,3)

                if jogada_temp==1:
                    tabuleiro[0][1]=1
                elif jogada_temp==2:
                    tabuleiro[1][0]=1
                elif jogada_temp==3:
                    tabuleiro[1][2]=1
                #------//-------------
        elif tabuleiro[1][1]==2:
            #----Caso o jogador tenha jogado no meio A IA vai jogar em algum canto----
            #----Jodas de defesa-----------   
            if tabuleiro[0][1]==2:
                tabuleiro[2][1]=1
            elif (tabuleiro[0][2]==2) or (tabuleiro[0][0]==2 and tabuleiro[2][2]==1):
                tabuleiro[2][0]=1
            elif tabuleiro[1][0]==2:
                tabuleiro[1][2]=1
            elif tabuleiro[1][2]==2 and tabuleiro[0][0]==1:
                tabuleiro[1][0]=1
            elif (tabuleiro[2][0]==2 and tabuleiro[0][0]==1) or (tabuleiro[2][2]==2 and tabuleiro[0][0]==1) or (tabuleiro[2][0]==2 and tabuleiro[2][2]==1):
                tabuleiro[0][2]=1
            elif tabuleiro[2][1]==2:
                tabuleiro[0][1]=1
            elif (tabuleiro[0][0]==2 and tabuleiro[0][1]==1) or (tabuleiro[2][0]==2 and tabuleiro[0][2]==1) or (tabuleiro[0][0]==2 and tabuleiro[2][0]==1):
                tabuleiro[2][2]=1
            elif (tabuleiro[2][2]==2) or (tabuleiro[0][2]==2 and tabuleiro[2][0]==1):
                tabuleiro[0][0]=1
        #----caso jogador tenha  comecado a jogar em algum dos lados do centro--------	
        else:
            if tabuleiro[0][1]==2 and tabuleiro[0][2]==2 and tabuleiro[0][0]==1:
                jogada_temp=random.randint(1,2)

                if jogada_temp==1:
                    tabuleiro[1][0]=1
                elif jogada_temp==2:
                    tabuleiro[2][0]=1
                #------//-------------  
            elif tabuleiro[0][1]==2 and tabuleiro[1][0]==2 and tabuleiro[0][0]==1:
                jogada_temp=random.randint(1,3)
                
                if jogada_temp==1 or jogada_temp==2:
                    tabuleiro[1][1]=1
                elif jogada_temp==2:
                    tabuleiro[2][0]=1
                #------//-------------
            elif tabuleiro[0][1]==2 and tabuleiro[1][2]==2 and tabuleiro[0][0]==1:
                jogada_temp=random.randint(1,4)

                if jogada_temp==1 or jogada_temp==4:
                    tabuleiro[2][1]=1
                elif jogada_temp==2:
                    tabuleiro[1][0]=1
                elif jogada_temp==3:
                    tabuleiro[1][1]=1
                #------//-------------   
            elif (tabuleiro[0][1]==2 and tabuleiro[2][1]==2 and tabuleiro[1][1]==0) or (tabuleiro[1][0]==2 and tabuleiro[1][2]==2 and tabuleiro[1][1]==0) or (tabuleiro[0][1]==2 and tabuleiro[2][0]==2 and tabuleiro[0][0]==1):
                tabuleiro[1][1]=1
            elif tabuleiro[0][1]==2 and tabuleiro[2][2]==2 and tabuleiro[0][0]==1:
                jogada_temp=random.randint(1,3)

                if jogada_temp==1:
                    tabuleiro[1][1]=1
                elif jogada_temp==2:
                    tabuleiro[2][0]=1
                elif jogada_temp==3:
                    tabuleiro[2][1]=1
                #------//-------------
            elif tabuleiro[0][0]==2 and tabuleiro[0][1]==2 and tabuleiro[0][2]==1:
                jogada_temp=random.randint(1,7)

                if jogada_temp <=3:
                    tabuleiro[1][2]=1
                elif jogada_temp>=4 and jogada_temp<=6:
                    tabuleiro[2][2]=1
                elif jogada_temp==7:
                    tabuleiro[2][1]=1
                #------//-------------
            elif tabuleiro[0][1]==2 and tabuleiro[1][0]==2 and tabuleiro[0][2]==1:
                jogada_temp=random.randint(1,10)

                if jogada_temp >=1 and jogada_temp<=5:
                    tabuleiro[2][2]=1
                elif jogada_temp==6 or jogada_temp==7:
                    tabuleiro[1][1]=1
                elif jogada_temp==8 or jogada_temp==9:
                    tabuleiro[1][2]=1
                elif jogada_temp==10:
                    tabuleiro[1][2]=1
                #------//-------------
            elif tabuleiro[0][1]==2 and tabuleiro[1][2]==2 and tabuleiro[0][2]==1:
                jogada_temp=random.randint(1,3)
            
                if jogada_temp<=2:
                    tabuleiro[1][1]=1
                elif jogada_temp==3:
                    tabuleiro[1][0]=1
                #------//-------------
            elif tabuleiro[0][1]==2 and tabuleiro[2][0]==2 and tabuleiro[0][2]==1:
                jogada_temp=random.randint(1,3)

                if jogada_temp == 1:
                    tabuleiro[1][1]=1
                elif jogada_temp == 2:
                    tabuleiro[2][1]=1
                elif jogada_temp == 3:
                    tabuleiro[2][2]=1
                #------//-------------    
            elif tabuleiro[0][1]==2 and tabuleiro[2][2]==2 and tabuleiro[0][2]==1:
                jogada_temp=random.randint(1,5)
            
                if jogada_temp<=3:
                    tabuleiro[1][1]=1
                elif jogada_temp>=4:
                    tabuleiro[2][1]=1
                #------//-------------
            elif tabuleiro[0][1]==2 and tabuleiro[1][0]==2 and tabuleiro[2][0]==1:
                tabuleiro[2][2]=1
            elif tabuleiro[0][1]==2 and tabuleiro[1][2]==2 and tabuleiro[2][0]==1:
                jogada_temp=random.randint(1,2)
            
                if jogada_temp==1:
                    tabuleiro[0][0]=1
                elif jogada_temp==2:
                    tabuleiro[2][2]=1
                #------//-------------
            elif tabuleiro[0][1]==2 and tabuleiro[2][2]==2 and tabuleiro[2][0]==1:
                tabuleiro[0][0]=1
            elif tabuleiro[0][1]==2 and tabuleiro[1][0]==2 and tabuleiro[0][0]==1:
                tabuleiro[1][1]=1
            elif tabuleiro[1][0]==2 and tabuleiro[2][0]==2 and tabuleiro[0][0]==1:
                tabuleiro[0][2]=1
            elif tabuleiro[1][0]==2 and tabuleiro[2][1]==2 and tabuleiro[0][0]==1:
                tabuleiro[1][1]=1
            elif tabuleiro[1][0]==2 and tabuleiro[2][2]==2 and tabuleiro[0][0]==1:
                tabuleiro[1][1]=1
            elif (tabuleiro[0][0]==2 and tabuleiro[1][2]==2 and tabuleiro[2][2]==1) or (tabuleiro[0][1]==2 and tabuleiro[1][2]==2 and tabuleiro[2][2]==1):
                tabuleiro[1][1]=1
            elif tabuleiro[1][2]==2 and tabuleiro[2][0]==2 and tabuleiro[2][2]==1:
                tabuleiro[1][1]=1
            elif tabuleiro[1][2]==2 and tabuleiro[2][1]==2 and tabuleiro[2][2]==1:
                tabuleiro[0][0]=1
            elif tabuleiro[1][2]==2 and tabuleiro[2][2]==2 and tabuleiro[2][2]==1:
                tabuleiro[0][0]=1
            elif tabuleiro[2][1]==2 and tabuleiro[0][0]==2 and tabuleiro[2][2]==1:
                tabuleiro[1][1]=1
            elif tabuleiro[2][1]==2 and tabuleiro[0][2]==2 and tabuleiro[2][2]==1:
                tabuleiro[1][1]=1
            elif tabuleiro[2][1]==2 and tabuleiro[1][0]==2 and tabuleiro[2][2]==1:
                tabuleiro[1][1]=1
            elif tabuleiro[2][1]==2 and tabuleiro[1][2]==2 and tabuleiro[2][2]==1:
                tabuleiro[1][1]=1
            elif tabuleiro[2][1]==2 and tabuleiro[2][0]==2 and tabuleiro[2][2]==1:
                jogada_temp=random.randint(1,7)
                
                if jogada_temp >= 1 and jogada_temp <=3:
                    tabuleiro[1][2]=1
                elif jogada_temp >= 4 and jogada_temp <=6:
                    tabuleiro[0][2]=1
                elif jogada_temp == 7:
                    tabuleiro[0][1]=1
                #------//-------------
            elif tabuleiro[0][2]==2 and tabuleiro[1][2]==2 and tabuleiro[2][2]==1:
                jogada_temp=random.randint(1,4)
            
                if jogada_temp<=2:
                    tabuleiro[2][1]=1
                elif jogada_temp>=3:
                    tabuleiro[1][1]=1
                #------//-------------
            elif tabuleiro[1][1]==2 and tabuleiro[1][2]==2 and tabuleiro[2][2]==1:
                tabuleiro[1][0]=1
            else:
                print("Não tenho jogadas ----JOGADA DE NÚMERO 4!!!\n\n")
                jogadaAleatoria()
                print("Efetuei jogada aleatoria !!!")
#----------------------------//--------------------------------------------------------

#-----------Quinta Jogada -----------------
def quintaJogada():
    if ganharJogo()==0:
        if fecharJogador()==0:
            if (tabuleiro[0][0]==1 and tabuleiro[2][0]==1 and tabuleiro[0][2]==2) or (tabuleiro[0][0]==1 and tabuleiro[2][0]==1 and tabuleiro[0][1]==2):
                tabuleiro[2][2]=1
            elif (tabuleiro[0][0]==1 and tabuleiro[2][0]==1 and tabuleiro[2][2]==2) or (tabuleiro[0][0]==1 and tabuleiro[2][0]==1 and tabuleiro[2][1]==2):
                tabuleiro[0][2]=1
            elif (tabuleiro[0][0]==1 and tabuleiro[0][2]==1 and tabuleiro[2][2]==2) or (tabuleiro[0][0]==1 and tabuleiro[0][2]==1 and tabuleiro[1][2]==2):
                tabuleiro[2][0]=1
            elif (tabuleiro[0][0]==1 and tabuleiro[0][2]==1 and tabuleiro[2][0]==2) or (tabuleiro[0][0]==1 and tabuleiro[0][2]==1 and tabuleiro[1][0]==2):
                tabuleiro[2][2]=1
            elif (tabuleiro[0][2]==1 and tabuleiro[2][2]==1 and tabuleiro[0][0]==2) or (tabuleiro[0][2]==1 and tabuleiro[2][2]==1 and tabuleiro[0][1]==2):
                tabuleiro[2][0]=1
            elif (tabuleiro[0][2]==1 and tabuleiro[2][2]==1 and tabuleiro[2][0]==2) or (tabuleiro[0][2]==1 and tabuleiro[2][2]==1 and tabuleiro[2][1]==2):
                tabuleiro[0][0]=1
            elif (tabuleiro[2][0]==1 and tabuleiro[2][2]==1 and tabuleiro[0][2]==2) or (tabuleiro[2][0]==1 and tabuleiro[2][2]==1 and tabuleiro[1][2]==2):
                tabuleiro[0][0]=1
            elif (tabuleiro[2][0]==1 and tabuleiro[2][2]==1 and tabuleiro[0][0]==2) or (tabuleiro[2][0]==1 and tabuleiro[2][2]==1 and tabuleiro[1][0]==2):
                tabuleiro[0][2]=1
            else:
                print("Não tenho mais jogada ----- JOGADA DE NÚMERO 05 !!!\n\n\n")
                jogadaAleatoria()
                print("Efetuei jogada aleatória!!!!\n\n")
#------------------------------------//-----------------------------------

#-----CHAMANDO IA -------------------------------------------------
def chamaIA():
    if cont2==1:
        comecarJogada()

    elif cont2==2:
        segundaJogada()
        
    elif cont2==3:
        terceiraJogada()

    elif cont2==4:
        quartaJogada()

    elif cont2==5:
        quintaJogada()

    elif cont2>=6:
        if ganharJogo()==0:
            if fecharJogador()==0:
                print(f'Não tenho mais jogada ----- JOGADA DE NÚMERO {cont2} !!!\n\n\n')
                jogadaAleatoria()
                print("Efetuei jogada aleatória!!!!\n\n")
#---------------//-----------------------------

                
def main():
    jogada=0
    termino=0
        #------iniciando matriz------
    for l in range (0,3):
        for c in range (0,3):
            tabuleiro[l][c]=0
        #---------//------------------

        #-------selecionar aleatoriamento quem joga primeiro------------
    jogo_atual=random.randint(1,2)
    cont2=0
        
    while True :
        
        imprime_tabuleiro()

        
        if jogo_atual == 1:
            cont2 = cont2+1
            if cont2==1:
                comecarJogada()

            elif cont2==2:
                segundaJogada()
        
            elif cont2==3:
                terceiraJogada()

            elif cont2==4:
                quartaJogada()

            elif cont2==5:
                quintaJogada()

            elif cont2>=6:
                if ganharJogo()==0:
                    if fecharJogador()==0:
                        print(f'Não tenho mais jogada ----- JOGADA DE NÚMERO {cont2} !!!\n\n\n')
                        jogadaAleatoria()
                        print("Efetuei jogada aleatória!!!!\n\n")
            print()
                
        elif jogo_atual == 2:
            cont2 = cont2 + 1
            print(f'\nJogador {jogo_atual}')
            jogada=int(input("Informe sua jogada"))

            while verifica_jogada(jogada, jogo_atual) != 1 :
                print("Jogada inválida tente novamente!!")
                jogada=int(input("Informe sua jogada"))

        if jogo_atual == 1:
            jogo_atual = 2
        else:
            jogo_atual = 1
            
        termino=verifica_termino()
        if termino != 0:
            break
    imprime_tabuleiro()
    if termino != 3:
        print(f'O jogador {termino} ganhou')
    else:
        print("Jogo terminou, deu velha")
        
              

main()

