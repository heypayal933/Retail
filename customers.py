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
t7=f.getvalue("t7")
t8=f.getvalue("t8")
t9=f.getvalue("t9")
t10=f.getvalue("t10")
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['customers']
  f=0;
  for x in collection.find({}):
   if(x["id"]==t1):
    f=1;
    break;
  if(f==0):
    insert1={'id':t1,'firstname':t2,'lastname':t3,'birthdate':t4,'phone':t5,'email':t6,'registrationdate':t7,'discountlevel':t8,'login':t9,'passwordhash':t10}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
  else:
    print("<script>alert('id already exist')</script>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['customers']
   collection.update_many({'id':t1},{'$set':{'firstname':t2,'lastname':t3,'birthdate':t4,'phone':t5,'email':t6,'registrationdate':t7,'discountlevel':t8,'login':t9,'passwordhash':t10}})
   print("<script>alert('Record Updated...')</script>")
 if(b1=="Delete"):
  client=pymongo.MongoClient("mongodb://localhost:27017/")
  db=client['retail']
  collection=db['customers']
  insert1={'id':t1}
  collection.delete_many(insert1)
  print("<script>alert('Record Deleted...')</script>")
 if(b1=="Allsearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['customers']
   print("<body><input type=button value=Print onclick=window.print()></body>")
   print("<table border=1><tr><th>ID</th><th>FirstName</th><th>LastName</th><th>BirthDate</th><th>Phone</th><th>Email</th><th>RegistrationDate</th><th>DiscountLevel</th><th>Login</th><th>PasswordHash</th></tr>")
   for x in collection.find({}):
     print("<tr><td>",x["id"],"</td><td>",x["firstname"],"</td><td>",x["lastname"],"</td><td>",x["birthdate"],"</td><td>",x["phone"],"</td><td>",x["email"],"</td><td>",x["registrationdate"],"</td><td>",x["discountlevel"],"</td><td>",x["login"],"</td><td>",x["passwordhash"],"</td></tr>")
 if(b1=="Psearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['retail']
   collection=db['customers']
   print("<body><input type=button value=Print onclick=window.print()></body>")
   print("<table border=1><tr><th>ID</th><th>FirstName</th><th>LastName</th><th>BirthDate</th><th>Phone</th><th>Email</th><th>RegistrationDate</th><th>DiscountLevel</th><th>Login</th><th>PasswordHash</th></tr>")
   for x in collection.find({'customerid':t1}):
     print("<tr><td>",x["id"],"</td><td>",x["firstname"],"</td><td>",x["lastname"],"</td><td>",x["birthdate"],"</td><td>",x["phone"],"</td><td>",x["email"],"</td><td>",x["registrationdate"],"</td><td>",x["discountlevel"],"</td><td>",x["login"],"</td><td>",x["passwordhash"],"</td></tr>")
except Exception:
 traceback.print_exc()










