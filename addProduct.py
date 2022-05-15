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



@app.route('/', methods =['POST'])
def addProduct () :
   data = db.product

   req_Json= request.json
   name=req_Json['name']
   price=req_Json['price']
   image=req_Json['image']
   store_id=req_Json['store_id']
   
   Filter={"name":name}
   if data.count_documents(Filter):
     return "This product already exists. Try another one."
   else: 
      data.insert_one({"name":name, "price":price, "image":image, "store_id":store_id })
      return 'Product inserted successfully.'

   
  

app.run(debug=True)