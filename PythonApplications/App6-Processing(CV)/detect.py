from tkinter import *

def Detect():
    import capture

window=Tk()

window.wm_title("MotionDetector")
b1=Button(window, text="Detect", command=Detect)
b1.grid(row=1, column=2, columnspan=2)

b2=Button(window, text="Close", command=window.destroy)
b2.grid(row=2, column=2, columnspan=2)

window.mainloop()
