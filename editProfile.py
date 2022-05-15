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

@app.route('/', methods =['GET','POST'])
def edit () :

  req_Json= request.json
  Id=req_Json['Id']
  storeName=req_Json['storeName']
  phone_number=req_Json['phone_number']
  facebook_link=req_Json['facebook_link']
  another_link=req_Json['another_link']
  image=req_Json['image']
  longtiude=req_Json['longtiude']
  latitude=req_Json['latitude']

  data = db.storeOwner.update_one({"_id":ObjectId(Id)}, 
   {   "$set": {"storeName":storeName, "contacts":{"phone_number":phone_number, "facebook_link":facebook_link, "another_link":another_link}, "location":{longtiude:longtiude, latitude:latitude} }  } )

  return 'Product updated successfully.'

   
  
  

app.run(debug=True)