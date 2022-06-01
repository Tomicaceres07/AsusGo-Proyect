from fastapi.responses import RedirectResponse
from fastapi import *
from Users.users import usrlogin,usrregister,usrregisterverif,usrpassreset,usrpassrverif
from DataBase.database import DataBase
from Settings.settings import xml
from param.param import *
import uvicorn

app = FastAPI()#Set app
settings = xml()#Read setings on xml
database = DataBase(settings)#Create de database connection
tempusr = {}#Set a auxiliary dictionay

#User functions

#Test connection with the server
@app.get('/api')
async def test():
    ''' This function returns dictionay with 'msj':'connected' '''
    return {'msj':'connected'}

#Try to login in a user
@app.post('/api/login')
async def log(request: Request):
    ''' This fuction needs input email and password, returns dictionay with 'msj':'error'// return of usrlogin '''
    try:
        if request.mail:
            mail = request.mail
        if request.password:
            password = request.password
        context = usrlogin(mail,password,database)
        return context
    except:
        return {'msj':'error'}

#Try to register new user
@app.post('/api/register')
async def register(request: Request):
    ''' This function need input email, password, name and global dictionary tempusr, returns dictionay with 'msj':'reg error'// return of usrregister '''
    try:
        if request.mail:
            mail = request.mail
        if request.password:
            password = request.password
        if request.name:
            name = request.name
        context = usrregister(mail,name,password,settings,database)
        if context['exist']== False:
            tempusr[mail]=context['code']
        return context
    except:
        return {'msj':'reg error'}

#Verificate email from the new user
@app.get('/api/register/verif/{name}/{mail}/{code}/{password}',response_class=RedirectResponse)
async def registerverif(name:str,mail:str,code:str,password:str):
    ''' This function need on de url name, mail, code and password, returns a redirect from the url on xmlsettings '''
    try:
        context = usrregisterverif(mail,name,password,code,tempusr,database)
        if context['msj']=='usr created':
            return settings[8] #Page of login
        else:
            return settings[9] #Page of register
    except:
        return settings[7] #Page of start

#Reset password from user
@app.post('/api/resetp')
async def resetp(request: Request):
    ''' This function need mail and password, returns dictionary with 'msj':'res error'//returns of usrpassreset '''
    try:
        if request.mail:
            mail = request.mail
        if request.password:
            password = request.password
        context = usrpassreset(mail,password,settings,database)
        if context['exist']== True:
            tempusr[mail]=context['code']
            return context
    except:
        return {'msj':'res error'}

#Verificate password reset email
@app.get('/api/resetp/verif/{name}/{mail}/{code}/{password}',response_class=RedirectResponse)
async def resetpverif(name:str,mail:str,code:str,password:str):
    '''This function need on url name, mail, code and password, returnsa a redirect from the url on xmlsetings '''
    try:
        context = usrpassrverif(mail,password,code,tempusr,database)
        if context['msj']=='usr password updated':
            return settings[8] #Page of login
        else:
            return settings[8] #page of login
    except:
        return settings[9]#page of register

#User functions end

if __name__ == "__main__":
    #Start the server
    uvicorn.run(app, host=settings[10], port=5000)