from db import conectar

def cadastrar_cliente():
    nome = input('Nome: ')
    email = input('Email: ')
    telefone = input('Telefone: ')
    conn = conectar()
    cursor = conn.cursor()

    sql = "INSERT INTO CLIENTES (nome, email, telefone) VALUES(%s, %s, %s)"
    valores = (nome, email, telefone)

    cursor.execute(sql, valores)
    conn.commit()

    print("Cliente cadastrado!")

    cursor.close()
    conn.close()

def listar_clientes():
    conn = conectar()
    print(conn)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    resultado = cursor.fetchall()

    print("\n Lista de clientes: ")
    for cliente in resultado:
        print(cliente)
    
    cursor.close()
    conn.close()

def atualizar_clientes():
    id = input("ID do cliente: ")
    nome = input("Novo nome: ")
    email = input("Novo email: ")
    telefone = input("Novo telefone: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET nome=%s, email=%s, telefone=%s WHERE id=%s", (nome, email, telefone, id))
    conn.commit()
    print("Cliente atualizado!")
    conn.close()

def deletar_clientes():
    print("Informe o ID do cliente que deseja deletar")
    id = input("ID: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
    conn.commit()
    print("Cliente removido")
    conn.close()



def menu():
    while True:
        print('\n == Sistema de Cadastro de Clientes ==')
        print('1 - Cadastrar cliente')
        print('2 - Listar cliente')
        print('3 - Atualizar cliente')
        print('4 - Deletar cliente')
        print('5 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao  == '1':          
            cadastrar_cliente()

        elif opcao == '2':
            listar_clientes()

        elif opcao == '3':
            atualizar_clientes()
        
        elif opcao == '4':
            deletar_clientes()
        
        elif opcao == '5':
            print('Saindo...')
            break

        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    menu()
