from flask import Flask, render_template
import players

app = Flask(__name__)

@app.route('/')
def home():
	players.updateScore()
	return render_template('home.html', players=players.getPlayers())

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=False,port=5000,host='0.0.0.0')