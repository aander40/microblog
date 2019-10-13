from app import application
from flask import render_template

@application.route('/')
@application.route('/index')
def index():
    user = {'username':"andy"}
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
