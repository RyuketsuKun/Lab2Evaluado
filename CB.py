import binascii
  
def Llave_Random(p):
    import random
    llave = ""
    p = int(p)
      
    for i in range(p):
          
        temp = str(random.randint(0,1))
        llave = llave + temp
          
    return(llave)
   

def bit(a,b,n):
      
    temp = "" 
      
    for i in range(n): 
          
        if (a[i] == b[i]):
            temp += "0"
              
        else: 
            temp += "1"
              
    return temp 
  
def BaD(binary): 
    string = int(binary, 2) 
    return string
  
def Cifrado(msj):
    newmsj = msj


    msjbit = [ord(x) for x in newmsj]
    

    msjbin = [format(y,'08b') for y in msjbit]
    msjbin = "".join(msjbin)
    
    n = int(len(msjbin)//2)
    L1 = msjbin[0:n]
    R1 = msjbin[n::]
    m = len(R1)
    

    clave1= Llave_Random(m)

    clave2= Llave_Random(m)
    

    f1 = bit(R1,clave1,n)
    R2 = bit(f1,L1,n)
    L2 = R1

    f2 = bit(R2,clave2,n)
    R3 = bit(f2,L2,n)
    L3 = R2
    

    datosB = L3 + R3
    msjfinal =' '
    
    for i in range(0, len(datosB), 7): 
            

        temporal = datosB[i:i + 7] 
            

        datosD = BaD(temporal) 
            

        msjfinal = msjfinal + chr(datosD) 
        
    return msjfinal,L3,R3, clave2,clave1,n



def Decifrado(msj, L, R ,clave2 , clave1,n):
    L4 = L
    R4 = R
    
    f3 = bit(L4,clave2,n)
    L5 = bit(R4,f3,n)
    R5 = L4
    
    f4 = bit(L5,clave1,n)
    L6 = bit(R5,f4,n)
    R6 = L5
    PT1 = L6+R6
    PT1 = int(PT1, 2)
    
    RPT = binascii.unhexlify( '%x'% PT1)
    RPT = RPT.decode("utf8")
    return RPT






