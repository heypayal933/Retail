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
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['stocks']
  f=0;
  for x in collection.find({}):
   if(x["storeid"]==t1):
    f=1;
    break;
  if(f==0):
    insert1={'storeid':t1,'productid':t2,'quantity':t3}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
  else:
    print("<script>alert('id already exist')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['stocks']
   collection.update_many({'storeid':t1},{'$set':{'productid':t2,'quantity':t3}})
   print("<script>alert('Record Updated...')</script>")
 if(b1=="Delete"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['stocks']
  insert1={'storeid':t1}
  collection.delete_many(insert1)
  print("<script>alert('Record Deleted...')</script>")
 if(b1=="Allsearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['stocks']
   print("<body><input type=button value=Print onclick=window.print()></body>")
   print("<table border=1><tr><th>StoreID</th><th>ProductID</th><th>Quantity</th></tr>")
   for x in collection.find({}):
     print("<tr><td>",x["storeid"],"</td><td>",x["productid"],"</td><td>",x["quantity"],"</td></tr>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['stocks']
   print("<body><input type=button value=Print onclick=window.print()></body>")
   print("<table border=1><tr><th>StoreID</th><th>ProductID</th><th>Quantity</th></tr>")
   for x in collection.find({'storeid':t1}):
     print("<tr><td>",x["storeid"],"</td><td>",x["productid"],"</td><td>",x["quantity"],"</td></tr>")
except Exception:
 traceback.print_exc()