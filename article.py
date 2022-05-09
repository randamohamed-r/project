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

#################################################################
@app.route('/article_title/<language>', methods = ['GET'])
def get_article_title(language):
  
  data = db.article
  if language == 'arabic' :
    for result in data.find({},{ 'englishTitle':0, 'articleInEnglish':0, 'articleInArabic':0}):
      list.append(result)
    print(list)
    return json.dumps(list, indent=4, default=json_util.default)
      
      #return json.dumps(result, indent=4, default=json_util.default)
  elif language == 'english':
    for result in data.find({},{ 'arabicTitle':0, 'articleInEnglish':0, 'articleInArabic':0}):
      list.append(result)
    print(list)
    return json.dumps(list, indent=4, default=json_util.default)
  
app.run(debug=True)

#####################################################################



