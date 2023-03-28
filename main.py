from flask import Flask, make_response, request, jsonify
from db import Products

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config.update(TEMPLATES_AUTO_RELOAD=True)

@app.route('/products', methods=['GET'])
def get_products():
    return make_response(
        jsonify(
            message='Products list',
            data=Products
        )
    )

@app.route('/products', methods=['POST'])
def create_product():
    item = request.json
    Products.append(item)
    return make_response(
        jsonify(
            message='Successfully registered',
            data=item
        )
    )

app.run()
