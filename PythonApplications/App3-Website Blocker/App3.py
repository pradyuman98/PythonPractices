import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com",  "www.instagram.com", "terna.org"]

while True:
   if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
       print("Working hrs. ")
       with open(hosts_path, 'r+') as f:
            content= f.read()
            for i in website_list:
               if i in content:
                   pass
               else: f.write("\n"+redirect+" "+ i+"\n")

   else:
       print("Be in working hrs. ")
       with open(hosts_path,'r+') as f:
             content=f.readlines()
             f.seek(0)
             for i in content:
                 if not any(j in i for j in website_list):
                    f.write(i)
             f.truncate()


   time.sleep(5)
