from CriacaoPython import criacaocadastro

from AutenticacaoPython import autenticausuario

# Menu

opcao = 0

while opcao != 3:
    print("Menu\n")
    print("1 - Cadastrar email\n")
    print("2 - Autenticar email\n")
    print("3 - Fim\n")

    escolha = input("Escolha uma opção: ")
    opcao = float (escolha)

    if opcao == 1:
        print ("Opção 1\n")
        chave = input("Digite seu e-mail: ")
        segredo = input("Digite sua senha, com pelo menos 6 caracteres: ")
        criacaocadastro(chave, segredo)

    if opcao == 2:
        print ("Opção 2\n")
        chave = input("Digite seu e-mail: ")
        segredo = input("Digite sua senha, com pelo menos 6 caracteres: ")
        autenticausuario(chave, segredo)

    if opcao == 3:
        print("Opcao 3\n")
        print("Fim")
        break