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


@app.route('/', methods=['POST'])
def test():
    data = db.storeOwner
    req_Json= request.json
    email=req_Json['email']
    password=req_Json['password']
    storeName=req_Json['storeName']
   # return({'response': name })
    data.insert_one({'email': email, 'password':password, 'storeName':storeName})
    return({'email': email, 'password': password, 'storeName': storeName })

    
    


    


  
  
app.run(debug=True) 
 
 