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

"""
email=input("Enter email: ")
password=input("Enter password: ")
storeName=input("Enter storeName: ")
store={
      "email":email,
      "password":password,
      "storeName":storeName
    }
"""
@app.route('/', methods =['POST'])
def signup () :
   #data = db.storeOwner
   
   req_Json= request.json
   name=req_Json['name']
   return jsonify({'response', name})
   
   

   
  
  

app.run(debug=True)