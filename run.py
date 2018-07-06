from flask import Flask, render_template, jsonify
from random import *
from flask_cors import CORS
app = Flask(__name__, 
            static_folder = "./dist/static",
            template_folder = "./dist")

cors = CORS(app, resources={r"/api/*":{"origins":"*"}})
@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1,100)
    }
    return jsonify(response)
