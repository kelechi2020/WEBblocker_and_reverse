import time
from datetime import datetime as dt
host_path='C:\\Windows\\System32\\Drivers\\etc\\hosts'
host_temp = r'C:\Users\KELECHI EGBOSI\PycharmProjects\WEB3.4\hosts'
redirect = "127.0.0.1"
website_list=["kickass.cr","onyeoma.com","https://www.youtube.com/","thepiratebay.org",
             "facebook.com","nairaland.com","www.nairaland.com","http://www.su-kam.com/load-chart.aspx",
              "https://web.facebook.com/","https://www.youtube.com" ,"www.saveyoutube.com","https://kat.cr","https://thepiratebay.se",
              "http://extratorrent.cc" ]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("working hours")
        with open(host_path, 'r+') as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:

        with open(host_path, 'r+') as file:

            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours")

    time.sleep(6)
