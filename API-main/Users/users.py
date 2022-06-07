from Users.Verificate.verificate import *
from Users.Login.login import login

#Login
def usrlogin():
    try:
        context =url_login()
        return context
    except:
        return {'msj':'error'}

#Verificate
def verif(url,database):
    try:
        context =callback(url)
        print(context)

        #obtains the direction of the mail
        mail_direct = context['email']
        mail_direct = mail_direct['@','.']

        #verificate the email
        if (mail_direct == 'gmail') and (context['verif']==True):
            return context
        else:
            return {'msj':'mail not valid'}
    except:
        return {'msj':'error'}