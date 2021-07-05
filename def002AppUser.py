
# App Python methods
# Store this code in 'app.py' file
from flask import Flask, render_template, request, redirect, url_for, session
import re
import pyodbc
import strconn
import runSqlQry



app = Flask(__name__)


app.secret_key = 'your secret key'


@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'address' in request.form and 'city' in request.form and 'country' in request.form and 'postalcode' in request.form and 'organisation' in request.form:
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		organisation = request.form['organisation']
		address = request.form['address']
		city = request.form['city']
		state = request.form['state']
		country = request.form['country']	
		postalcode = request.form['postalcode']
		
		qryResult = runSqlQry.runQry('SELECT * FROM accounts WHERE username = ?', (username))
		
		if qryResult:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'name must contain only characters and numbers !'
		else:
			runSqlQry.runQryWithCommit('INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (username, password, email, organisation, address, city, state, country, postalcode))
			
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)



@app.route("/update", methods =['GET', 'POST'])
def update():
	msg = ''
	if 'loggedin' in session:
		if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'address' in request.form and 'city' in request.form and 'country' in request.form and 'postalcode' in request.form and 'organisation' in request.form:
			username = request.form['username']
			password = request.form['password']
			email = request.form['email']
			organisation = request.form['organisation']
			address = request.form['address']
			city = request.form['city']
			state = request.form['state']
			country = request.form['country']	
			postalcode = request.form['postalcode'] 
				
			qryResult = runSqlQry.runQry('SELECT * FROM accounts WHERE username = ?', (username))
			
			if qryResult:
				msg = 'Account already exists !'
			elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
				msg = 'Invalid email address !'
			elif not re.match(r'[A-Za-z0-9]+', username):
				msg = 'name must contain only characters and numbers !'
			else:
				runSqlQry.runQryWithCommit('UPDATE accounts SET username =?, password =?, email =?, organisation =?, address =?, city =?, state =?, country =?, postalcode =? WHERE id =?', (username, password, email, organisation, address, city, state, country, postalcode, (session['id'] ) ))
				
				msg = 'You have successfully updated !'
		elif request.method == 'POST':
			msg = 'Please fill out the form !'
		return render_template("update.html", msg = msg)
	return redirect(url_for('login'))


