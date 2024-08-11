from tkinter import *
 
# don't forget to change the serial port to suit

 
def move_servo(a):
    print(a)
 
# set up GUI
root = Tk()
 
# draw a nice big slider for servo position
scale = Scale(root,
    command = move_servo,
    to = 175,
    orient = HORIZONTAL,
    length = 400,
    label = 'Angle')
scale.pack(anchor = CENTER)
 
# run Tk event loop
root.mainloop()