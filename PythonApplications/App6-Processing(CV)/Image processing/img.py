import cv2
import glob

images=glob.glob("*.jpg")
i=0
for img in images:
    img=cv2.imread(img,1)
    re=cv2.resize(img, (int(img.shape[0]/2), int(img.shape[1]/2)))
    cv2.imshow("Hey", re)
    cv2.waitKey(200)
    cv2.destroyAllWindows()
    cv2.imwrite("Resized"+images[i], re)
    i=i+1
