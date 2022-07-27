from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY'] = 'super-secret-key'


username = "llo2ay"
password = "123"


@app.route('/', methods = ["GET", "POST"])  # '/' for the default page
def login():
	if request.method == "GET":
		return render_template('login.html')
	
	else:
		user= request.form['user']
		pas = request.form['pass']
		if user == username and pas == password:
			return redirect(url_for('home'))
		else:
			return render_template('login.html')

@app.route('/home')
def home():
	facebook_friends=["Arthur","Ilan","Shane", "Kitai", "Daniel", "Ioana"]
	return render_template('home.html', facebook_friends = facebook_friends)

@app.route('/friend_exists/<string:friend>')
def friends (friend):
	facebook_friends=["Arthur","Ilan","Shane", "Kitai", "Daniel", "Ioana"]
	return render_template('friend_exists.html',friend = friend, facebook_friends = facebook_friends)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)