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



Id=input("Enter product ID: ")

storeName=input("Enter storeName: ")
phone_number=input("Enter phone number: ")
facebook_link=input("Enter Facebook Link: ")
another_link=input("Enter another link: ")
image=input("Enter image: ")
longtiude=input("Enter longtiude: ")
latitude=input("Enter latitude: ")


@app.route('/', methods =['GET','POST'])
def edit () :
   data = db.storeOwner.update_one({"_id":ObjectId(Id)}, 
   {   "$set": {"storeName":storeName, "contacts":{"phone_number":phone_number, "facebook_link":facebook_link, "another_link":another_link}, "location":{"longtiude":longtiude, "latitude":latitude} }  } )

   return 'Product updated successfully.'

   
  
  

app.run(debug=True)