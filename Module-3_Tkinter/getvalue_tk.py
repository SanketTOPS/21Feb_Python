from tkinter import *
screen=Tk()


screen.geometry('400x600')
screen.title('FirstApp')
screen.config(bg='gold')

v2 = DoubleVar()
  
def show2():
      
    sel = "Vertical Scale Value = " + str(v2.get()) 
    l2.config(text = sel, font =("Courier", 14))
  
s2 = Scale(screen, variable = v2,
           from_ = 50, to = 1,
           orient = VERTICAL) 

  
b2 = Button(screen, text ="Display Vertical",
            command = show2,
            bg = "purple", 
            fg = "white")
  
l2 = Label(screen)
  
s2.pack(anchor = CENTER) 
b2.pack()
l2.pack()
  
screen.mainloop()