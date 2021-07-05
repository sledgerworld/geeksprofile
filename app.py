
# App Python methods
# Store this code in 'app.py' file
from flask import Flask, render_template, request, redirect, url_for, session
import re
import pyodbc
import strconn
import runSqlQry


import def001Login
import def002AppUser



app = Flask(__name__)
app.secret_key = 'your secret key'


@app.route("/index")
def index():
	if 'loggedin' in session:
		return render_template("index.html")
	return redirect(url_for('login'))


@app.route("/display")
def display():
	if 'loggedin' in session:
    		
		qryResult = runSqlQry.runQry('SELECT * FROM accounts WHERE id = ?', (session['id'] ))
			
		return render_template("display.html", qryResult = qryResult)
	return redirect(url_for('login'))

if __name__ == "__main__":
	app.run(host ="localhost", port = int("5000"))
