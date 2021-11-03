# importar o pyrebase4 no pip
import pyrebase

def criacaocadastro (user, password):

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

    status = auth.create_user_with_email_and_password(user,password)
    #status = auth.sign_in_with_email_and_password(user,password)
    idToken = status["idToken"]

    print("Resultado: ", status)
    print("Token: ", idToken)

    if idToken != "":
        print("Usuário cadastrado com sucesso")
    else:
        print("Não foi possível efetuar o cadastramento")