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

###############################################################################################
@app.route('/advice_titles', methods = ['GET'])
def get_advice_title():
  list = [ ]
  data = db.advice
  req_Json= request.json
  language=req_Json['language']

  if language == 'arabic' :
    for result in data.find({},{'arabicTitle':1}):
      list.append(result)
    print(list)
    return json.dumps(list, indent=4, default=json_util.default)
  elif language == 'english':
    for result in data.find({},{ 'englishTitle':1}):
      list.append(result)
    print(list)
    return json.dumps(list, indent=4, default=json_util.default)
###############################################################################################

@app.route('/adviceDetail', methods =['GET'])
def get_advice () :
  data = db.advice
  
  req_Json= request.json
  language=req_Json['language']
  ID=req_Json['ID']

  if language == 'arabic':
    result = data.find_one({'_id':ObjectId(ID)},{'_id':0, 'adviceInArabic':1})
    print(result)
    return json.dumps(result, indent=4, default = json_util.default)
  elif language == 'english':
    result = data.find_one({'_id':ObjectId(ID)},{'_id':0,  'adviceInEnglish':1})
    print(result)
    return json.dumps(result, indent=4, default=json_util.default)
###############################################################################################

@app.route('/article_titles', methods = ['GET'])
def get_article_title():
  list=[]
  data = db.article

  req_Json= request.json
  language=req_Json['language']

  if language == 'arabic' :
    for result in data.find({},{ 'arabicTitle':1}):
      list.append(result)
    print(list)
    return json.dumps(list, indent=4, default=json_util.default)
  elif language == 'english':
    for result in data.find({},{ 'englishTitle':1}):
      list.append(result)
    print(list)
    return json.dumps(list, indent=4, default=json_util.default)
###############################################################################################

@app.route('/articleDetail', methods =['GET'])
def get_article () :
  data = db.article

  req_Json= request.json
  language=req_Json['language']
  ID=req_Json['ID'] 

  if language == 'arabic':
    result = data.find_one({'_id':ObjectId(ID)},{'_id':0,'articleInArabic':1})
    print(result)
    return json.dumps(result, indent=4, default = json_util.default)
  elif language == 'english':
    result = data.find_one({'_id':ObjectId(ID)},{'_id':0, 'articleInEnglish':1})
    print(result)
    return json.dumps(result, indent=4, default=json_util.default)


app.run(debug=True)


