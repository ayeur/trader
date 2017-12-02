from tkinter import *
from requests import *

r = get('https://api.coindesk.com/v1/bpi/currentprice.json', params=None)

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))


window = Tk()
window.title("Trader")
window.minsize(50,50)
T = Text(window, height=50, width=50)
T.pack()
T.insert(END, r.text)
center(window)
mainloop()


window.mainloop()