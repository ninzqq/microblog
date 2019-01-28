
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Janne'}
    posts = [
        {
            'author': {'username': 'Gayy'},
            'body':  'Beautiful day in Gayland!'
        },
        {
            'author': {'username': 'Homo'},
            'body':  'Nice day in Homoland!'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

