#Tomas Astudillo (Id: 00179409) - Marco Vasquez (Id: 00179475)
#Laboratorio 2 Evaluado - Seguridad Informatica
#Se utilizo la version de Python 3.9.7
import hashlib
import Sustitucion
import CB
Comprobacion = []
Main = True
while Main:
    try:
        Seleccion = int(input("¿Que desea hacer?\n 1) Codificar el mensaje del archivo \n 2) Decodificar el mensaje del archivo \n 3) Cambiar Mensaje de entrada\n 4) Salir\n..."))
    except ValueError:
        print("Ingrese un valor numerico")
        print("-------------------------------------------")
        continue
    print("-------------------------------------------")
    if Seleccion == 1:
        if Comprobacion:
            print("Ya ha realizado la Codificacion, Proceda a Decodificar (Opcion 2)")
        else:
            MsjEntrante = open("mensajedeentrada.txt","r")
            Msj = MsjEntrante.readline().replace('\n','')
            MsjEntrante.close()
            Hash = hashlib.sha1(Msj.encode("utf-8"))
            Hash1 = Hash.hexdigest()
            Comprobacion.append(Hash1)
            Msj=Sustitucion.ATbash(Msj,1)
            Msj=Sustitucion.rot3(Msj,1)
            Msj,L,R,Clave2,Clave1,n=CB.Cifrado(Msj)
            MsjSaliente = open("mensajeseguro.txt","w")
            MsjSaliente.write(Msj)
            MsjSaliente.close()
            print("Exito!\nSu mensaje ha sido codificado satisfactoriamente")

    elif Seleccion ==2:
        if not Comprobacion:
            print("Aun no se ha realizado la Codificacion (Opcion 1)")
        else:
            MsjSaliente = open("mensajeseguro.txt","r")
            Msj = MsjSaliente.readline().replace('\n','')
            MsjSaliente.close()
            Msj=CB.Decifrado(Msj,L,R,Clave2,Clave1,n)
            Msj=Sustitucion.rot3(Msj,2)
            Msj=Sustitucion.ATbash(Msj,2)  
            Hash = hashlib.sha1(Msj.encode("utf-8"))
            Hash2 = Hash.hexdigest()
            Comprobacion.append(Hash2)
            print("Exito!\nSe ha decodificado su meensaje")
            print("Su mensaje : ", Msj,"\ntiene el codigo Hash: ", Hash2)
            if Comprobacion[1] ==Comprobacion[0]: 
                print("Su mensaje no ha sido intervenido")
            else:
                print("Su mensaje ha sido intervenido")
        print("-------------------------------------------")
    
    elif Seleccion ==3:
        if Comprobacion:
            print("Ya ha realizado la Codificacion, Proceda a Decodificar (Opcion 2)")
        else:
            MsjEntrante = open("mensajedeentrada.txt","w")
            Msj = str(input("Ingrese un nuevo mensaje: \n(Puede escribir numeros, letras mayusculas, minusculas o espacios; otros terminos como la letra ñ no se modificaran)\n..."))
            MsjEntrante.write(Msj)
            MsjEntrante.close()
            print("Su mensaje ha sido cambiado con exito!")
            print("-------------------------------------------")
    elif Seleccion ==4:
        print("Hasta Luego")
        Main = False
    else:
        print("Porfavor, escriba una opcion valida")