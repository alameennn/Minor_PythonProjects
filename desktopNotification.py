from re import T
from winotify import Notification, audio
from plyer import notification
import time

while True:

    toast = Notification(app_id="IMPORTANT",
                         title="Message", msg="please drink water",
                         duration="short", icon="C:\water.jpeg")
    toast.set_audio(audio.LoopingAlarm, loop=False)

    toast.show()
    time.sleep(60)
time_hour = float(input("Set the hrs"))
while(True):
    time.sleep(2 * time_hour)
    notification.notify(
                        title="Water",
                        message = "drink water",
                        timeout=2
                        )