from flask import Flask, request, jsonify
from api import api

#Main flask app class for API

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api') # register api class as a blueprint, done to make code clean

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, debug=True) # runs on port 5000 with debug mode on