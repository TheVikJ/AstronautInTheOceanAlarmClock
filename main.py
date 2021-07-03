import time
import webbrowser
import datetime

setalarm = input("Set an alarm: ")
aito1hour = "https://www.youtube.com/watch?v=AYVSFk1OAlw&ab_channel=NickKohler"

while True:
    if datetime.datetime.now().strftime('%H:%M') == setalarm:
        webbrowser.open(aito1hour, new=1)
        break
    else:
        time.sleep(30)
