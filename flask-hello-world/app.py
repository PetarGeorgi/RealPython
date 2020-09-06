#-----Flask Hello World ---------#

# import the FLask class from the Flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# use decorator pattern to lunk
#view function to a  URL
@app.route('/')
@app.route('/hello')

# define a view using the function, which returns a string
def hello_world():
	return "Hello, World!"

#start development server using run() method

if __name__ == '__main__':
	app.run()