import serial
from tkinter import*

root=Tk()
root.geometry('300x300')

lbl=Label(text='',font='Arial 24')
lbl.pack()

port = 'COM5'

ser=serial.Serial(port=port,baudrate=57600)

def func():
    data = ser.readline()
    data = data.decode('utf-8')
    print('Light',data,end='')
    lbl.config(data)
    root.after(100,func)


root.mainloop()