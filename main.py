from flask import Flask, make_response, request, jsonify
from db import Products

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config.update(TEMPLATES_AUTO_RELOAD=True)

@app.route('/products', methods=['GET'])
def get_products():
    return make_response(
        jsonify(Products)
    )

@app.route('/products', methods=['POST'])
def create_product():
    item = request.json
    Products.append(item)
    response = make_response("Success")
    response.status_code = 200
    return response

app.run()
