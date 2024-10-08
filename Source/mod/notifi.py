from win32api import GetModuleHandle, PostQuitMessage
from win32con import CW_USEDEFAULT, IDI_APPLICATION, IMAGE_ICON, LR_DEFAULTSIZE, LR_LOADFROMFILE, WM_DESTROY, WM_USER, WS_OVERLAPPED, WS_SYSMENU
from win32gui import Shell_NotifyIcon, UpdateWindow, WNDCLASS, RegisterClass, UnregisterClass, CreateWindow, DestroyWindow, LoadIcon, LoadImage, NIF_ICON, NIF_INFO, NIF_MESSAGE, NIF_TIP, NIM_ADD, NIM_DELETE, NIM_MODIFY
from playsound import playsound
from PIL import Image, ImageTk
from time import sleep
from tkinter import Tk, Canvas, Button, Label, Entry, CENTER, NW
from os import system
from threading import Thread
from . readed import open_un

def lang_focus():
    s, nlang = open_un()
    with open('qrc//additionals.txt', 'r', encoding='utf-8') as f:
        language = f.read().split('\\')
        language[0] = language[0].splitlines()
        language[1] = language[1].splitlines()
        language[1].pop(0)
    return s, nlang, language

s, nlang, language = lang_focus()
_is_running_ = False

class Notifi:
# Notifi().show_toast("Chuẩn bị nghỉ ngơi, nhớ save công việc lại nha <3")
    def __init__(self):
        self._thread = None
    def _show_toast(self, msg, duration=5):
        self.wc = WNDCLASS()
        self.hinst = self.wc.hInstance = GetModuleHandle(None)
        self.wc.lpszClassName = "EyeCare"
        self.wc.lpfnWndProc = {WM_DESTROY: self.on_destroy}
        try:
            self.classAtom = RegisterClass(self.wc)
            self.hwnd = CreateWindow(self.classAtom, "EyeCare", WS_OVERLAPPED | WS_SYSMENU, 0, 0, CW_USEDEFAULT, CW_USEDEFAULT, 0, 0, self.hinst, None)
            UpdateWindow(self.hwnd)
            hicon, flags = LoadImage(self.hinst, "logo.ico", IMAGE_ICON, 0, 0, LR_LOADFROMFILE | LR_DEFAULTSIZE) , (NIF_ICON | NIF_MESSAGE | NIF_TIP)
            nid = (self.hwnd, 0, flags, WM_USER + 20, hicon, "Tooltip")
            Shell_NotifyIcon(NIM_ADD, nid)
            Shell_NotifyIcon(NIM_MODIFY, (self.hwnd, 0, NIF_INFO, WM_USER + 20, hicon, "Balloon Tooltip", msg, 200, "EyeCare"))
            sleep(duration)
            DestroyWindow(self.hwnd)
            UnregisterClass(self.wc.lpszClassName, None)
        except:
            pass
    def show_toast(self, msg, duration=5):
        self._thread= Thread(target=self._show_toast, args=(msg, duration))
        self._thread.start()
    def on_destroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)

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

def focus(_type, _sound, _file: list, tim_wait, nlang):
    root = Tk()
    disable_fixed(root)
    
    if _type == 1:
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.overrideredirect(1)
        root.geometry("%dx%d+0+0" % (w, h))
        canvas = Canvas(root, width=w, height=h, bd=0, highlightthickness=0)
        canvas.pack()
        canvas.configure(background='black')
        
        try:
            # Load the image from the file
            imag = Image.open(_file[0])
        except:
            # Use a default image if the file is not found
            imag = Image.open("logo.ico")
        
        imgWidth, imgHeight = imag.size
        ratio = min(w / imgWidth, h / imgHeight)
        imgWidth, imgHeight = int(imgWidth * ratio), int(imgHeight * ratio)
        imag = imag.resize((imgWidth, imgHeight))
        
        # Store reference to the image to prevent garbage collection
        image = ImageTk.PhotoImage(imag)
        imagesprite = canvas.create_image(w / 2, h / 2, image=image)
        
        def unblock():
            if _sound == 1:
                playsound('sound//win.wav', block=False)
            canvas.create_window(100, 100, anchor=NW, window=Button(text=language[nlang][37], justify=CENTER, command=root.destroy, font="Helvetica 25 bold", bg="yellow"))

        # Keep a reference to the image to avoid it being garbage collected
        root.image = image

    else:
        root.configure(background='black')
        text = Label(root, text=None, justify=CENTER, font="Helvetica 25 bold", bg="lightblue")
        
        if _type == 2:
            text.configure(text=_file[1])
            text.pack()
        
        def unblock():
            if _sound == 1:
                playsound('sound//win.wav', block=False)
            text.configure(text=language[nlang][36])
            text.pack()
            Button(root, text=language[nlang][37], justify=CENTER, command=root.destroy, font="Helvetica 15 bold", bg="yellow").pack()
    
    root.after(tim_wait, unblock)
    root.mainloop()


def lock_lock(_pass, nlang):
    global _is_running_
    if _is_running_:
        return
    _is_running_ = True
    root = Tk()
    disable_fixed(root)
    root.configure(background='black')
    text = Label(root, text=language[nlang][38], justify=CENTER, font="Helvetica 25 bold", bg="lightblue")
    def pass_check(e=None):
        if widget.get()==_pass:
            global _is_running_
            _is_running_ = False
            root.destroy()
        else: text.configure(text=language[nlang][39], bg="red")
    widget = Entry(root, show="*", font="Helvetica 25 bold", width=25, justify=CENTER)
    text.pack()
    widget.bind('<Return>', pass_check)
    widget.pack()
    Button(root, text ="Okela", justify=CENTER, command = pass_check, font="Helvetica 16 bold", bg="yellow").pack()
    root.mainloop()

def sleep_lock(sound_on, pass_on, _pass, nlang):
    root = Tk()
    disable_fixed(root)
    root.configure(background='black')
    def shutdown_run():
        system('shutdown /s /t 2')
        system('taskkill /F /FI "STATUS eq RUNNING"')
    root.after(40000, shutdown_run)
    if sound_on:
        playsound('sound//lullaby.wav', block=False)

    Label(root, text=language[nlang][40], justify=CENTER, font="Helvetica 25 bold", bg="lightblue").pack()
    if pass_on:
        text = Label(root, text=language[nlang][41], justify=CENTER, font="Helvetica 15 bold", bg="pink")
        text.pack()
        def pass_check(e=None):
            if widget.get()==_pass:
                root.destroy()
            else: text.configure(text=language[nlang][39], bg="red")
        widget = Entry(root, show="*", font="Helvetica 25 bold", width=25, justify=CENTER)
        widget.bind('<Return>', pass_check)
        widget.pack()
    Button(root, text ="Turn off now", justify=CENTER, command = shutdown_run, font="Helvetica 16 bold", bg="yellow").pack()
    root.mainloop()