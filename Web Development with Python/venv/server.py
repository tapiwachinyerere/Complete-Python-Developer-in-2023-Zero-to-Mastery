from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return 'Hello, Tapiwa! I didn\'t know you liked blogs'

@app.route('/blog/2020/dogs')
def blog2():
    return 'Hello, Tapiwa! You love dogs too?'