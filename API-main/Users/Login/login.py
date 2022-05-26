#Validate and create slq instruction for login
from email.errors import InvalidMultipartContentTransferEncodingDefect

def login(mail:str,password:str):
    '''This function need mail, password, returns the query or dictionary with 'msj':'param error'//'login error' '''
    try:
        if (mail and password)!= '':
                return f"SELECT * FROM USUARIOS WHERE MAIL like '{mail}';"
        else:
            return {'msj':'param error'}
    except:
        return {'msj':'login error'}