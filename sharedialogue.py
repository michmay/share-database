import tkinter
import os
#import sharescraper.py


def spm():

    window = tkinter.Tk()
    window.title('SharePricer')

    lbl = tkinter.Label(window,text="Enter 3xyz")
    lbl.grid(row=0,sticky='ew')#(side=L)
    
    ent = tkinter.Entry(window)
    ent.grid(row=1,column=0,sticky='e')#(side=L)

    txt = tkinter.Label(window,text="$xx.xx")
    txt.grid(row=1,column=1,sticky='ew')
    
    btn=tkinter.Button(window,text="$",command=pricefind)
    btn.grid(row=2)#(side=L)

    window.mainloop()
    pass

def pricefind():
    
        
    pass



spm()




z = input()

g = sharescraper.shareprice('z')

print(g)
