import json
import os
from flask import abort, Flask, request
from db import SimpleKVDb


app = Flask(__name__)
db = SimpleKVDb(os.path.expanduser('~')+'/file.txt')

@app.route('/get', methods=['GET'])
def get_record():
    if request.content_type == 'application/json':
        req = request.json
        k = req['key']
        v = db.get(k)
        if v is not None:
            response = {k:v}
        else:
            abort(404)
        return response
    else:
        return 'Content type is not supported yet.'

@app.route('/get_all', methods=['GET'])
def get_all_records():
    if request.content_type == 'application/json':
        response = db.get_all()
        return response
    else:
        return 'Content type is not supported yet.'

@app.route('/set', methods=['PUT'])
def set_record():
    if request.content_type == 'application/json':
        req = request.json
        k = req['key'] if 'key' in req.keys() else None
        v = req['value'] if 'value' in req.keys() else None
        if k is not None and v is not None:
            db.set(k,v)
            return '',200
        else:
            abort(404)
    else:
        return 'Content type is not supported yet.'

@app.route('/flush', methods=['PUT'])
def flush_db():
    if request.content_type == 'application/json':
        db.flush()
        return '',200
    else:
        return 'Content type is not supported yet.'

@app.route('/delete', methods=['DELETE'])
def delete_record():
    if request.content_type == 'application/json':
        req = request.json
        response = db.delete(req['key'])
        if response:
            return '',200
        else:
            return '',404
    else:
        return 'Content type is not supported yet.'

if __name__ == '__main__':
    app.run()
