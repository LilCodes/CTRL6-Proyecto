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

@app.route('/Ingresar')
def ingresar():
    return render_template('Ingresar.html')

@app.route('/Crear')
def crear():
    return render_template('Crear.html')

"""
@app.route('/Crear.html')
def game():
    return render_template('Admin.html')

@app.route('/Ingresar.html')
def game():
    return render_template('Pupilo.html')
"""

#PROBANDO EL GIT HUB..

if __name__ == "__main__":
    app.run(port = 3000, debug = True)
