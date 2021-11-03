import random

from Email import enviamsg

# importar o pyrebase4 no pip
import pyrebase

def autenticausuario (destino_email,password):
    firebaseConfig = {
        "apiKey": "AIzaSyAHWzCpedoqPdBDLIWprSy0Y0gCJxxxxxx",
        "authDomain": "fir-pucpr-fdxxx.firebaseapp.com",
        "projectId": "fir-pucpr-fdxxx",
        "databaseURL": "https://" + "fir-pucpr-fdxxx" + ".firebaseio.com",
        "storageBucket": "fir-pucpr-fdxxx.appspot.com",
        "messagingSenderId": "538814xxxxxx",
        "appId": "1:538814266312:web:e089134784b3a414xxxxxx",
        "measurementId": "G-QX7Hxxxxxx"
    }

    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()


    # status = auth.create_user_with_email_and_password(user,password)
    status = auth.sign_in_with_email_and_password(destino_email,password)
    idToken = status["idToken"]

    print("Resultado: ", status)
    print("Token: ", idToken)

    info = auth.get_account_info(idToken)
    print("Info: ", info)

    codigoativacao = random.randrange(1, 1000000)

    print("Código Aleatório", codigoativacao)

    enviamsg(codigoativacao, destino_email)

    codigoverificacao = input("Favor digite o código que enviamos ao teu email:")


    if status != "":
        print("Email está cadastrado, vou analisar a segunda autenticação ...\n")

        # verificação:

        if float(codigoverificacao) == float(codigoativacao):

            print("Usuário verificado e autenticado !\n")

        else:
            print("Usuário não autenticado.\n")

