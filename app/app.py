from os import name
from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    nick = request.form.get("nick")
    return render_template("Login.html", nick=nick)

@app.route('/Crear')
def crear():
    name_sala = request.form.get("name_sala")
    contrasenia = request.form.get("contrasenia")
    return render_template('Crear.html', name_sala=name_sala, contrasenia=contrasenia)

@app.route('/Ingresar')
def ingresar():
    contrasenia = request.form.get("contrasenia")
    return render_template('Ingresar.html', contrasenia=contrasenia)

@app.route('/Tutor')
def tutor():
    return render_template('Tutor.html')

@app.route('/Pupilo')
def pupilo():
    return render_template('Pupilo.html')

if __name__ == "__main__":
    app.run(port = 3000, debug = True)
