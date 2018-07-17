#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import mysql.connector

def read_file():
    coupons = []
    f = open("../static/coupons")
    while(1):
        line = f.readline()
        if not line:
            break
        coupons.append(line[:6])
    return coupons

def use_mysql(coupons):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "fight0315",
        database = "coupons"
    )

    mycursor = mydb.cursor(buffered=True) # buffered cursor is needed to avoid UNREAD error

    mycursor.execute("CREATE TABLE my_coupons (id INT, value VARCHAR(6))")

    mycursor.execute("SHOW TABLES")

    sql = "INSERT INTO my_coupons (id, value) VALUES (%s, %s)"

    for val in enumerate(coupons):
        #print(val)
        mycursor.execute(sql, val)
        mydb.commit()

    mycursor.execute("SELECT * FROM my_coupons")
    for x in mycursor:
        print(x)
    
    mycursor.close()
    mydb.close()

if __name__ == "__main__":
    coupons = read_file()
    #print(coupons)
    use_mysql(coupons)