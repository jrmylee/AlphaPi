import wolframalpha
from tkinter import *
x = input('What is your question?')
client = wolframalpha.Client('X969A9-QP6K293UUR')
res = client.query(x)
for pod in res.pods:
    if type(pod) is img:
        im = Image.open(pod)
        im.show()
    elif type(pod) is text:
        print(pod)

        
