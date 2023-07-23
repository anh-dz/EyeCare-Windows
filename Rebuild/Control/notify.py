from win32api import GetModuleHandle, PostQuitMessage
from win32con import CW_USEDEFAULT, IDI_APPLICATION, IMAGE_ICON, LR_DEFAULTSIZE, LR_LOADFROMFILE, WM_DESTROY, WM_USER, WS_OVERLAPPED, WS_SYSMENU
from win32gui import Shell_NotifyIcon, UpdateWindow, WNDCLASS, RegisterClass, UnregisterClass, CreateWindow, DestroyWindow, LoadIcon, LoadImage, NIF_ICON, NIF_INFO, NIF_MESSAGE, NIF_TIP, NIM_ADD, NIM_DELETE, NIM_MODIFY
from threading import Thread
from time import sleep

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
        """

        :rtype: object
        """
        self._thread= Thread(target=self._show_toast, args=(msg, duration))
        self._thread.start()
    def on_destroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)