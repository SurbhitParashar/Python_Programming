import time
from plyer import notification
from datetime import datetime
# if __name__=="__main__":
while(True):
        
    notification.notify(
            title = "Drink Water!!!",
            message="Please drink water it has been 1hr",
            timeout=2) # displaying time
        
        # waiting time
    time.sleep(3600)
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(current_time)   
    dt_object = datetime.strptime(current_time, "%H:%M:%S")
    hour = dt_object.hour
    if hour>=14:
        break
