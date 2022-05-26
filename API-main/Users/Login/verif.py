from werkzeug.security import check_password_hash

#Verificate password an saved hash
def verifpassword(password:str,hash:str):
    '''This function needs password and hash, returns a bool'''
    context = check_password_hash(hash,password)
    return context