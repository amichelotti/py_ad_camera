import pvaccess
import time
print("ciao")

chan = pvaccess.Channel("13ARV1:Pva1:Image")

## function called each image update
def imageUpdate(x):
    ## replace with the code to display monochrome image
    print ("got array " +str(x) )


chan.subscribe('image',imageUpdate)
chan.setMonitorMaxQueueLength(3)

chan.startMonitor()

while True:
    time.sleep (1)
