from flask import Flask, render_template
from WebUI import WebUI

app = Flask(__name__)
ui = WebUI(app,debug=True)

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello1.html', name = user)


@app.route('/myindex')
def myindex():
   return '<html><body><h1>Hello World HTML Code Returned </h1></body></html>'


@app.route('/rendertemplate')
def index():
   return render_template('hello.html')


@app.route('/flask')
def hello_flask():
	return 'Hello Flask'

@app.route('/python/')
def hello_python():
	return 'Hello Python'


@app.route("/")
def fmain():
	return "Welcome !"

if __name__ == "__main__":
	ui.run()


