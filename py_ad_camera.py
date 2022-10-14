import pvaccess
import time
import cv2
import numpy as np

name="13ARV1"

chan = pvaccess.Channel(name+":Pva1:Image")
sizex_chan= pvaccess.Channel(name+":cam1:SizeX")
sizey_chan= pvaccess.Channel(name+":cam1:SizeY")

sizex=sizex_chan.get()['value']
sizey=sizey_chan.get()['value']

print ("Image :"+str(sizex)+" x "+str(sizey))

## function called each image update
def imageUpdate(x):
   # print ("got array " +str(x['value']['ubyteValue']) )
    arr=pvaccess.NtNdArray(x)
    ts = arr.getDataTimeStamp()
    
    print ("TS:"+str(ts))

    im = arr.getValue()['ubyteValue'].reshape((sizey, sizex)) #notice row, column format
    ## replace with the code to display monochrome image
    cv2.imshow(name, im)
    cv2.waitKey(1)

chan.subscribe('image',imageUpdate)
chan.setMonitorMaxQueueLength(3)

chan.startMonitor()

while True:
    # cv2.waitKey()
    time.sleep (1)
