import pymysql
import requests
import json

class Database:
    cur = None
    @staticmethod
    def intialize():
        connection = pymysql.connect("localhost", "brijesh", "", "Project")
        Database.cur = connection.cursor()

    @staticmethod
    def find(Stype , name):
        sql = "SELECT *FROM HAB where S_name='%s'" %(name)
        #print(sql)
        try:
            Database.cur.execute(sql)
            row = None
            for row in Database.cur:
                list(row)
            return row
        except pymysql.Error as err :
            return None

    @staticmethod
    def getNorad(Stype,name):
        sql = "SELECT S_nid FROM HAB where S_name='%s'" %(name)
        Database.cur.execute(sql);
        row = None
        for row in Database.cur:
            list(row)
        return row[0]

    @staticmethod
    def getdata(norad):
        request = requests.get("https://www.n2yo.com/rest/v1/satellite/positions/%s/25.9/81.95/0/1&apiKey=F8G5ZA-TPFZXA-8SX5GE-3Y23" %norad )
        content = json.loads(request.content);
        return content['positions']




