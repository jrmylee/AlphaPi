import wolframalpha
from tkinter import *
from tkinter import ttk
import urllib.request
import base64
client = wolframalpha.Client('X969A9-QP6K293UUR')
root = Tk()

class WolframData():
    count = 1.0
    arrcount = 0
    def transmit(self, txtBox,frame):
        pos = txtBox.index("end-1c linestart")
        res = client.query(txtBox.get(pos+'',END))
        print(pos)
        if len(res.pods) > 0:
            for pod in res.pods:
                if pod.text:
                    txtBox.tag_configure('tag-right', justify='right')
                    txtBox.insert(END, '\n' + pod.text + '\n', 'tag-right')
                    txtBox.tag_configure('tag-left', justify='left')
                    self.count+=10.0
                    print(self.count)
                elif pod.img:
                    url = pod.img
                    response = urllib.request.urlopen(url)
                    data = response.read()
                    response.close()
                    b64_data = base64.encodebytes(data)
                    self.img = PhotoImage(data=b64_data)
                    label = Label(frame, image = self.img)
                    label.image = self.img
                    label.pack()


class WolframAlphaGUI(Frame):
    def main(self):
        data = WolframData
        nb = ttk.Notebook(root)
        page1 = ttk.Frame(nb)
        page2 = ttk.Frame(nb)
        scrollbar2 = Scrollbar(page1)
        scrollbar2.pack(side=RIGHT,fill=Y)

        Frame.__init__(self, page2)
        self.canvas = Canvas(page2, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(page2, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

        txtBox = Text(page1,wrap=WORD,yscrollcommand=scrollbar2.set)
        button = Button(page1, text="Ask!", command=lambda: data.transmit(data, txtBox,self.frame))

        nb.add(page1, text='Main')
        nb.add(page2, text='More Info')

        nb.grid(row=0)
        nb.grid(row=0, column=1)

        txtBox.pack()
        button.pack()
        root.mainloop()

    def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))



app = WolframAlphaGUI()
app.main()
