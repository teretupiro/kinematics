from serial_example import *
from tkinter import *

def send_msg_b():
    if blue_var.get():
        send_msg('B')
    else:
        send_msg('b')

def send_msg_r():
    if red_var.get():
        send_msg('R')
    else:
        send_msg('r')

def send_msg_g():
    if green_var.get():
        send_msg('G')
    else:
        send_msg('g')


root=Tk()
root.geometry('300x300')


#red_button_on=Button(text='RED_ON',command=lambda:send_msg('R') )
#red_button_on.place(x=0,y=0)

#red_button_off=Button(text='RED_OFF',command=lambda:send_msg('r') )
#red_button_off.place(x=0,y=25)

#green_button_on=Button(text='GREEN_ON', command=lambda:send_msg_g)
#green_button_on.pack()

#green_button_off=Button(text='GREEN_OFF', command=lambda:send_msg_g)
#green_button_off.pack()


BLUE_button_on=Button(text='BLUE_ON',command=lambda:send_msg('1') )
BLUE_button_on.place(x=240,y=0)

BLUE_button_off=Button(text='BLUE_OFF',command=lambda:send_msg('2') )
BLUE_button_off.place(x=240,y=25)


RED_button_on=Button(text='RED_ON',command=lambda:send_msg('3') )
RED_button_on.place(x=0,y=0)

RED_button_off=Button(text='RED_OFF',command=lambda:send_msg('4') )
RED_button_off.place(x=0,y=25)

blue_var=BooleanVar()
blue_chnbutn=Checkbutton(text='BLUE', variable=blue_var, command=send_msg_b)
blue_chnbutn.pack()


red_var=BooleanVar()
red_chnbutn=Checkbutton(text='RED', variable=red_var, command=send_msg_r)
red_chnbutn.pack()


green_var=BooleanVar()
green_chnbutn=Checkbutton(text='GREEN', variable=green_var, command=send_msg_g)
green_chnbutn.pack()

root.mainloop()
