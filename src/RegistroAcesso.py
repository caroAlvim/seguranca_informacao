import os

import stat

def registrar_acesso(email, date_and_hour):

        # Criar o arquivo Acesso
        arquivo = open("acesso.txt", "a")

        os.chmod("acesso.txt", stat.S_IRWXU)

        # Escreve no arquivo, email e data e hora
        arquivo.write(email + "\n")
        arquivo.write(str(date_and_hour) + "\n")

        # Fecha o arquivo
        arquivo.close()

        # Modifica o arquivo apenas para leitura
        # os.chmod("acesso.txt", stat.S_IRUSR)

        # Mensagem confirmacao fechamento e alteracao para modo leitura

        print("Arquivo acesso fechado e modificado para modo leitura, com sucesso !")

