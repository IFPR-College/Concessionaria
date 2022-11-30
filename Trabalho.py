import os
import sqlite3
import time


bd = './Concessionaria.db'
if os.path.exists(bd) == True:
    banco = sqlite3.connect("Concessionaria.db") #cria o banco de dados
    cursor = banco.cursor()#invoca metodos de sql
else: 
    banco = sqlite3.connect("Concessionaria.db") #cria o banco de dados
    cursor = banco.cursor()#invoca metodos de sql
    cursor.execute("""CREATE TABLE IF NOT EXISTS Carros (
    idcarro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    Marca text(30) NOT NULL, 
    Ano integer(4) NOT NULL, 
    Status string(15)
    )""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS  Clientes (
    idclientes INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome text(50) NOT NULL, 
    Telefone integer(11) NOT NULL 
    )""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS  Vendedores (
    idvendedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome text(50) NOT NULL, 
    Telefone integer(11) NOT NULL
    )""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS  Vendas (
    idvenda INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    idcarrovenda INTEGER NOT NULL, 
    idcliente INTEGER NOT NULL, 
    idvendedor INTEGER NOT NULL,
    valor float NOT NULL,
    datavenda date NOT NULL,
    foreign key (idcarrovenda) references Carros(idcarro),
    foreign key (idcliente) references Clientes(idcliente),
    foreign key (idvendedor) references Vendedores(idvendedor)
    )""")
    



def telainicial():
    print("Bem vindo(a) a Concessionaria do Polido!!!")
    time.sleep(0.5) #tempo de espera
    print("Por favor responda somente com números!!!")
    time.sleep(0.5)
    resp = int(input("1 ► [Carros]     2 ► [Clientes]     3 ► [Vendedores]     4 ► [Vendas]     5 ► [Pesquisar]     6 ► [Sair] \n"))
    return resp

# inicio carros ------------------------------------------------------------------------------------------------

def adicionarXCarros():
    qtdcarro = None
    qtdcarro = int(input("Quantos carros você deseja adicionar ? \n"))
    status = "Disponivel"
    for i in range(0, qtdcarro):
        print("Carro numero: ",i+1)
        marcacarro = str(input("Digite o nome do carro: "))
        anocarro = int(input("Digite o ano do carro: "))
        cursor.execute('INSERT INTO Carros(Marca, Ano, Status) VALUES("'+marcacarro+'", "'+str(anocarro)+'", "'+status+'")') #insere dados na tabela Carros

    cursor.execute('SELECT * FROM Carros') #seleciona todos de carros
    banco.commit() #atuliza os dados no banco de dados
    print("Adicionado com sucesso!!!")

def visualizarVeiculos():
    print("ID   Marca     Ano     Status")
    cursor.execute('SELECT * FROM Carros')
    carros = cursor.fetchall() #busca todas as linhas de um resultado de consulta
    for carro in carros: # laço de repetição 
        print(carro)


def Carros(): #tela de carros
    time.sleep(0.4)
    resp=int(input("Você deseja adicionar ou visualizar os veículo ? \n1 ► [Adicionar]    2 ► [Visualizar]    3 ► [Voltar]\n"))
    if resp == 1:
        adicionarXCarros()
        return Carros()
        

    if resp == 2:
        visualizarVeiculos()
        return Carros()
        
    
    if resp == 3:
        return  Concessionaria()

    if resp > 3 or resp <= 0:
        return Clientes()
        
# fim carros ------------------------------------------------------------------------------------------------

# inicio clientes ------------------------------------------------------------------------------------------------

def adicionarClientes():
    qtdcarro = 0
    qtdcarro = int(input("Quantos clientes você deseja adicionar ? \n"))
    for i in range(0, qtdcarro): #laço de repetição pra adicionar varios clientes
        print("Cliente numero: ",i+1)
        nomecliente = str(input("Digite o nome do cliente: "))
        print("Exemplo de telefone: 45912345678 ")
        telefonecliente = int(input("Digite o telefone do cliente: "))
        cursor.execute('INSERT INTO Clientes(Nome, Telefone) VALUES("'+nomecliente+'", "'+str(telefonecliente)+'")') #insere na tabela
        cursor.execute('SELECT * FROM Clientes')
        banco.commit()  #atuliza o bd
    print("Cadastrado com sucesso!!! \n")
    

def visualizarCliente():
    print("ID   Nome        Telefone")
    cursor.execute('SELECT * FROM Clientes') #seleciona tudo
    clientes = cursor.fetchall()
    for cliente in clientes: #e mostra na tela
        print(cliente)

def Clientes(): #tela dos clientes
    time.sleep(0.4)
    resp=int(input("Você deseja adicionar ou visualizar os clientes? \n1 ► [Adicionar]    2 ► [Visualizar]    3 ► [Voltar]\n")) 
    if resp == 1:
        adicionarClientes()
        return Clientes()
    if resp == 2:
        visualizarCliente()
        return Clientes()
    if resp == 3:
        return Concessionaria()
    
    if resp > 3 or resp <= 0:
        return Clientes()
        

# fim clientes ------------------------------------------------------------------------------------------------

# inicio vendedor ------------------------------------------------------------------------------------------------

def adicionarVendedor():
    qtdvend = 0
    qtdvend = int(input("Quantos vendedores você deseja adicionar ? \n"))
    for i in range(0, qtdvend): #laço de repetição
        print("Vendedor numero: ",i+1)
        nomevendedor = str(input("Digite o nome do vendedor: "))
        print("Exemplo de telefone: 45912345678 ")
        telefonevendedor = int(input("Digite o telefone do vendedor:"))
        cursor.execute('INSERT INTO Vendedores(Nome, Telefone) VALUES("'+nomevendedor+'", "'+str(telefonevendedor)+'")') #insere na tabela
        cursor.execute('SELECT * FROM Vendedores')
        banco.commit() #atuliza o bd

def visualizarVendedor():
    print("ID   Nome        Telefone")
    cursor.execute('SELECT * FROM Vendedores')  #seleciona todos os dados
    vendedores = cursor.fetchall() #busca todas as linhas de um resultado de consulta
    for vendedor in vendedores:
        print(vendedor)

def Vendedor(): #tela do vendedor
    time.sleep(0.4)
    resp=int(input("Você deseja adicionar ou visualizar os vendedores? \n1 ► [Adicionar]    2 ► [Visualizar]    3 ► [Voltar]\n"))
    if resp == 1:
        adicionarVendedor()
        return Vendedor()
    
    if resp == 2:
        visualizarVendedor()
        return Vendedor()

    if resp == 3:
        return Concessionaria()
    
    if resp > 3 or resp <= 0:
        return Clientes()


# fim vendedor ------------------------------

# inicio vendas ------------------------------

def fazerVenda(): 
    print("Veículos a vender")
    visualizarVeiculos()
    print("Clientes Cadastrados")
    visualizarCliente()
    print("Vendedores Cadastrados")
    visualizarVendedor()
    idveiculo = int(input("Digite o ID do veículo: "))
    idcliente = int(input("Digite o ID do(a) cliente que deseja comprar o veículo: "))
    idvendedor = int(input("Digite o ID do(a) vendedor(a) que está vendendo o veículo: "))
    valorvenda = float(input("Digite o valor da venda: "))
    print("Formato da data: AAAA/MM/DD")
    datavenda = str(input("Digite a data da venda:"))
    cursor.execute('INSERT INTO Vendas(idcarrovenda, idcliente, idvendedor, Valor, datavenda ) VALUES("'+str(idveiculo)+'", "'+str(idcliente)+'", "'+str(idvendedor)+'", "'+str(valorvenda)+'", "'+str(datavenda)+'")') #insere os dados na tabela
    banco.commit() #atuliza o bd
    atualizaCarro() #muda status de disponivel para vendido
    banco.commit() #atuliza o bd
    return Vendas()


def atualizaCarro():
    cursor.execute('UPDATE Carros SET Status = "Vendido" FROM Vendas WHERE Carros.idcarro = Vendas.idcarrovenda') #muda o status de disponivel para vendido para vendido
    banco.commit() 
    print("Venda concluída com sucesso!!!") 


def consultarCarrosVendidos():
    cursor.execute("""SELECT Vendas.idvenda, Carros.Marca, Clientes.Nome, Vendedores.Nome, Vendas.valor, Vendas.datavenda, Carros.Status  FROM Vendas, Carros, Clientes, Vendedores
    WHERE Vendas.idcarrovenda = Carros.idcarro AND Vendas.idcliente = Clientes.idclientes AND Vendas.idvendedor = Vendedores.idvendedor AND Carros.Status = "Vendido" """) 
    vendas = cursor.fetchall() #busca todas as linhas de um resultado de consulta e vai printar
    print("ID  Veículo      Cliente         Vendedor        Valor       Data    Status")
    for venda in vendas: 
        print(venda)
    return consultarVendas()

def consultarCarrosNaoVendidos():
    cursor.execute('SELECT * FROM Carros WHERE Carros.Status = "Disponivel"')
    vendas = cursor.fetchall() #busca todas as linhas de um resultado de consulta e printa
    print("ID   Marca     Ano     Status")
    for venda in vendas: #laço de repetição
        print(venda)
    return consultarVendas()

def consultarTodosVeiculos():
    cursor.execute("""SELECT * from Carros""")
    vendas = cursor.fetchall() #busca todas as linhas de um resultado de consulta e printa
    print("ID   Marca     Ano     Status")
    for venda in vendas: #laço de repetição
        print(venda)
    return consultarVendas()


def consultarVendas(): #tela de consultar vendas
    time.sleep(0.4)
    print("Deseja consultar por carros vendidos ou carros não vendidos?")
    resp=int(input("1 ► [Carros Vendidos]    2 ► [Carros Não Vendidos]    3 ► [Todos]    4 ► [Voltar]\n"))
    if resp == 1:
        consultarCarrosVendidos()

    if resp == 2:
        consultarCarrosNaoVendidos()

    if resp == 3:
        consultarTodosVeiculos()

    if resp == 4:
        return Vendas()
    
    if resp > 4 or resp <= 0:
        return Clientes()


def Vendas(): #tela de vendas
    time.sleep(0.4)
    print("Você deseja realizar ou visualizar uma venda?")   
    resp=int(input("1 ► [Realizar]    2 ► [Visualizar]    3 ► [Voltar]\n"))
    if resp == 1:
        fazerVenda()
        return Vendas()
    
    if resp == 2:
        consultarVendas()
        return Vendas()

    if resp == 3:
        return Concessionaria()
    
    if resp > 3 or resp <= 0:
        return Clientes()




# fim vendas ------------------------------
# inicio consultas ------------------------------

def consultarVendedor():
    visualizarVendedor()
    resp = str(input("Digite o nome do vendedor que deseja pesquisar \n"))
    cursor.execute('SELECT Vendedores.idvendedor, Vendedores.Nome, Vendas.idvenda FROM Vendas, Vendedores WHERE Vendedores.Nome = "'+resp+'" AND Vendedores.idvendedor = Vendas.idvendedor' ) #seleciona para mostrar na tela
    vendedores = cursor.fetchall() #busca todas as linhas de um resultado de consulta
    print("ID  Nome  IDVenda")
    for vendedor in vendedores: #printa as informacoes do vendedor
        print(vendedor)
    return Consultar()
    


def consultarCliente():
    visualizarCliente()
    resp = str(input("Digite o nome do cliente que deseja pesquisar \n"))
    cursor.execute('SELECT Clientes.idclientes, Clientes.Nome, Vendas.idvenda FROM Vendas, Clientes WHERE Clientes.Nome = "'+resp+'" AND Clientes.idclientes = Vendas.idcliente' ) #seleciona para mostrar na tela
    clientes = cursor.fetchall() #busca todas as linhas de um resultado de consulta
    print("ID  Nome  IDVenda")
    for cliente in clientes: #mostra na tela as informacoes do cliente
        print(cliente)
    return Consultar()


def Consultar(): #tela de consulta
    time.sleep(0.4)
    print("Você deseja realizar uma consulta pelo nome do cliente ou do vendedor?")   
    resp=int(input("1 ► [Cliente]    2 ► [Vendedor]    3 ► [Voltar]\n"))
    if resp == 1:
        consultarCliente()
        return Consultar()
    
    if resp == 2:
        consultarVendedor()
        return Consultar()

    if resp == 3:
        return Concessionaria()

    if resp > 3 or resp <= 0:
        return Clientes()
    

    
#fim consultas ------------------------------
def Concessionaria(): #tela princial do sistema
    time.sleep(0.4)
    resp = telainicial()
    while True:
        if resp == 1: #vai pra tela de carros
            Carros()
    
        if resp == 2 : #vai pra tela de clientes
            Clientes()

        if resp == 3: #vai pra tela de vendedores
            Vendedor()

        if resp == 4: #vai pra tela de vendas
            Vendas()

        if resp == 5: #vai pra tela de consulta
            Consultar()

        if resp > 6 or resp <= 0: #retorna pra tela principal
            return Concessionaria()

        if resp == 6: #finaliza o codigo
            print("Obrigado por usar nosso sistema!")
            quit()
        
        

Concessionaria()