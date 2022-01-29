import cv2
import dropbox
import time
import random

startTime = time.time()
print(startTime)

def takeSnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while result:
        ret,frame = videoCaptureObject.read()
        image_name = "img"+str(number)+".png"
        cv2.imwrite(image_name, frame)
        startTime = time.time()
        result = False
    return image_name
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(image_name):
    accessToken = "********************************************************"
    file_from = image_name
    file_to = "/securitysystem/"+image_name
    dbx = dropbox.Dropbox(accessToken)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(), file_to)

while (True):
    if time.time()-startTime >= 5:
        name = takeSnapshot()
        uploadFile(name)
