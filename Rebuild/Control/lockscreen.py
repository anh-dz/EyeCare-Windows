from playsound import playsound
from PIL import Image, ImageTk
from time import sleep
from tkinter import Tk, Canvas, Button, Label, Entry, CENTER, NW
from os import system
from threading import Thread

def fade(root):
    root.attributes("-alpha", 0.1)
    sleep(0.01)
    root.attributes("-alpha", 0.2)
    sleep(0.01)
    root.attributes("-alpha", 0.3)
    sleep(0.01)
    root.attributes("-alpha", 0.4)
    sleep(0.01)
    root.attributes("-alpha", 0.5)
    sleep(0.01)
    root.attributes("-alpha", 0.6)
    sleep(0.01)
    root.attributes("-alpha", 0.7)
    sleep(0.01)
    root.attributes("-alpha", 0.8)
    sleep(0.01)
    root.attributes("-alpha", 0.9)
    sleep(0.01)
    root.attributes("-alpha", 1)

def disable_fixed(root):
    def do_exit():
        global pressed_f4
        pressed_f4 = False
    root.bind('<Alt-F4>')
    root.protocol("WM_DELETE_WINDOW",do_exit)
    root.attributes("-fullscreen", True, "-alpha", 0)
    root.wm_attributes("-topmost", 1)
    Thread(target= lambda: fade(root)).start()

def focus(_type, _sound, _file :list, tim_wait):
    root = Tk()
    disable_fixed(root)
    if _type == 1:
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.overrideredirect(1)
        root.geometry("%dx%d+0+0" % (w, h))
        canvas = Canvas(root,width=w,height=h,bd=0,highlightthickness=0)
        canvas.pack()
        canvas.configure(background='black')
        try: imag = Image.open(_file[0])
        except: imag = Image.open("logo.ico")
        imgWidth, imgHeight = imag.size
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth, imgHeight = int(imgWidth*ratio), int(imgHeight*ratio)
        imag = imag.resize((imgWidth,imgHeight), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(imag)
        imagesprite = canvas.create_image(w/2,h/2,image=image)
        def unblock():
            if _sound == 1:
                playsound('sound//win.wav', block=False)
            canvas.create_window(100, 100, anchor=NW, window=Button(text = "Trở lại làm việc", justify=CENTER, command = root.destroy, font="Helvetica 25 bold", bg="yellow"))
    else:
        root.configure(background='black')
        text = Label(root, text=None, justify=CENTER, font="Helvetica 25 bold", bg="lightblue")
        if _type == 2:
            text.configure(text = _file[1])
            text.pack()
        def unblock():
            if _sound == 1:
                playsound('sound//win.wav', block=False)
            text.configure(text = "Giải lao xong")
            text.pack()
            Button(root, text ="Trở lại làm việc", justify=CENTER, command = root.destroy, font="Helvetica 15 bold", bg="yellow").pack()
    root.after(tim_wait, unblock)
    root.mainloop()

_is_running_ = False
def lock_lock(_pass: str):
    global _is_running_
    if _is_running_:
        return
    _is_running_ = True
    root = Tk()
    disable_fixed(root)
    root.configure(background='black')
    text = Label(root, text="Nhập mật khẩu", justify=CENTER, font="Helvetica 25 bold", bg="lightblue")
    def pass_check(e=None):
        if widget.get()==_pass:
            global _is_running_
            _is_running_ = False
            root.destroy()
        else: text.configure(text="Sai mật khẩu")
    widget = Entry(root, show="*", font="Helvetica 25 bold", width=25, justify=CENTER)
    text.pack()
    widget.bind('<Return>', pass_check)
    widget.pack()
    Button(root, text ="Okela", justify=CENTER, command = pass_check, font="Helvetica 16 bold", bg="yellow").pack()
    root.mainloop()

def sleep_lock(sound_on, pass_on, _pass: str):
    root = Tk()
    disable_fixed(root)
    root.configure(background='black')
    def shutdown_run():
        system("shutdown /s /t 0")
    root.after(40000, shutdown_run)
    if sound_on:
        playsound('sound//lullaby.wav', block=False)

    Label(root, text="Đã đến giờ đi ngủ! Tắt máy tự động sau 40s", justify=CENTER, font="Helvetica 25 bold", bg="lightblue").pack()
    if pass_on:
        text = Label(root, text="Nhập mật khẩu, nhấn enter để hủy bỏ tự động tắt máy", justify=CENTER, font="Helvetica 15 bold", bg="pink")
        text.pack()
        def pass_check(e=None):
            if widget.get()==_pass:
                root.destroy()
            else: text.configure(text="Sai mật khẩu")
        widget = Entry(root, show="*", font="Helvetica 25 bold", width=25, justify=CENTER)
        widget.bind('<Return>', pass_check)
        widget.pack()
    Button(root, text ="Tắt máy luôn", justify=CENTER, command = lambda: system("shutdown /s /t 0"), font="Helvetica 16 bold", bg="yellow").pack()
    root.mainloop()