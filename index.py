from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


@app.route("/")
def main():
	return render_template("base.html")

@socketio.on("message")
def handle_message(msg):
	send(msg, broadcast=True)


	
if __name__ == '__main__':
	app.run(debug=True)