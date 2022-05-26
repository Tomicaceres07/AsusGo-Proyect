from werkzeug.security import generate_password_hash

#Create a password hash
def encriptpassword(password:str):
    '''this function need password and return the password_hash'''
    context =generate_password_hash(password)
    return context
