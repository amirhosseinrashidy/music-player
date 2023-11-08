from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
root = Tk()
root.title('Dataflair python MP3 music player App')

mixer.init()

songs_list = Listbox(root , selectmode=SINGLE , bg="black" , fg="white" , font=
                     ('arial' ,15) , height=12 , width=47, selectbackground="gray" , selectforeground="black")
songs_list.grid(columnspan=9)
defined_font = font.Font(family='Helvetica')
play_button = Button(root , text="play" , width=7 ,  )
play_button['font']=defined_font
play_button.grid(row=1 , column=0)
pause_button = Button(root , text="pause" , width=7 , )
pause_button['font']= defined_font
pause_button.grid(row=1 , column=1)
mainloop()


