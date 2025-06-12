from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
 
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
 
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == '1' and form.password.data == '1':
            return redirect(url_for('home'))
        else:
            return render_template('login2.html', form=form, error='Invalid credentials')
    return render_template('login2.html', form=form)
 
@app.route('/home')
def home():
    return render_template('home.html')
 
@app.route('/project_management')
def project_management():
    return render_template('pm.html')
 
@app.route('/feasibility_study')
def feasibility_study():
    return render_template('dropdown1.html')
 
@app.route('/Project planning')
def project_planning():
    return render_template('dropdown2.html')
 
@app.route('/Project_Execution')
def Project_Execution():
    return render_template('dropdown3.html')
 
@app.route('/Project Termination')
def Project_Termination():
    return render_template('dropdown4.html')

@app.route('/learn More')
def develop():
    return render_template('develop.html')


 
 
if __name__ == '__main__':
    app.run(debug=True)
 