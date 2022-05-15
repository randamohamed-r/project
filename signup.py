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


@app.route('/', methods =['POST' , 'GET'])
def signup () :
   #data = db.storeOwner
   
   req_Json= request.json
   email=req_Json['email']
   password=req_Json['password']
   storeName=req_Json['storeName']

   Filter = {"email":email}
   if db.storeOwner.count_documents(Filter):
     return("Thsi email already has an store. Try another one.")
   else:
     db.storeOwner.insert_one({"email": email, "password": password, "storeName": storeName})
     result = db.storeOwner.find_one({'email': email},{'_id':1})
     print(result)
     return json.dumps(result, indent=4, default = json_util.default)
  
    

     
    
  

app.run(debug=True)