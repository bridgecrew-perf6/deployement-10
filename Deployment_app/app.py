from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return f'Hello Dipankar'

@app.route('/gallary')
def gallary():
    return render_template('gallary.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run(debug = True)