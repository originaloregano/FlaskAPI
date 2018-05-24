from flask import Flask, render_template
from flask_github import Github

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return github.authorize()

app.config['GITHUB_CLIENT_ID'] = 'XXX'
app.config['GITHUB_CLIENT_SECRET'] = 'YYY'

github = GitHub(app)
if __name__ == '__main__':
    app.run(debug=True)
