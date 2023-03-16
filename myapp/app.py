from flask import Flask, render_template, jsonify
from flask import request
from flask import redirect
from flask import url_for

from Alumnos.routes import alumnos
from Directivos.routes import directivos
from Maestros.routes import maestros

app=Flask(__name__)
app.config['DEBUG']=True

@app.route("/",methods=['GET'])
def home():
    return jsonify({'Datos':'Hola'})

app.register_blueprint(alumnos)
app.register_blueprint(directivos)
app.register_blueprint(maestros)

if __name__=='__main__':
    app.run()
