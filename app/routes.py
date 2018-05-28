from flask import request, redirect, render_template, url_for
from app import app

@app.route('/')
def home():
    return render_template('home.html')


# @app.route('/github', methods=['POST'])
# def api_github_message():
#     if request.headers['Content-Type'] == 'application/json':
#         git_info = json.dumps(request.json)
#         print git_info
#         return json.dumps(request.json)
