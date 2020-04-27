def Detecta1(Vetor1):
    valor = 160
    cont = 0
    ES = False
   

    for x in range(Vetor1.shape[0]):
        if(cont == 0):
            for y in range(Vetor1.shape[1]):
                b,g,r = Vetor1[x,y]
                
                if(b > 190):
                    if(g < valor):
                        if(r < valor):
                            cont = 1
                            ES = True
                            return ES


def Detecta2(Vetor2):
    valor = 160
    cont = 0
    EI = False

    for x in range(Vetor2.shape[0]):
        if(cont == 0):
            for y in range(Vetor2.shape[1]):
                b,g,r = Vetor2[x,y]
                
                if(b > 190):
                    if(g < valor):
                        if(r < valor):
                            cont = 1
                            EI = True
                            return EI
      


def Detecta3(Vetor3):
    valor = 160
    cont = 0
    DS = False

    for x in range(Vetor3.shape[0]):
        if(cont == 0):
            for y in range(Vetor3.shape[1]):
                b,g,r = Vetor3[x,y]
                
                if(b > 190):
                    if(g < valor):
                        if(r < valor):
                            cont = 1
                            DS = True
                            return DS


def Detecta4(Vetor4):
    valor = 160
    cont = 0
    DI = False


    for x in range(Vetor4.shape[0]):
        if(cont == 0):
            for y in range(Vetor4.shape[1]):
                b,g,r = Vetor4[x,y]
                
                if(b > 190):
                    if(g < valor):
                        if(r < valor):
                            cont = 1
                            DI = True
                            return DI
