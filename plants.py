import pymongo
from pymongo import MongoClient
import json
from bson import ObjectId, json_util
from bson.json_util import dumps
from flask import Flask, render_template, jsonify , Response, request

list = [ ]
app=Flask(__name__)

try:
  client = MongoClient(host="localhost", port=27017)
  db = client.Agrosnap
  client.server_info()
except:
  print('ERROR')
##########################################################################################

@app.route('/getAllPlants', methods = ['GET'])
def viewAll():
    list=[]
    data = db.plants

    for result in data.find({},{ '_id':1 , 'name':1, 'image':1, 'sub_overview':1}):
      list.append(result)
    print(list)
    return json.dumps(list, indent=4, default=json_util.default)
##########################################################################################

@app.route('/plantById', methods = ['GET'])
def view():
    data = db.plants
    req_Json= request.json
    ID=req_Json['ID']
    result = data.find_one({'_id':ObjectId(ID)},{'_id':0, "sub_overview": 0})
    print(result)
    return json.dumps(result, indent=4, default=json_util.default)
##########################################################################################

@app.route('/search', methods = ['GET'])
def search_plant():
  req_Json= request.json
  plant_name=req_Json['plant_name']

  regex = ".*" + plant_name + ".*"

  for result in db.plants.find( {"name" : {'$regex' : regex, "$options":"i"}}, {"sub_overview": 0} ):
      list.append(result)
  print(list)
  return json.dumps(list, indent=4, default = json_util.default)

app.run(debug=True)