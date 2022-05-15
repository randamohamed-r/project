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
""" req_Json= request.json
   email=req_Json['email']
   password=req_Json['password']
   storeName=req_Json['storeName']
"""
@app.route('/', methods =['POST' , 'GET'])
def signup () :
     result = db.storeOnwer.find({location: {'$near':[15,46]}})

     #result = db.storeOwner.find_one({'email': email},{'_id':1})
     print(result)
     return json.dumps(result, indent=4, default = json_util.default)
  
    

     
    
  

app.run(debug=True)