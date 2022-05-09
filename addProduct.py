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

name=input("Enter name: ")
price=input("Enter price: ")
image=input("Enter image: ")
store_id=input("Enter store_id: ")

@app.route('/', methods =['GET','POST'])
def addProduct () :
   data = db.product
   store={
      "name":name,
      "price":price,
      "image":image,
      "store_id":store_id
    }
   Filter={"name":name}
   if data.count_documents(Filter):
    return "This product is already exists. Try another one."
   else: 
     data.insert_one(store)
     return 'Product inserted successfully.'

   
  
  

app.run(debug=True)