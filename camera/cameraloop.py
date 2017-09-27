import os
import time

FRAMES = 1
TIMEBETWEEN = 60

frameCount = -1000
while frameCount < FRAMES:
    imageNumber = str(frameCount).zfill(7)
    os.system("raspistill -o image%s.jpg"%(imageNumber))
    frameCount += 1
    time.sleep(TIMEBETWEEN - 6) 
