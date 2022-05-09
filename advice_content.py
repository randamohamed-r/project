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

##############################################################################
@app.route('/advice_content/<language>/<id>', methods =['GET'])
def get_advice (language, id) :
  data = db.advice

  if language == 'arabic':
    result = data.find_one({'_id':ObjectId(id)},{'_id':0, 'image':0, 'arabicTitle':0, 'englishTitle':0, 'adviceInEnglish':0})
    print(result)
    return json.dumps(result, indent=4, default = json_util.default)
  elif language == 'english':
    result = data.find_one({'_id':ObjectId(id)},{'_id':0, 'image':0, 'englishTitle':0, 'arabicTitle':0, 'adviceInArabic':0})
    print(result)
    return json.dumps(result, indent=4, default=json_util.default)

app.run(debug=True)
###############################################################################