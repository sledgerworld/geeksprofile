
# App Python methods
# Store this code in 'app.py' file
from flask import Flask, render_template, request, redirect, url_for, session
import re
import pyodbc
import strconn
import runSqlQry


app = Flask(__name__)


app.secret_key = 'your secret key'


@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']


		qryResult = runSqlQry.runQry('SELECT * FROM accounts WHERE username = ? AND password = ?', (username, password))

		if qryResult:
			session['loggedin'] = True
			session['id'] = qryResult.id
			session['username'] = qryResult.username
			msg = 'Logged in successfully !'
			return render_template('index.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))


