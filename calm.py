# Begun 2016-07-30 

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def load_page_home():
    return render_template('index.html')

@app.route('/learning')
def load_page_projects():
    return render_template('learning/learning-directory.html')

# ======================================= #
# Nav Bar Links
# ======================================= #

@app.route('/about')
def load_page_about():
    return render_template('about.html')

# ======================================= #
# Error Pages
# ======================================= #

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not-found.html'), 404

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
