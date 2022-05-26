from Users.Register.encript import encriptpassword

#Create a dictionary with mail and password
def resetpassword(mail:str,password:str):
    '''This function need mail and password,returns dictionary with 'msj':'param error'//'reset password error' '''
    try:
        if (mail and password)!= '':
            return {'mail':mail,'password':password}
        else:
            return {'msj':'param error'}
    except:
        return {'msj':'reset password error'}

#Create the password_hash and query for update the password user
def setnewpassword(mail:str,password:str):
    '''This function need mail and password,returns dictionary with 'msj':'paramerror'//'setusr error' '''
    try:
        if (mail and password)!= '':
            enpass = encriptpassword(password)
            print(enpass)
            return f"UPDATE USUARIOS SET CONTRASEÑA= '{enpass}' WHERE MAIL LIKE '{mail}';"
        else:
            return {'msj':'param error'}
    except:
        return {'msj':'setusr error'}