import wolframalpha
from tkinter import *

from PIL import Image, ImageTk

class WolframAlpha():
    

    def showPods(self):
        x = input('What is your question?')
        client = wolframalpha.Client('X969A9-QP6K293UUR')

        res = client.query(x)

        for pod in res.pods:
            if pod.text:
                print(pod.text)
            elif pod.img:
                print(pod.img)
    def makeWindow(image):
        root = Tk()
        img = ImageTk.PhotoImage(Image.open(image))
        theLabel = Label(root, text = "this is too easy")
        theLabel.pack()
        img.pack()
        root.mainloop()
app = WolframAlpha()
app.showPods()