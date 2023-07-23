import sys
from os import system, path, getcwd
from win32com.client import Dispatch
def create_shortcut(location, name):
    try:
        shortcut = Dispatch('WScript.Shell').CreateShortCut(path.join(location, name))
        shortcut.Targetpath = sys.argv[0]
        shortcut.WorkingDirectory = path.abspath(getcwd())
        shortcut.IconLocation = sys.argv[0]
        shortcut.save()
    except:
        return False
    return True

def create_sleep_list(sleep_data, days):
    try:
        sleep_list, c = [], True
        for i in days:
            for j in sleep_data:
                if i==j:
                    sleep_list.append(1)
                    c = False
            if c: sleep_list.append(0)
            else: c = True
    except:
        sleep_list = [0] * len(days)
    return sleep_list