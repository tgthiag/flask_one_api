from flask import Flask, make_response, jsonify
from db import Products

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return make_response(
        jsonify(Products)
    )

app.run()