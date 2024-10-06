#!C:/Users/lenovo/AppData/Local/Programs/Python/Python312/python
print("Content-Type:text/html")
print()
import cgi
import traceback
from pymongo import MongoClient
import pymongo
f=cgi.FieldStorage()
t1=f.getvalue("t1")
t2=f.getvalue("t2")
t3=f.getvalue("t3")
t4=f.getvalue("t4")
t5=f.getvalue("t5")
t6=f.getvalue("t6")
b1=f.getvalue("b1")
try:
 if(b1=="New"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['orders']
  f=0;
  for x in collection.find({}):
   if(x["id"]==t1):
    f=1;
    break;
  if(f==0):
   print("Not welcome")
  else:
   print("Welcome")
 if(b1=="Save"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['orders']
  f=0;
  for x in collection.find({}):
   if(x["id"]==t1):
    f=1;
    break;
  if(f==0):
    insert1={'id':t1,'customerid':t2,'staffid':t3,'shipmentid':t4,'date':t5,'status':t6}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
  else:
    print("<script>alert('id already exist')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['orders']
   collection.update_many({'id':t1},{'$set':{'customerid':t2,'staffid':t3,'shipmentid':t4,'date':t5,'status':t6}})
   print("<script>alert('Record Updated...')</script>")
 if(b1=="Delete"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['orders']
  insert1={'id':t1}
  collection.delete_many(insert1)
  print("<script>alert('Record Deleted...')</script>")
 if(b1=="Allsearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['orders']
   print("<body><input type=button value=Print onclick=window.print()></body>")
   print("<table border=1><tr><th>ID</th><th>CustomerID</th><th>StaffID</th><th>ShipmentID</th><th>Date</th><th>Status</th></tr>")
   for x in collection.find({}):
     print("<tr><td>",x["id"],"</td><td>",x["customerid"],"</td><td>",x["staffid"],"</td><td>",x["shipmentid"],"</td><td>",x["date"],"</td><td>",x["status"],"</td></tr>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['orders']
   print("<body><input type=button value=Print onclick=window.print()></body>")
   print("<table border=1><tr><th>ID</th><th>CustomerID</th><th>StaffID</th><th>ShipmentID</th><th>Date</th><th>Status</th></tr>")
   for x in collection.find({'id':t1}):
     print("<tr><td>",x["id"],"</td><td>",x["customerid"],"</td><td>",x["staffid"],"</td><td>",x["shipmentid"],"</td><td>",x["date"],"</td><td>",x["status"],"</td></tr>")
except Exception:
 traceback.print_exc()