import wolframalpha
from tkinter import *
class WolframAlpha():
    

    def showPods(self):
        x = input('What is your question?')
        client = wolframalpha.Client('X969A9-QP6K293UUR')
        x = self.translate(x)
        res = client.query(x)

        for pod in res.pods:
            if pod.text:
                print(pod.text)
            elif pod.img:
                print(pod.img)
    def makeWindow(image):
        root = Tk()

        topFrame = Frame(root)
        topFrame.pack()

        bottomFrame = Frame(root)
        bottomFrame.pack(side=BOTTOM)
    def translate(self, String):
        if String[0:2] == "d:":
            return "derivative of"
        else:
            return String
app = WolframAlpha()
app.showPods()