"""\
First prototype of the actual application
"""
import logging

from markupsafe import escape

from flask import render_template
from flask import make_response, redirect, url_for
from flask import request, session

from flask import Flask

#from .data import data

app = Flask(__name__)
app.secret_key = b'ADJUST THIS LATER' # XXX: Secret key outside git

logging.basicConfig(level=logging.INFO)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        logging.info('Received POST request: name=%s' % name)
        if name:
            session['name'] = name
            return redirect(url_for('index'))
    # else - No POST data
    name = session.get('name')
    return render_template('index.html', name=name)

@app.route('/logout/')
def logout():
    # remove the username from the session if it's there
    session.pop('name', None)
    return redirect(url_for('index'))

@app.route('/find/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
