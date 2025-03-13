from flask import Flask, request, jsonify
from flask_cors import CORS
import bestSchool 



app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/<int:a>/<int:b>/<int:c>/<int:d>/<int:e>/<float:f>/<float:g>', methods=['GET'])
def function(a =0 , b=0 , c=0  ,  d =0, e=0 , f =0 , g=0):
    school = bestSchool.bestSchool([[a,b,c,d,e,f,g]])
    return school
