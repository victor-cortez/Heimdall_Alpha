import socket
from collections import OrderedDict
from random import randint


s = socket.socket()         # Create a socket object
host = socket.gethostname()
port = 600
quant_populacao = 8

def returnvalues(x):
    valores = [i[1] for i in list(x.items())]
    return valores

def nothousand(x):
    if x >= 999:
        return 999
    else:
        return x
def nothreethousand(x):
    if x >= 2000:
        return 2000
    else:
        return x
def no500(x):
    if x >= 500:
        return 500
    else:
        return x

def maior(x,minimum):
    if x >= minimum:
        return x
    else:
        return minimum

num_rounds = int(input("Digite a quantidade de rounds: "))
populacao = OrderedDict()
filhos = []
for i in range(0,quant_populacao):
    minimal = randint(0,200)
    filhos.append([str(randint(1,999)) + "," + str(randint(30,2000)) + "," + str(minimal) + "," + str(randint(minimal,500))])
print ("Populacao inicial:")
print (filhos)
print ("-----")
main_count = 0

for i in range(0,num_rounds):
    if main_count != 0:
        #Order the population, filter the two more fit, and then reproduce them introducing some random mutations
        populacao = OrderedDict(reversed(sorted(populacao.items(), key=lambda x: x[1])))
        pai = populacao.popitem(last = False)
        mae = populacao.popitem(last = False)
        configs_pai = [int(i) for i in pai[0].split(",")]
        configs_mae = [int(i) for i in mae[0].split(",")]
        configs_filho = [int((configs_pai [0] + configs_mae[0]) / 2),int((configs_pai [1] + configs_mae[1]) / 2),int((configs_pai [2] + configs_mae[2]) / 2),int((configs_pai [3] + configs_mae[3]) / 2)]
        filhos = []
        for i in range(0,quant_populacao - 2):
            menor = no500(configs_filho[2] + randint(-40,40))
            new_filho = [
            nothousand(configs_filho[0] + randint(-60,60)),
            nothreethousand(configs_filho[1] + randint(-120,120)),
            menor,
            no500(maior(configs_filho[3] + randint(-40,40),menor))
            ]
            filhos.append(new_filho)
        filhos.append(configs_pai)
        filhos.append(configs_mae)
        print ("------------")
        print("Nova populacao:")
        print (filhos)
        print ("------------")

    populacao = OrderedDict()
    #start the multiprocessing
    conta = 0
    s = socket.socket()
    s.bind((host, port))        # Bind to the port
    s.listen(20)
    ok = True
    while len(populacao) < len(filhos):
        if ok is True:
            print ("----------")
            print (len(populacao))
            print(populacao)
            print (len(filhos))
            print(conta)
            print ("----------")
        try:
            if ok is True:
                print ("Wainting connections")
            c, addr = s.accept()     # Establish connection with client.
            status = c.recv(1024).decode('utf-8')
            if ok is True:
                print (str(addr[0]) + " is " + str(status.split("|")[0]))
            if status == "ready" and conta < len(filhos):
                c.send (bytes(",".join([str(i) for i in filhos[conta]]),"utf-8"))
                conta += 1
                ok = True
            elif str(status.split("|")[0]) == "done":
                print(status)
                chave = status.split("|")[1]
                valor = status.split("|")[2]
                populacao.update({chave : valor})
                print (populacao)
                ok = True
            else:
                c.send(bytes("wait","utf-8"))
                ok = False
        except Exception as e:
            print ("An error ocurred")
            print (str(e))
    print("---------------")
    valores =[int(i) for i in returnvalues(populacao)]
    media = sum(valores) / len(valores)
    arquivo = open("data.txt","a")
    arquivo.write(str(main_count) + " " + str(media) + "\n")
    print ("Round number %d finished" % main_count)
    print("A media de duracao eh de: %f" % media)
    print("---------------")
    main_count += 1
    filhos = []


print ("----------")
print ("Simulacao encerrada")
print ("A populacao restante:")
print (populacao)
print("---------")
saida = input("Digite Enter para sair")