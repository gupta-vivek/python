from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index2.html')


@socketio.on('my_event', namespace='/test')
def handle_message(message):
    print('received message: ' + str(message))
    emit('my response', 'HAHAHA!', namespace='/test')


if __name__ == '__main__':
    socketio.run(app)