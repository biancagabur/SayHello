from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'manbearpig_Mudmaan88'


@app.route('/hello')
def index():
    flash("What's your name?")
    return render_template('index.html')


@app.route('/greet',methods=['POST'])
def greet():
    user_input = request.form['name_input']
    flash(f'Hi, {user_input}, great to see you!')
    return render_template('index.html')