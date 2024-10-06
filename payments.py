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
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['payments']
  f=0;
  for x in collection.find({}):
   if(x["orderid"]==t1):
    f=1;
    break;
  if(f==0):
    insert1={'orderid':t1,'posid':t2,'invoiceno':t3,'paymentmode':t4}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
  else:
    print("<script>alert('id already exist')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['payments']
   collection.update_many({'orderid':t1},{'$set':{'posid':t2,'invoiceno':t3,'paymentmode':t4}})
   print("<script>alert('Record Updated...')</script>")
 if(b1=="Delete"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['payments']
  insert1={'orderid':t1}
  collection.delete_many(insert1)
  print("<script>alert('Record Deleted...')</script>")
 if(b1=="Allsearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['payments']
   print("<body><input type=button value=Print onclick=window.print()></body>")
   print("<table border=1><tr><th>OrderID</th><th>PosID</th><th>InvoiceNo</th><th>PaymentMode</th></tr>")
   for x in collection.find({}):
     print("<tr><td>",x["orderid"],"</td><td>",x["posid"],"</td><td>",x["invoiceno"],"</td><td>",x["paymentmode"],"</td></tr>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['payments']
   print("<body><input type=button value=Print onclick=window.print()></body>")
   print("<table border=1><tr><th>OrderID</th><th>PosID</th><th>InvoiceNo</th><th>PaymentMode</th></tr>")
   for x in collection.find({'orderid':t1}):
      print("<tr><td>",x["orderid"],"</td><td>",x["posid"],"</td><td>",x["invoiceno"],"</td><td>",x["paymentmode"],"</td></tr>")
except Exception:
 traceback.print_exc()