import socket
import sys
import time
from ploxys import main

host = input("Digite o ip do mestre: ")
porta = 600
ok = True
while True:
    time.sleep(0.1)
    while True:
        resultado = 0
        final = 0
        resposta = 0
        inputs = []
        try:
            mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # cria o socket
        except socket.error:
            if ok is True:
                print ("Error in creating the socket") # Encerra com status de erro
            ok = False
            break
        try:
            mysock.connect((host,porta))  # conecta ao host
            ok = True
        except socket.error:
            if ok is True:
                print ("Error in connecting with the master")
            ok = False
            break
        try:
             # Obtem os dados a serem enviados
            mysock.send(bytes("ready","utf-8"))  # envia os dados para o servidor
            resposta = mysock.recv(1024).decode("utf-8")
            mysock.close()
            if resposta == "wait":
                break
            print ("Got a task: " + resposta)
            ok = True
        except:
            e = sys.exc_info()[0]
            if ok is True:
                print ("Error in communicating with master")
                print ("Error %s" % e)
            ok = False
            break
        try:
            inputs = [int(i) for i in resposta.split(",")]
            resultado = main(inputs[0],inputs[1],inputs[2],inputs[3])
            ok = True
        except:
            e = sys.exc_info()[0]
            if ok is True:
                print ("Error %s" % e)
                print("Error in calculating result, maybe data could not been found")
            ok = False
            break
        try:
            final = "done|" + resposta + "|" + str(resultado)
            print (resultado)
            mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            mysock.connect((host,porta))
            mysock.send(final.encode("utf-8"))
            ok = True
        except:
            if ok is True:
                print ("Error in answering the master")
            ok = False
            break
        mysock.close()
saida = input("Digite Enter para sair")