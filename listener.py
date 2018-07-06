import serial
import time
import MySQLdb as db
import json
import decimal
import io
connect = db.connect(host='localhost', user='root',passwd='root', db='grow',charset='utf8')

def ReadSerial():
    ser = serial.Serial('/dev/ttyS2', 9600, timeout=1)
    sio = io.TextIOWrapper(io.BufferedRWPair(ser,ser))
    ser.isOpen()
    sio.flush()
    out = sio.readline()
    if out != '':
        print(out)
        data = json.loads(out)
        temp = data['Temperature']
        hydro = data['Hydro']
#        print(temp, hydro)
        try:
            with connect.cursor() as cursor:
                sql1 = "INSERT INTO `sensor_data` (`device_id`, `sensor_id`, `data`) values (1,1, %s)"
                cursor.execute(sql1, (temp, ))
                sql2= "INSERT INTO `sensor_data` (`device_id`, `sensor_id`, `data`) values (1,2, %s)"                
                cursor.execute(sql2, (hydro,))
            connect.commit()
        except:
            print("not add base")
while 1:
    ReadSerial()
#    time.sleep(4)
