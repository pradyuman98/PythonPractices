import cv2, time, pandas
from datetime import datetime

f_frame=None
video=cv2.VideoCapture(0)
status_list=[None,None]
a=0
times=[]
df=pandas.DataFrame(columns=["Start", "End"])

while True:
    a=a+1
    status=0
    check, frame=video.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray1=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray, (15,15),0)

    if f_frame is None:
        f_frame=gray
        continue

    delta=cv2.absdiff(gray, f_frame)
    thresh=cv2.threshold(delta, 30,255, cv2.THRESH_BINARY)[1]
    thresh=cv2.dilate(thresh, None, iterations=2)

    cnts, heirarchy=cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i in cnts:
        if cv2.contourArea(i)<10000:
            continue
        status=1
        (a,b,c,d) = cv2.boundingRect(i)
        cv2.rectangle(frame, (a,b), (a+c, b+d), (0,255,0), 3)

    status_list.append(status)

    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())

    cv2.imshow("Capturing", frame)
    cv2.imshow("Delta", delta)
    cv2.imshow("ThreshHold", thresh)
    cv2.imshow("Gray", gray1)

    s=cv2.waitKey(50)
    if s==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

print(status_list)
print(a)
print(times)

for i in range(0, len(times),2):
    df=df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows()
