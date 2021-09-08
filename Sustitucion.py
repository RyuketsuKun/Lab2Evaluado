

def rot3(MSj,modo):
    if modo == 1 :
        abc ='abcdefghijklmnopqrstuvwxyz'
        ABC ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        Num ='1234567890'
        MensajeAux = []
        for letra in MSj:
            MensajeAux.append(letra)
        MensajeF =[]
        for letra in MensajeAux:
            if letra in abc:
                j = (abc[(abc.find(letra)+3)%26])
            elif letra in ABC:
                j = (ABC[(ABC.find(letra)+3)%26])
            elif letra in Num:
                j=  (Num[(Num.find(letra)+3)%10])
            else:
                j= letra
            MensajeF.append(j)
        MSj =''
        for letra in MensajeF:
            MSj = MSj + letra
        return MSj
    else:
        abc ='abcdefghijklmnopqrstuvwxyz'
        ABC ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        Num ='1234567890'
        MensajeAux = []
        for letra in MSj:
            MensajeAux.append(letra)
        MensajeF =[]
        for letra in MensajeAux:
            if letra in abc:
                j = (abc[(abc.find(letra)-3)%26])
            elif letra in ABC:
                j = (ABC[(ABC.find(letra)-3)%26])
            elif letra in Num:
                j=  (Num[(Num.find(letra)-3)%10])
            else:
                j= letra
            MensajeF.append(j)
        MSj =''
        for letra in MensajeF:
            MSj = MSj + letra
        return MSj




def ATbash(Msj, modo):
    if modo == 1:
        abc ='abcdefghijklmnopqrstuvwxyz'
        ABC ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        Num ='1234567890'
        MensajeAux = []
        for letra in Msj:
            MensajeAux.append(letra)
        MensajeF =[]
        for letra in MensajeAux:
            if letra in abc:
                N = 25
                j = (abc[(N- abc.find(letra))])
            elif letra in ABC:
                N = 25
                j = (ABC[(N- ABC.find(letra))])
            elif letra in Num:
                N = 9
                j=  (Num[(N- Num.find(letra))])
            else:
                j= letra
            MensajeF.append(j)
        Msj =''
        for letra in MensajeF:
            Msj = Msj + letra
        return Msj
    else:
        abc ='abcdefghijklmnopqrstuvwxyz'
        rev_abc = abc[::-1]
        ABC ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        rev_ABC = ABC[::-1]
        Num ='1234567890'
        rev_Num = Num[::-1]
        MensajeAux = []
        for letra in Msj:
            MensajeAux.append(letra)
        MensajeF =[]
        for letra in MensajeAux:
            if letra in abc:
                N = 25
                j = (abc[(N- abc.find(letra))])
            elif letra in ABC:
                N = 25
                j = (ABC[(N- ABC.find(letra))])
            elif letra in Num:
                N = 9
                j=  (Num[(N- Num.find(letra))])
            else:
                j= letra
            MensajeF.append(j)
        Msj =''
        for letra in MensajeF:
            Msj = Msj + letra
        return Msj





