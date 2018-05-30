# from app import app
# app.run(debug=True)
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

#POST - used to receive data
#GET - used to send data back only
@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/store/<string:name>')
def get_store(name):
    #Iterate over stores
    #if the store name matches, return it
    #if none match, return an error message
    if store['name'] == name:
        return jsonify(store)
return jsonify({'message': 'store not found'})

@app.route('/store') #route only does GET, so need to tell it post
def get_store():
    return jsonify({'store': stores}) #make into dictionary

@app.route('/store', methods='POST')
def create_store():
        request_data = request.get_json() #converts json string to python dictionary
        new_store = {
            'name': request_data['name'],
            'items': []
        }
        stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

app.run(debug=True)
