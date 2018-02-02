# from flask import Flask, render_template
# from flask_socketio import SocketIO, send, emit
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)
#
#
# def ack():
#     print('message was received!')
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @socketio.on('message')
# def handle_message(message):
#     print('received message: ' + str(message))
#     emit('my response', 'Success!')
#
#
# if __name__ == '__main__':
#     socketio.run(app)
