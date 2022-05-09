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





#print("which to update? T OR F \n Name: ")
#ifName=input()
#print("Price: ")
#ifPrice=input()
#print("Image: ")
#ifImage=input()




@app.route('/', methods =['GET','POST'])
def edit () :
   
   req_Json= request.json
   ID=req_Json['ID']
   name=req_Json['name']
   price=req_Json['price']
   image=req_Json['image']

   data = db.product.update_one({"_id":ObjectId(ID)}, 
   {   "$set": {"name":name, "price":price, "image":image }  } )

   return 'Product updated successfully.'

   
  
  

app.run(debug=True)