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
   collection=db['cart']
   f=0;
   '''Primary Key '''
   for x in collection.find({}):
    if(x["customerid"]==t1):
     f=1;
     break;
    
   '''Product id as foreign key '''
   collection=db['products']
   p=0;
   for x in collection.find({}):
    if(x["id"]==t2):
     p=1;
     break;
   if(f==0 and p==1):
    collection=db['cart']
    insert1={'customerid':t1,'productid':t2,'quantity':t3,'addedat':t4}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
   elif(f==1): 
    print("<script>alert('Customer id already exist')</script>")
   elif(p==0): 
    print("<script>alert('Product id must present in the product table')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['cart']
   collection.update_many({'customerid':t1},{'$set':{'productid':t2,'quantity':t3,'addedat':t4}})
   print("<script>alert('Record Updated...')</script>")
 if(b1=="Delete"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['cart']
  insert1={'customerid':t1}
  collection.delete_many(insert1)
  print("<script>alert('Record Deleted...')</script>")
 if(b1=="Allsearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['cart']
   print("<head><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css'></head><body><input type=button value=Print onclick=window.print()></body>")
   print("<table border=1 class='table'><tr><th>Customer ID</th><th>Product Id</th><th>Quantity</th><th>Added At</th></tr>")
   for x in collection.find({}):
     print("<tr class='success'><td class=active>",x["customerid"],"</td><td class=danger>",x["productid"],"</td><td class=info>",x["quantity"],"</td><td class=warning>",x["addedat"],"</td></tr>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['cart']
   print("<body><input type=button value=Print onclick=window.print()></body>")
   print("<table border=1><tr><th>Customer ID</th><th>Product Id</th><th>Quantity</th><th>Added At</th></tr>")
   for x in collection.find({'customerid':t1}):
     print("<tr><td>",x["customerid"],"</td><td>",x["productid"],"</td><td>",x["quantity"],"</td><td>",x["addedat"],"</td></tr>")
except Exception:
      traceback.print_exc()