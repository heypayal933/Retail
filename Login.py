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
b1=f.getvalue("b1")
try:
 if(b1=="Login"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['Login']
  f=0;
  for x in collection.find({}):
   if(x["id"]==t1 and x["pwd"]==t2):
    f=1;
    break;
  if(f==0):
   print("<script>alert('Login Denied')</script>")
  else:
   print("<script>window.open('menu.html','_self')</script>")
 if(b1=="Register"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['Login']
  f=0;
  for x in collection.find({}):
   if(x["id"]==t1):
    f=1;
    break;
  if(f==0):
   collection=db['Login']
   insert1={'id':t1,'pwd':t2}
   collection.insert_one(insert1)
   print("<script>alert('Record Saved...')</script>")
  elif(f==1):
   print("<script>alert('Login id already exist')</script>")
except Exception:
   traceback.print_exc()