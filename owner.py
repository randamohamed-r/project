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

###########################################################################################
@app.route('/signup', methods =['POST' , 'GET'])
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
  
###########################################################################################
@app.route('/login', methods = ['GET','POST'])
def login():
    data = db.storeOwner
    req_Json= request.json
    email=req_Json['email']
    password=req_Json['password']
    result = data.find_one({'email':email , 'password':password},{})
    print(result)
    
    return json.dumps(result, indent=4, default = json_util.default)

###########################################################################################
@app.route('/edit', methods =['GET','POST'])
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

###########################################################################################
@app.route('/delete', methods = ['GET'])
def delete():
    req_Json= request.json
    Id=req_Json['Id']
    data = db.storeOwner.delete_one({'_id':ObjectId(Id)})

    return 'Account deleted successfully'
###########################################################################################

@app.route('/searchStore', methods = ['GET'])
def search_store():
  list=[]
  req_Json= request.json
  store_name=req_Json['store_name']

  regex = ".*" + store_name + ".*"

  for result in db.storeOwner.find( {"storeName" : {'$regex' : regex, "$options":"i"}},{"storeName":1, "image":1} ):
      list.append(result)
  print(list)
  return json.dumps(list, indent=4, default = json_util.default)
###########################################################################################

@app.route('/storeDetail', methods = ['GET'])
def view_store():
    list=[]
    data = db.storeOwner
    req_Json= request.json
    ID=req_Json['ID']
    result = data.find_one({'_id':ObjectId(ID)},{'_id':0,"email":0, "password":0})
    print(result)

    for result1 in db.product.find({"store_id":ObjectId(ID)},{"store_id":0}):
      list.append(result1)
    print(list)
    return json.dumps( (result,list) , indent=4, default=json_util.default)
###########################################################################################

@app.route('/getAllStores', methods = ['GET'])
def view():
    list=[]
    data = db.storeOwner

    for result in data.find({},{ 'email':0 , 'contacts':0, 'location':0, 'password':0, 'products':0}):
      list.append(result)
    print(list)
    return json.dumps(list, indent=4, default=json_util.default)

app.run(debug=True)