from os import name
from flask import Flask, render_template, request, redirect, url_for
from flask.globals import session
from flask_socketio import SocketIO, join_room, leave_room, emit

from flask_session import Session

app=Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

socketio = SocketIO(app, manage_session=False)

values = {
    'slider1': 25,
    'slider2': 0,
}

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
        nm = request.form['nm']
        session['nick'] = request.form['nm']
        session['nm'] = nm
        return redirect(url_for('success',nm = nm))
   else:
        if (session.get('nm') is not None):
            nm = request.form.get('nm')

            session['nm'] = nm
            return redirect(url_for('success',nm = nm))
        else:
            return redirect(url_for('index'))

@app.route('/main')
def success():
    return render_template("Login.html")

#-----------
@app.route('/Crear')
def crear():
    return render_template('Crear.html')

@app.route('/Crear1', methods=['POST','GET'])
def crear1():
    if request.method == "GET":
        name = request.form["name_sala"]
        password = request.form["contrasenia"]

        session['nm'] = name
        session['nm'] = password
        return redirect(url_for('tutor', session = session))
    else:
        if (session.get('nm') is not None):
            name = request.form.get("name_sala")
            password = request.form.get("contrasenia")

            session['nm'] = name
            session['nm'] = password
            return redirect(url_for('tutor', session = session))
        else:
            return redirect(url_for('index'))

@app.route('/Tutor')
def tutor():
    return render_template('Tutor.html')

#---------------
@app.route('/Ingresar')
def ingresar():
    return render_template('Ingresar.html')

@app.route('/Ingresar1', methods=['POST','GET'])
def ingresar1():
    if request.method == "GET":
        password1 = request.form["contrasena"]

        session['nm'] = password1
        return redirect(url_for('pupilo'))
    else:
        if (session.get('nm') is not None):
            password1 = request.form.get("contrasena")

            session['nm'] = password1
            return redirect(url_for('pupilo'))
        else:
            return redirect(url_for('index'))

@app.route('/Pupilo')
def pupilo():
    return render_template('Pupilo.html')

@socketio.on('send-update', namespace='/chronometer-update')
def text(message):
    print(message)
    emit('chronometerStatus', {'msg': message}, broadcast=True)


#-------------
#-------------

@socketio.on('join', namespace='/chat')
def join(message):
    #room = session.get('name')
    #print(room)
    #join_room(room)
    print("Restarting web")
    emit('status', {'msg':  session.get('nick') + ' ha entrado a la sala. ¡Saludos!.'})


@socketio.on('message', namespace='/chat')
def text(message):
    #room = session.get('name')
    #, room=room
    emit('message', {'msg': session.get('nick') + ' : ' + message['msg']},  broadcast=True)

#-------------
#---------------

if __name__ == "__main__":
    app.run(port = 3000, debug = True)