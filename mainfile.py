import pywhatkit
from datetime import datetime

now = datetime.now()
hour = int(now.strftime("%H"))
minu = int(now.strftime("%M"))
f = open("number_list.txt", "r")
for i in f:
    print(i)
    minu = minu + 1
    pywhatkit.sendwhatmsg(i,"Hy! This is Demo Message", hour, minu, 2)
    print("Message sent successfuly")
