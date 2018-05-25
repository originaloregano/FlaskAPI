from flask import json
from flask import request
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def api_route():
    return render_template('home.html')

@app.route('/github', methods=['POST'])
def api_github_message():
    if request.headers['Content-Type'] == 'application/json':
        git_info = json.dumps(request.json)
        print git_info
        return json.dumps(request.json)

if __name__ == '__main__':
    app.run(debug=True)
