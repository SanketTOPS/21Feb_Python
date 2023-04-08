import tkinter
from tkinter import DoubleVar, ttk, messagebox

screen=tkinter.Tk()
screen.geometry('400x600')
screen.title('FirstApp')
screen.config(bg='gold')

n = DoubleVar()

"""tkinter.Label(text='Firstname:').pack()
tkinter.Label(text='Lastname:').pack()"""

"""tkinter.Label(text='Firstname:',font='Bahnschrift 15 bold',bg='gold',fg='red').place(x=0,y=0)
tkinter.Label(text='Lastname:',font='Bahnschrift 15 bold',bg='gold',fg='red').place(x=0,y=30)"""

tkinter.Label(text='Firstname:',font='Bahnschrift 15 bold',bg='gold',fg='red').grid(row=0,column=0,sticky='W')
tkinter.Label(text='Lastname:',font='Bahnschrift 15 bold',bg='gold',fg='red').grid(row=1,column=0,sticky='W')

tkinter.Entry().grid(row=0,column=1,sticky='W')
tkinter.Entry().grid(row=1,column=1,sticky='W')

tkinter.Radiobutton(value=0, text='Male',font='Bahnschrift 15 bold',bg='gold',fg='red').grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(value=1, text='Female',font='Bahnschrift 15 bold',bg='gold',fg='red').grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text='Gujarati',font='Bahnschrift 15 bold',bg='gold',fg='red').grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text='Hindi',font='Bahnschrift 15 bold',bg='gold',fg='red').grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text='English',font='Bahnschrift 15 bold',bg='gold',fg='red').grid(row=5,column=0,sticky='W')

city=['Ahmedabad','Surat','Baroda','Rajkot','Jamnagar']
ttk.Combobox(values=city).grid(row=6,column=0)

tkinter.Scale(orient='horizontal',from_=0, to=500).grid(row=7,column=0)

def btnclick():
    #print("Button Clicked!")
    #messagebox.showerror("Error","Something went wrong...Try again!")
    #messagebox.showinfo("Success","Your data has been submitted!")
    #messagebox.showwarning("Warning","Your disk is full!")

    #messagebox.askokcancel("Success","Your data has been submitted!")
    #messagebox.askquestion("Download","Do you want to continue?")
    #messagebox.askretrycancel("Download","Do you want to continue?")
    #messagebox.askyesno("Download","Do you want to continue?")
    messagebox.askyesnocancel("Download","Do you want to continue?")

l2 = tkinter.Label().grid(row=8,column=0)

def show2():
    sel = "Vertical Scale Value = " + str(n.get()) 
    l2.config(text = sel, font =("Courier", 14))


tkinter.Button(command=show2,text='Submit',font='Bahnschrift 15 bold').place(x=160,y=250)
tkinter.mainloop()


