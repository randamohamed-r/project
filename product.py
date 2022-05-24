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


#########################################################################################

@app.route('/add', methods =['POST'])
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

#########################################################################################

@app.route('/edit', methods =['GET','POST'])
def edit () :
   
   req_Json= request.json
   ID=req_Json['ID']
   name=req_Json['name']
   price=req_Json['price']
   image=req_Json['image']

   data = db.product.update_one({"_id":ObjectId(ID)}, 
   {   "$set": {"name":name, "price":price, "image":image }  } )

   return 'Product updated successfully.'

#########################################################################################

@app.route('/delete', methods = ['GET'])
def delete():
    req_Json= request.json
    ID=req_Json['ID']
    data = db.product.delete_one({'_id':ObjectId(ID)})
    return 'Product deleted successfully.'

#########################################################################################

@app.route('/viewAll', methods = ['GET'])
def view():
    list=[]
    req_Json= request.json
    ID=req_Json['ID']
    data = db.product

    for result in data.find({"store_id":ObjectId(ID)},{"store_id":0}):
      list.append(result)
    print(list)
    return json.dumps(list, indent=4, default=json_util.default)

app.run(debug=True)