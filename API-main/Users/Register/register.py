from Users.Register.encript import encriptpassword

#Validate and create slq instruction for register
def register(mail:str,name:str,password:str):
    '''This function need mail,name, password, returns the query or dictionary with 'msj':'param error'//'register error' '''
    try:
        if (mail and name and password)!= '':
                return {'mail':mail,'name':name,'password':password}
        else:
            return {'msj':'param error'}
    except:
        return {'msj':'register error'}

#Create the hash of password and create the qsl query for save
def setusr(mail:str,name:str,password:str):
    '''This function need mail, name, password, returns the query or dictionary with 'msj':'param error'//'setusr error' '''
    try:
        if (mail and name and password)!= '':
            enpass = encriptpassword(password)
            return f"INSERT INTO USUARIOS VALUES('{mail}','{name}','{enpass}');"
        else:
            return {'msj':'param error'}
    except:
        return {'msj':'setusr error'}

#Vlidate if exist on database
def isusr (mail:str):
    '''This function need mail, and returns a sql query for search usr'''
    try:
        if mail != '':
            return f"SELECT * FROM USUARIOS WHERE MAIL like '{mail}';"
        else:
            return {'msj':'mail error'}
    except:
        return {'msj':'isusr error'}