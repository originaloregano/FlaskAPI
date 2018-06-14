from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
api = "https://api.github.com"

@app.route('/api', methods=['GET'])
def getApi():
  r = requests.get(api)
  api_json = r.json()
  return jsonify(api_json)

@app.route('/api/<username>', methods=['GET'])
def getUser(username):
  """ grab github profile"""
  user_endpoint = api+"/users/"+username
  user_request = requests.get(user_endpoint)
  user_data = user_request.json()
  return user_data


def manipulateData(user_data):
    keys = ['followers', 'starred_url', 'public_repos']
    new_data = {}
    for key in keys:
        new_data[key] = user_data[key]
    return new_data

# @app.route('/display/<display>', methods=['GET'])
def displayPretty(user_data):
    """pretty print key and values"""
    # user_data = getUser(display)
    variable = ""
    for key in user_data:
        variable += "{}: {}".format(key, user_data[key]) + "<br>"
    return variable

@app.route("/everything/<param>")
def retrieveAndDisplay(param):
    user_data = getUser(param)
    display_data = guts(user_data)
    return displayKeys(display_data)



# in order to get more data such as repos from github, need authentication
# @app.route('/api/<username>/<section>', methods=['GET'])
# def getUser(section):
#   user_endpoint = api+"/users/{}/{}".format(username,section)
#   user_request = user_request.get(user_endpoint)
#   user_data = user_request.json()
#   return jsonify(user_data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
