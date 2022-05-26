from Users.Login.verif import verifpassword
from Users.Login.login import login
from Users.Mail.mail import sendmail
from Users.Register.register import isusr, register,setusr
from Users.Resetp.resetp import resetpassword, setnewpassword

#Login function
def usrlogin(mail:str,password:str,database:object):
    '''This function needs email, password, database, returns dictionary with 'msj':'invalid mail or password'//'usr not exist'//'usr login error'//returns of database '''
    try:
        inst = login(mail,password)
        usr = database.datasearch(inst)
        if usr != ():
            data = usr[0]
            ver = verifpassword(password,data[2])
            if ver == True:
                return usr
            else:
                return {'msj':'invalid mail or password'}
        else:
            return {'msj':'usr not exist'}
    except:
        return {'msj':'usr login error'}

#Register function
def usrregister(mail:str,name:str,password:str,settings,database:object):
    '''This function need email, name, password, settings, database, returns dictionay with 'msj':'user already exist'//'user register error'//returns of sendmail '''
    try:
        inst = isusr(mail)
        usr = database.datasearch(inst)
        if usr == ():
            reg = register(mail,name,password)
            context = sendmail(settings[4],reg['mail'],settings[5],'reg',reg['password'],reg['name'])
            context['exist']=False
            return context
        else:
            return {'msj':'user already exist','exist':True}
    except:
        return {'msj':'user register error'}

#Mail register verification
def usrregisterverif(mail:str,name:str,password:str,code:str,temp:dict,database:object):
    '''This function need mail, name, password, code, temp, database, returns dictionary with 'msj':'user created'//'code not valid'//'register verif error' '''
    try:
        if code == temp[mail]:
            inst = setusr(mail,name,password)
            database.datainsert(inst)
            return {'msj':'usr created'}
        else:
            return{'msj':'code not valid'}
    except:
        return {'msj':'register verif error'}

#Send mail for change the password
def usrpassreset (mail:str,password:str,settings,database:object):
    '''This function need mail, password, settings, database, returns dictionay with 'msj':'user not exist'//'usrregister'//sendmail returns'''
    try:
        inst = isusr(mail)
        usr = database.datasearch(inst)
        if usr != ():
            res = resetpassword(mail,password)
            context = sendmail(settings[4],res['mail'],settings[5],'res',res['password'],'')
            context['exist']=True
            return context
        else:
            return {'msj':'user not exist','exist':False}
    except:
        return {'msj':'usrregister error','exist':False}

#Verificate password update
def usrpassrverif (mail:str,password:str,code:str,temp:dict,database:object):
    '''This function need mail, password, code, temp, database, returns dictionary with 'msj':'usr password updated'//'code not valid'//'passverif error' '''
    try:
        print(temp[mail])
        if code == temp[mail]:
            inst = setnewpassword(mail,password)
            database.datainsert(inst)
            return {'msj':'usr password updated'}
        else:
            return{'msj':'code not valid'}
    except:
        return {'msj':'passrverif error'}