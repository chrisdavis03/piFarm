#!/home/chestnut/venv-piFarm/bin/python3

import schedule
from datetime import datetime, timedelta
import time
import db_conn
from actuators.gpio import lightPower, fanPower, psuPower
from sensors.lux import getLux
from sensors.tempHumidity import readDHT

def check_lights():
    currentTime = datetime.now().time()
    zone, startTime, endTime = db_conn.getzone1()

    startTime = datetime.strptime(startTime, '%H:%M:%S').time()
    endTime = datetime.strptime(endTime, '%H:%M:%S').time()

    if currentTime > startTime and currentTime < endTime:
        print('On')
        lightPower(True)
        fanPower(True)
    else:
        print('Off')
        lightPower(False)
        fanPower(False)

    print('Temperature:\t{}'.format(readDHT()))
    print('Lux:\t\t{}'.format(getLux()))

'''
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)
'''

schedule.every(1).seconds.do(check_lights)

def heartbeat():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    heartbeat()
