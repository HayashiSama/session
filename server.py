from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = '01189998819991197253'

@app.route('/')
def index():
  session['counter'] +=1;
  return render_template("index.html", counter=session['counter'])

@app.route('/counter2', methods=['POST'])
def plustwo():
  session['counter'] +=1;
  return redirect("/")

@app.route('/resetcounter', methods=['POST'])
def reset():
  session['counter'] = 0;
  return redirect("/")

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # here we add two properties to session to store the name and email
   session['name'] = request.form['name']
   session['email'] = request.form['email']

   return redirect('/show')

@app.route('/show')
def show_user():
  return render_template('user.html', name=session['name'], email=session['email'])


app.run(debug=True)