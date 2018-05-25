from flask import json
from flask import request
from flask import Flask, render_template
# from flask_github import Github

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/github', methods=['POST'])
def api_github_message():
    if request.headers['Content-Type'] == 'application/json':
        git_info = json.dumps(request.json)
        print git_info
        return json.dumps(request.json)
# @app.route('/login')
# def login():
#     return github.authorize()

@app.errorhandler(404)
def not_found(e):
    return 'I dont know what you are talking about, Willis', 404

# app.config['GITHUB_CLIENT_ID'] = 'XXX'
# app.config['GITHUB_CLIENT_SECRET'] = 'YYY'

#setup github-flask
# github = GitHub(app)

if __name__ == '__main__':
    app.run(debug=True)
