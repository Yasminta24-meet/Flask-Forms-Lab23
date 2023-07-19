from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "YasminQt"
password = "1234"
facebook_friends=["Loai","Kenda","Jihad", "George", "Fouad", "Gi", "Sergey"]


@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method=='POST':
		name = request.form['username']
		psw = request.form['password']
		if name == username and psw == password:
			return redirect(url_for('home'))
	return render_template('login.html')


@app.route('/home', methods=['GET','POST'])
def home():
	return render_template('home.html', friends=facebook_friends)

@app.route('/friend_exists/<string:name>')
def friends(name):
	return render_template('friend_exists.html', n=name in facebook_friends )





  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
