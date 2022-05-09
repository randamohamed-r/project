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

#name= input()

@app.route('/', methods=['POST'])
def signup():
    data = db.storeOwner
    req_Json= request.json
    email=req_Json['email']
    password=req_Json['password']
    storeName=req_Json['storeName']
    return({'response': {email, password , storeName}})
    
    #data.insert_one({'name': name})



  
  
app.run(debug=True) 
 
 