from pickle import GLOBAL
from tkinter import *
from math import cos,sin,pi
from tokenize import single_quoted
WIDTH=600
HEIGHT=500

A=[200,300]
B=[0,0]
C=[0,0]
D=[0,0]

AB=200
BC=150
CD=50


yBC_angle=20
xAB_angle=70
ABC_angle=-45
BCD_angle=45

root =Tk()
canvas=Canvas(width=WIDTH,height=HEIGHT,bg='black')
canvas.pack()


def draw(A,B,C,D):


#координаты точки B
    #cos (xAB/180 * P)+radius(AB(плечо)
    # -sin (xAB/180 * P)+radius(AB(плечо)
    B[0]=int(cos(xAB_angle/180*pi)* AB+A[0])
    B[1] = int(-sin(xAB_angle / 180 * pi) * AB + A[1])
#координаты точки C

    C[0]=int(cos(yBC_angle/180*pi)*BC+B[0])
    C[1]=int(sin(yBC_angle/180*pi)*BC+B[1])
    

    #координаты точки D
    D[0]=C[0]+CD
    D[1]=C[1]
    



    canvas.create_line(A,B,fill='red',width=5)
    canvas.create_line(B,C,fill='blue',width=3)
    canvas.create_line(C,D,fill='yellow',width=3)

    return (A,B,C,D)
A,B,C,D=draw(A,B,C,D)

def move_x(a):
    global A
    global B
    global C
    global D
    global xAB_angle
    global yBC_angle
    print('X',xAB_angle)
    canvas.delete('all')

    xAB_angle+=a
    yBC_angle+=a

    A, B, C, D = draw(A, B, C, D)


def move_y(a):
    global A
    global B
    global C
    global D
    global yBC_angle

    print('Y',yBC_angle)
    canvas.delete('all')


    yBC_angle+=a

    A, B, C, D = draw(A, B, C, D)

root.bind('<Left>',lambda event: move_x(1))
root.bind('<Right>',lambda event: move_x(-1))
root.bind('<Up>',lambda event: move_y(-1))
root.bind('<Down>',lambda event: move_y(1))

root.mainloop()