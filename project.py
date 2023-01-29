# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Harsha" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/Father")
def home():

    name = "Prasad" # write your name
    age = "46" # write your age

    return render_template('Father.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/Mother")
def home():

    name = "Indu" # write your name
    age = "42" # write your age

    return render_template('Mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/Friend")
def home():

    name = "Charan" # write your name
    age = "12" # write your age

    return render_template('Friend.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)