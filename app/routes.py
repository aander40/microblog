from app import application
from flask import render_template, flash, redirect
from app.forms import LoginForm

@application.route('/')
@application.route('/index')
def index():
    user = {'username':"loser"}
    posts = [
        {
            "author": {"username":"John"},
            "body": "Get ready to rumble!"
        },
        {
            "author": {"username":"Joe"},
            "body": "I can't even right now."
        }
        
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@application.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)