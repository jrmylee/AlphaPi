import wolframalpha
from tkinter import *
from tkinter import ttk
import urllib.request
import base64
client = wolframalpha.Client('X969A9-QP6K293UUR')
root = Tk()
from decimal import Decimal
class WolframData():

    def __init__(self):
        self.img = NONE

    def transmit(self, textbox, frame):

        pos = textbox.index("end-1c linestart")

        res = client.query(textbox.get(pos, END))
        if len(res.pods) > 0:
            for pod in res.pods:
                if pod.text:
                    textbox.tag_configure('tag-right', justify='right')
                    textbox.insert(END, '\n' + pod.text + '\n', 'tag-right')
                    textbox.tag_configure('tag-left', justify='left')
                elif pod.img:
                    url = pod.img
                    response = urllib.request.urlopen(url)
                    data = response.read()
                    response.close()
                    b64_data = base64.encodebytes(data)
                    self.img = PhotoImage(data=b64_data)
                    label = Label(frame, image=self.img)
                    label.image = self.img
                    label.pack()


class WolframAlphaGUI(Frame):

    def __init__(self):
        Frame.__init__(self)
        root.title("WolframPi")
        self.canvas = NONE
        self.frame = NONE
        self.vsb = NONE
        self.data = WolframData()
        self.nb = ttk.Notebook(root)
        self.page1 = ttk.Frame(self.nb)
        self.page2 = ttk.Frame(self.nb)
        scrollbar2 = Scrollbar(self.page1)
        scrollbar2.pack(side=RIGHT, fill=Y)
        self.textbox = Text(self.page1,wrap=WORD,yscrollcommand=scrollbar2.set)
        self.menubar = Menu(root)

        self.file = Menu(self.menubar, tearoff=0)
        self.file.add_command(label="Open", command=self.hello)

        self.edit = Menu(self.menubar, tearoff=0)
        self.edit.add_command(label="Copy", command=self.hello)
        self.edit.add_command(label="Paste",command=self.hello)

        self.functions = Menu(self.menubar, tearoff=0)
        self.functions.add_command(label="Graph", command=self.hello)

        self.menubar.add_cascade(label="File", menu=self.file)
        self.menubar.add_cascade(label="Edit", menu=self.edit)
        self.menubar.add_cascade(label="Functions", menu=self.functions)

    def main(self):

        self.canvas = Canvas(self.page2, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(self.page2, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",tags="self.frame")
        self.frame.bind("<Configure>", self.onframeconfigure)

        button = Button(self.page1, text="Ask!", command=lambda: self.data.transmit(self.textbox, self.frame))
        self.textbox.bind("<Key>", self.key)

        self.nb.add(self.page1, text='Main')
        self.nb.add(self.page2, text='More Info')

        self.nb.grid(row=0)
        self.nb.grid(row=0, column=1)

        self.textbox.pack()
        button.pack()
        root.config(menu=self.menubar)

        root.mainloop()

    def hello(self):
        print("hello")
    def key(self,event):
        if str(event.char) == '\r':
            self.data.transmit(self.textbox, self.frame)
    def onframeconfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))
    def onframeconfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
app = WolframAlphaGUI()
app.main()
