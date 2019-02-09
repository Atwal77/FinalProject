import pymysql

#connection  = pymysql.connect("localhost" , "brijesh" , "" , "Satellites")

#cur = connection.cursor()
# CREATE TABLE Navigation
# (NORAD_ID varchar(20) ,
# NAME_OF_THE_SATELLITE varchar(20) ,
# LAUNCH_DATE varchar(20) , \
# LAUNCH_VECHICLE varchar(20) ,
# APPLICATION varchar(40) ,
# ORBIT_TYPE varchar(40) ,
# PAYLOAD float ,
# ALTITUDE float ,
# LONGITUDE float);

# for i in range(3):
#     norad = input("Enter the NORAD ID : ")
#     name = input("Enter the satellite name : ")
#     launch_date = input("Enter the launch date in dd:mm:yyyy format : ")
#     launch_vechicle = input("launch vechile : ")
#     application = input("enter the app : ")
#     orbit_type = input("orbit type : ")
#     payload = input("payload : ")
#     altitude = input("altitude : ")
#     longitude = input("longitude : ")
#
#     sql = "insert into Navigation (S_nid , Sname ,S_ld , S_lv , S_app , S_ot ,S_payl , S_alt, S_long) values ('%s' ,'%s' , '%s' ,'%s' , '%s' , '%s' ,%s,%s,%s )" %(norad , name , launch_date , launch_vechicle , application , orbit_type , payload , altitude , longitude)
#     cur.execute(sql)
#     connection.commit()

from database import Database

Database.intialize()

name = 'GSAT-8'
sql = "SELECT *FROM Navigation where Sname = '%s';" %name

Database.find("Navigation", "GSAT-8")
# print(type(cur))
# row = None
# for row in cur:
#     print(list(row))
# for i in range(len(row)):
#     print(row[i])

# Enter the NORAD ID : 43286
# Enter the satellite name : IRNS-1I
# Enter the launch date in dd:mm:yyyy format : 12:04:2018
# launch vechile : PSLV-C41/IRNSS-1I
# enter the app : Navigation
# orbit type : GSO
# payload : 1425
# altitude : NULL
# longitude : NULL