import requests
import json
from flask import Flask, render_template, request, session

from src.database import Database

app = Flask(__name__)

@app.before_first_request
def start():
    Database.intialize()

@app.route('/')
def hello():
    return render_template('map.html')

@app.route('/results' , methods = ['POST'])
def post_results():
    Stype = request.form['Stype']
    Sname = request.form['Sname']

    row = Database.find(Stype,Sname)
    if row is None :
        return render_template("Error.html")
    norad = Database.getNorad(Stype,Sname)
    print(norad)
    dynamicData = Database.getdata(norad)
    return render_template("results.html", data=row , content=dynamicData)


if __name__ == '__main__':
    app.run()

#base url =  https://www.n2yo.com/rest/v1/satellite/
#to get tle = /tle/{id}
#get satelite positions =  /positions/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{seconds}
#myapi = F8G5ZA-TPFZXA-8SX5GE-3Y23
#Name	Latitude	Longitude	Action	Selection
#Pratapgarh	25.9	81.95	    Remove	SELECTED

#
# request  = requests.get("https://www.n2yo.com/rest/v1/satellite/tle/25544&apiKey=F8G5ZA-TPFZXA-8SX5GE-3Y23")
# #print(request.content)
# content  = json.loads(request.content)
# print(content['info'])
# for k, v in content['info'].items():
#     print(k, v, sep=' ')
#
# request = requests.get("https://www.n2yo.com/rest/v1/satellite/positions/25544/25.9/81.95/0/1&apiKey=F8G5ZA-TPFZXA-8SX5GE-3Y23")
# content = json.loads(request.content);
# print((content['positions']))
# for v in content['positions']:
#    for key , val in v.items():
#        print(key , val , sep=' ')
