import cv2
cap=cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap.set(3,640)#for width we use 3
cap.set(4,480)#for height we use 4
cap.set(10,70)#for brightness we use 10
count=0
Id=int(input('enter your id'))
while True:
    success,img=cap.read()
    #cv2.imshow("video",img)
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=detector.detectMultiScale(gray_img,1.3,7)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        count=count+1
        cv2.imwrite("dataset/user."+str(Id)+'.'+str(count)+".jpg",gray_img[y:y+h,x:x+w])
        cv2.imshow('frame',img)
    if cv2.waitKey(100)& 0xFF==ord('q'):
        break
    elif(count>30):
        break
cap.release()
cv2.destroyAllWindows()
