from flask import Flask, request,session
from Users.Verificate.verificate import callback
from Users.users import usrlogin,verif
from DataBase.database import DataBase
from Settings.settings import xml

app = Flask('app')
app.secret_key = "Asusgo-proyect"
settings = xml()#Read setings on xml
database = DataBase(settings)#Create de database connection

#login route
@app.route('/api/login')
def login():
    try:
        context = usrlogin()
        return context
    except:
        return {'msj':'error'}

#Verif route
@app.route("/callback")
def verif():
    try:
        context = verif(request.url)
        return context
    except:
        return {'msj':'error'}

#Test route
@app.route("/api")
def index():
    return {'msj':'conected'}

if __name__ == "__main__":
    app.run(debug=True)