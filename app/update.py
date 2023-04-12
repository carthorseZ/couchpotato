#!/usr/bin/env python3
from config import *
from time import sleep
#import seeed_dht
from datetime import datetime
from grove.gpio import GPIO
import pymysql
from groverelay import GroveRelay
import logging # flexible event logging

#setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'{LOGDIR}\{datetime.date(datetime.now())}log.txt'),
        logging.StreamHandler()
    ]
)

def main():
    #sensor = seeed_dht.DHT("11", 12)
    relay = GroveRelay(5)
   
 # Connect to the database.
    conn = pymysql.connect(db=DATABASE,
        user=USER,
        passwd=PASSWD,
        host=HOST)
    c = conn.cursor()
      
    while True:
        sleep(1)
        now = datetime.now()
        #humidity, temp = sensor.read()
        humidity = 20 #temporarily hard code values for testing
        temp = 20  #temporarily hard code values for testing

        c.execute(f"SELECT value from config where id='MorningStartTime';")
        data = c.fetchone()
        MorningStartTime = int(data[0])
        c.execute(f"SELECT value from config where id='MorningEndTime';")
        data = c.fetchone()
        MorningEndTime = int(data[0])
        c.execute(f"SELECT value from config where id='EveningStartTime';")
        data = c.fetchone()
        EveningStartTime = int(data[0])
        c.execute(f"SELECT value from config where id='EveningEndTime';")
        data = c.fetchone()
        EveningEndTime = int(data[0])
        c.execute(f"SELECT value from config where id='MorningTargetTemp';")  
        data = c.fetchone()
        MorningTargetTemp = int(data[0])
        c.execute(f"SELECT value from config where id='EveningTargetTemp';")
        data = c.fetchone()
        EveningTargetTemp = int(data[0])
        c.execute(f"SELECT value from config where id='MinTempThreshold';")
        data = c.fetchone()
        MinTempThreshold = int(data[0])
        c.execute(f"SELECT value from config where id='override';")
        data = c.fetchone()
        override = data[0]
      
        if (now.hour >= MorningStartTime and now.hour < MorningEndTime):
            mintemp = MorningTargetTemp
        elif (now.hour >= EveningStartTime and now.hour < EveningEndTime):
            mintemp = EveningTargetTemp
        else:
            mintemp = MinTempThreshold
        
        c.execute(f"UPDATE config set value='{mintemp}' where id='mintemp';")
        c.execute(f"UPDATE config set value='{temp}' where id='temp';")
        c.execute(f"UPDATE config set value='{humidity}' where id='humidity';")
        conn.commit()
        logging.info(f"temp {temp}{DEGREE_SIGN} mintemp {mintemp}{DEGREE_SIGN} humidity {humidity}%" )
   
main()