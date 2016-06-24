import wolframalpha
from tkinter import *
from PIL import ImageTk, Image
import urllib.request




client = wolframalpha.Client('X969A9-QP6K293UUR')
root = Tk()
txtBox = Text(root)
entry = Entry(root)


class WolframAlpha():

    def main(self):
        button = Button(root,text = "Get Rekt", command=self.transmit)
        labe = Label(root,text="Search", bg = "black", fg = "white")

        txtBox.grid(row=0)
        labe.grid(row = 1)
        entry.grid(row=1, column=1)
        button.grid(row=1, column=2)
        root.mainloop()


    def transmit(self):
        res = client.query(entry.get())
        if len(res.pods) > 0:
            for pod in res.pods:
                if pod.text:
                    txtBox.insert('1.0', pod.text + '\n')
                elif pod.img:
                    im = Image.open(urllib.request.urlopen(pod.img))

                    photo = PhotoImage(im)
                    label = Label(root, image = photo)
                    label.grid(row = 0, column = 1)
    def translate(self, String):
        if String[0:2] == "d:":
            return "ddx" + String[2:len(String)]
        else:
            return String

app = WolframAlpha()
app.main()
