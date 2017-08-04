import MySQLdb
import time

while True:
    try:
        MySQLdb.connect(user="flask", passwd="pass", host="mysql")
        break
    except:
        print("can't connect mysql, I'm waiting for it to ready...")
        time.sleep(1)
