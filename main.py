from tkinter import *
from tkinter import messagebox
import customtkinter
import os


window = customtkinter.CTk()

#---LOGIC---#

running = False
minutes, seconds = 20, 0

def start() :
    global running
    if not running :
        update()
        running = True

def pause() :
    global running 
    if running :
        timer_label.after_cancel(update_time)   
        running = False

def reset() :
    global running
    if running :
        timer_label.after_cancel(update_time)
        running = False

    global minutes, seconds
    minutes, seconds = 20, 0
    timer_label.config(text='20:00')

def alert() :
    messagebox.showinfo(" ", "Check your posture")
    reset()
    

def test() :
    global running
    if running :
        timer_label.after_cancel(update_time)
        running = False

    global minutes, seconds
    minutes, seconds = 0, 5
    timer_label.config(text='00:05')

def update() :
    global minutes, seconds
    seconds -= 1
    if seconds == -1 :
        minutes -= 1
        seconds = 59

    if minutes == 0 and seconds == 0 :
        alert()


    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    timer_label.config(text=minutes_string + ':' + seconds_string)

    global update_time

    update_time = timer_label.after(1000, update)       

#---DESIGN---#

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

window.geometry("300x300")
window.resizable(False, False)
window.iconbitmap(bitmap=os.path.abspath("icon.ico"))
window.title("Posture Checker")

timer_label = customtkinter.CTkLabel(text='20:00', text_font=('Arial', 30), text_color=("white"), width = 100, height = 50)
timer_label.place(relx = 0.5, rely = 0.2, anchor=CENTER)

stopButton = customtkinter.CTkButton(window, text = "Play", width = 150, height = 50, command = start)
stopButton.place(relx=0.5, rely=0.5, anchor=CENTER)
repeatButton = customtkinter.CTkButton(window, text = "Pause", width = 150, height = 50, command = pause)
repeatButton.place(relx=0.5, rely=0.7, anchor=CENTER)
playButton = customtkinter.CTkButton(window, text = "Reset", width = 150, height = 50, command = reset)
playButton.place(relx = 0.5, rely = 0.9, anchor=CENTER)

window.mainloop()

