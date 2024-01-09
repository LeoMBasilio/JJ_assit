import datetime

def writeLog(msg):
    with open('log.txt', 'a') as log:
        log.write(str(datetime.datetime.now()) + ': ' + msg + '\n')