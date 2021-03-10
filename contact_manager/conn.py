import pymysql as connector

myconnection = connector.connect(host='localhost', user='root', password='root', database='mydatabase')
def close():
    myconnection.close()