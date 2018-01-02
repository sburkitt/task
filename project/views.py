#project views
import sqlite3
from functools import wraps 
from flask import Flask, flash, redirect, render_template, request, session, url_for

#config
app = Flask(__name__)
app.config.fromobject('__config__')

#helper functions

def connect_db():
	return sqlite3.connect(app.config['DATABASE_PATH'])

def login_required(test): 
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else: 
			flash('Log in first')
			return redirect(url_for('login'))
	return wrap

#route handlers

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('Logged Out')
	return redirect(url_for('login'))

@app.route('/', methods = ['GET','POST'])
def login():
	error= None
	status_code = 200
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = 'INVALID CREDENTIALS'
			return render_template('login.html', error = error)
		else:
			session['logged_in'] = True
			flash('WELCOME')
			return redirect(url_for('tasks'))
	return render_template('login.html', error=error), status_code

