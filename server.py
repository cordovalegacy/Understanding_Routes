from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello_World():
    return "Hello World"

@app.route('/dojo')
def Dojo():
    return "Dojo!"

@app.route('/say/<name>')
def Flask(name):
    return f"Hi {name.capitalize()}!"
##Uses .capitalize method so you don't have to manually type a capital first letter in URL

@app.route('/repeating/<int:num>/<string:name>')
def Repeat(num, name):
    result = ''
    for i in range(0, num):
        return f"Repeating: {name.capitalize()*num}!"
##Uses .capitalize method so you don't have to manually type a capital first letter in URL

if __name__=='__main__':
    app.run(debug = True)