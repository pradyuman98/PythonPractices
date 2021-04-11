import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("ultimater.jpg")
gray=cv2.imread("ultimater.jpg",0)

faces=face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

for a,b,c,d in faces:
    img=cv2.rectangle(img, (a,b),(a+c, b+d), (0,0,255), 3)

re=cv2.resize(img,(1000,800))
cv2.imshow("Faces", re)
cv2.waitKey(0)
cv2.destroyAllWindows()
