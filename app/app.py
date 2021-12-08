from os import name
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room, emit

app=Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'


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
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

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
        return redirect(url_for('tutor', name_sala = name))
    else:
        name = request.form.get("name_sala")
        password = request.form.get("contrasenia")
        return redirect(url_for('tutor', name_sala = name))

@app.route('/Tutor/<name_sala>')
def tutor(name_sala):
    return render_template('Tutor.html')

#---------------
@app.route('/Ingresar')
def ingresar():
    return render_template('Ingresar.html')

@app.route('/Ingresar1', methods=['POST','GET'])
def ingresar1():
    if request.method == "GET":
        password1 = request.form["contrasena"]
        return redirect(url_for('pupilo'))
    else:
        password1 = request.form.get("contrasena")
        return redirect(url_for('pupilo'))

@app.route('/Pupilo')
def pupilo():
    return render_template('Pupilo.html')

@socketio.on('send-update', namespace='/chronometer-update')
def text(message):
    print(message)
    emit('chronometerStatus', {'msg': message}, broadcast=True)


#-------------
#-------------
'''
@socketio.on('join', namespace='/chat')
def join(message):
    room = session.get('room')
    join_room(room)
    emit('status', {'msg':  session.get('username') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    emit('message', {'msg': session.get('username') + ' : ' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    username = session.get('username')
    leave_room(room)
    session.clear()
    emit('status', {'msg': username + ' has left the room.'}, room=room)
'''
#-------------
#---------------

if __name__ == "__main__":
    #socketio.on(app)
    app.run(port = 3000, debug = True)
