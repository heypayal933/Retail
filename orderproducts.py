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
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['orderproducts']
  f=0;
  for x in collection.find({}):
   if(x["saleid"]==t1):
    f=1;
    break;
  if(f==0):
    insert1={'saleid':t1,'productid':t2,'quantity':t3,'price':t4,'discount':t5}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
  else:
    print("<script>alert('id already exist')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['orderproducts']
   collection.update_many({'saleid':t1},{'$set':{'productid':t2,'quantity':t3,'price':t4,'discount':t5}})
   print("<script>alert('Record Updated...')</script>")
 if(b1=="Delete"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['orderproducts']
  insert1={'saleid':t1}
  collection.delete_many(insert1)
  print("<script>alert('Record Deleted...')</script>")
 if(b1=="Allsearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['orderproducts']
   print("<body><input type=button value=Print onclick=window.print()></body>")
   print("<table border=1><tr><th>SaleID</th><th>ProductID</th><th>Quantity</th><th>Price</th><th>Discount</th></tr>")
   for x in collection.find({}):
     print("<tr><td>",x["saleid"],"</td><td>",x["productid"],"</td><td>",x["quantity"],"</td><td>",x["price"],"</td><td>",x["discount"],"</td></tr>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['orderproducts']
   print("<body><input type=button value=Print onclick=window.print()></body>")
   print("<table border=1><tr><th>SaleID</th><th>ProductID</th><th>Quantity</th><th>Price</th><th>Discount</th></tr>")
   for x in collection.find({'saleid':t1}):
     print("<tr><td>",x["saleid"],"</td><td>",x["productid"],"</td><td>",x["quantity"],"</td><td>",x["price"],"</td><td>",x["discount"],"</td></tr>")
except Exception:
 traceback.print_exc()
