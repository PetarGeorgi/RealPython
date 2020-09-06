#-----Flask Hello World ---------#

# import the FLask class from the Flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# use decorator pattern to lunk
#view function to a  URL
@app.route('/')
@app.route('/hello')

#error handling
#app.config["DEBUG"] = True

# define a view using the function, which returns a string
def hello_world():
	return "Hello, World!"

# dynamic route
@app.route('/test/<search_query>')
def search(search_query):
	return search_query

@app.route("/integer/<int:value>")
def int_type(value):
	print(value + 1)
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print(value + 1)
	return "correct"

@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	return "correct"

@app.route("/name/<name>")
def index(name):
	if name.lower() == 'michael':
		return 'Hello, {}'.format(name), 200
	else:
		"Not found", 404

#start development server using run() method

if __name__ == '__main__':
	app.run()