from flask import Flask
from db import Products

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return Products

app.run()