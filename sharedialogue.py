import tkinter
import os
import sharescraper

@echo_off

textvar='fine'

def spm():

    window = tkinter.Tk()
    window.title('SharePricer')

    lbl = tkinter.Label(window,text="Enter Ticker")
    lbl.grid(row=1,sticky='ew')#(side=L)
    
    global ent
    ent = tkinter.Entry(window,textvar='')
    ent.grid(row=2,column=0,sticky='e')#(side=L)

    global txt
    txt = tkinter.Label(window,text="$xx.xx")
    txt.grid(row=2,column=1,sticky='ew')
    
    btn=tkinter.Button(window,text="$",command=lambda:pricefind(textvar))
    btn.grid(row=3,sticky='ew')#(side=L)

    window.mainloop()
    pass

def pricefind(sel):
    e=ent.get()

    price=sharescraper.shareprice(e)

    txt.configure(text='$'+str(price))
        
    return



spm()





