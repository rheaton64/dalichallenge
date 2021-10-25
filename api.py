from flask import Blueprint, request, jsonify, abort
import json, itertools

# API blueprint for flask app

api = Blueprint('api', __name__) # make blueprint called api

# load json files into dicts
pubdata = json.load(open('pubdata.json'))
anondata = json.load(open('anondata.json'))

# returns all public data
@api.route('/data/pub/all')
def public():
    return jsonify(pubdata)

# returns all anonymous data
@api.route('/data/anon/all')
def anon():
    return jsonify(anondata)

# returns all of both data sets
@api.route('data/all/all')
def alldata():
    return jsonify(pubdata + anondata)

# returns public data with query params & lets you add new public data
@api.route('/data/pub', methods=(['GET', 'POST']))
def pubargs():
    if request.method == 'GET':
        params = request.args

        result = []

        # for each keys that is in both the params and the data, 
        # if that object has matching value and isn't already in result, add it to results
        for p in anondata:
            for param in params:
                if param in p.keys() and p[param] == params.get(param) and not p in result:
                    result.append(p)

        return jsonify(result)

    if request.method == 'POST':

        # adds the post request's data to public data
        if not request.json:
            abort(400)

        data = request.json
        pubdata.append(data)

        return jsonify(data)
    

# returns anon data with query params & lets you add new anon data
@api.route('data/anon', methods=(['GET', 'POST']))
def anonargs():
    if request.method == 'GET':
        params = request.args

        result = []

        # for each keys that is in both the params and the data, 
        # if that object has matching value and isn't already in result, add it to results
        for p in anondata:
            for param in params:
                if param in p.keys() and p[param] == params.get(param) and not p in result:
                    result.append(p)

        return jsonify(result)

    if request.method == 'POST':

        #adds the post request's data to anon data
        if not request.json:
            abort(400)

        data = request.json
        anondata.append(data)

        return jsonify(data)

# returns data from both sets with query params
@api.route('data/all', methods=(['GET']))
def allargs():
    params = request.args

    result = []

    # for each keys that is in both the params and the data, 
    # if that object has matching value and isn't already in result, add it to results
    for p in itertools.chain(anondata, pubdata):
        for param in params:
            if param in p.keys() and p[param] == params.get(param) and not p in result:
                result.append(p)

    return jsonify(result)