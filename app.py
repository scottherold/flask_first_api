from flask import Flask, jsonify, request, render_template

# __name__ gives each file a unique name
app = Flask(__name__)

# ===== Data =====
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

# ===== HTTP requests =====
@app.route('/') # root URL
def home():
    return render_template('index.html')

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json() # data sent to the endpoint from the browser
    # create new store
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    # add new store to local data
    stores.append(new_store)
    return  jsonify(new_store) # flask's way of returning JSON

# <type:variable> is a special syntax for flask to allow for a parameter
# to be extracted from the route string
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'}) # no store found

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores}) # flask's way of returning JSON

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            request_data = request.get_json() # data sent to the endpoint from the browser
            # create new item
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            if store['items']:
                return jsonify({'items': store['items']})
            return jsonify({'message': 'store does not have any items'}) # no items found
    return jsonify({'message': 'store not found'}) # no store found

# ==== Port =====
app.run(port=5000)