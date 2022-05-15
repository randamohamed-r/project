import pymongo
from pymongo import MongoClient
import json
from bson import ObjectId, json_util
from bson.json_util import dumps
from flask import Flask, render_template, jsonify , Response, request


app=Flask(__name__)

try:
  client = MongoClient(host="localhost", port=27017)
  db = client.Agrosnap
  client.server_info()
except:
  print('ERROR')

@app.route('/<id>', methods = ['GET'])
def delete(id):
    data = db.product.delete_one({'_id':ObjectId(id)})
    return 'Product deleted successfully.'
app.run(debug=True)