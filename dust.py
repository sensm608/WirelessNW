import serial
import requests, json
from influxdb import InfluxDBClient as influxdb

port = '/dev/ttyACM0'
brate = 9600
cmd = 'temp'

seri = serial.Serial(port, baudrate = brate, timeout = None)
print(seri.name)

seri.write(cmd.encode())


a=1
while a:
    if seri.in_waiting !=0 :
        content = seri.readline()
        nums = content[:-2].decode()[14:].strip()
        if nums.strip() is '':
            continue
        else:
            nums = float(nums)
        data = [{
            'measurement' : 'dustsDB',
            'tags':{
                'VisionUni':'2410',},
            'fields':{
                'num': nums,
            }
        }]
        print(nums)
        client = None

        try:
            client = influxdb('localhost', 8086, 'root', 'root', 'dustsDB')
        except Exception as e:
            print("Exception" + str(e))

        if client is not None:
            try:
                client.write_points(data)
            except Exception as e:
                print("Exception write " + str(e))
            finally:
                client.close()
        print("complete")
