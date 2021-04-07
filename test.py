from flask import Flask, render_template
app = Flask(__name__)

'''
Test 1
@app.route('/')
def Home():
    return "<h1>Hello World!</h1>"

@app.route("/John")
def John():
    return "Hellow John!"
'''

'''
@app.route("/")
def hellow ():
    return 'Open a new tab and enter /Welcome/name for URL'

@app.route('/Welcome/<name>')
def Welcome_name(name):
    return 'Welcom ' + name + '!' 
'''


@app.route('/')
def Home():
    return render_template("home.html")

@app.route('/aboutUs')
def AboutUs():
    return render_template("aboutUs.html")

@app.route("/John")
def John():
    return "Hellow John!"


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=80)