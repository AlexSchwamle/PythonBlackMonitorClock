from Config import *

import tkinter as tk
from pyautogui import press as pyautoguiPress
from pyautogui import position as pyautoguiPosition
from pyautogui import hotkey as pyautoguiHotkey
from screeninfo import get_monitors 
from datetime import datetime
from os import system, name
from time import sleep

RUNNING_WINDOWS = name == "nt"
ZERO_PAD_REMOVAL = "#" if RUNNING_WINDOWS else "-"

class FullscreenWindow:
    def __init__(self, root: tk.Tk, x, y, showClock=False):
        self.root = root
        self.showClock = showClock
        self.clockUpdateID = None  # Track the after callback ID

        # Set window size and position
        self.root.geometry(f"+{x}+{y}")
        self.root.configure(background="black")
        
        if self.showClock:
            # Create and place the clock label
            self.clockLabel = tk.Label(self.root, font=("Helvetica", 48), fg="gray10", bg="black")
            self.clockLabel.place(relx=0.5, rely=0.5, anchor="center")
            self.updateClock()

        self.allThreeMouseButtonsDown = {1: False, 2: False, 3: False}

        self.root.state("zoomed")

        # Per-window key binding funcs
        self.root.bind("<Double-1>", self.closeWindow)
        self.root.bind("<Control-n>", lambda e: system(CMD_TO_OPEN_BROWSER))
        self.root.bind("<Double-3>", self.openBrowser)
        self.root.bind("<ButtonRelease-2>", lambda e: pyautoguiPress("win"))
        self.root.bind("<Button-1>", self.setMouseStateDown)
        self.root.bind("<Button-2>", self.setMouseStateDown)
        self.root.bind("<Button-3>", self.setMouseStateDown)
        self.root.bind("<ButtonRelease-1>", self.setMouseStateUp)
        self.root.bind("<ButtonRelease-2>", self.setMouseStateUp)
        self.root.bind("<ButtonRelease-3>", self.setMouseStateUp)

    def updateClock(self):
        format = f"%{ZERO_PAD_REMOVAL}H:%M:%S" if CLOCK_24H else f"%{ZERO_PAD_REMOVAL}I:%M:%S %p"
        now = datetime.now().strftime(format)
        self.clockLabel.config(text=now)
        self.clockUpdateID = self.root.after(1000, self.updateClock)  # Schedule next update

    def closeWindow(self, event):
        if self.clockUpdateID is not None:
            self.root.after_cancel(self.clockUpdateID) # Cancel the scheduled callback
        self.root.destroy()

    def getMonitorTopLeftAtCoords(self, x, y):
        for monitor in get_monitors():
            if monitor.x <= x <= monitor.x + monitor.width and monitor.y <= y <= monitor.y + monitor.height:
                return monitor.x, monitor.y
        return x, y # Failsafe to given coords
    def getMonitorTopLeftAtMouse(self):
        curX, curY = pyautoguiPosition()
        return self.getMonitorTopLeftAtCoords(curX, curY)

    def openBrowser(self, event):
        system(CMD_TO_OPEN_BROWSER)
        if RUNNING_WINDOWS:
            from pygetwindow import getWindowsWithTitle
            from pygetwindow import Win32Window
            infLoopBreaker = 0
            while len(getWindowsWithTitle(NEW_TAB_TITLE)) == 0: 
                infLoopBreaker += 1
                if infLoopBreaker > 5 / 0.1: # 5 seconds 
                    return 
                sleep(0.1)
            newTabWindow: Win32Window = getWindowsWithTitle(NEW_TAB_TITLE)[0] 
            newTabWindow.restore()
            eventX, eventY = event.x_root, event.y_root
            topLeftX, topLeftY = self.getMonitorTopLeftAtCoords(eventX, eventY)
            newTabWindow.moveTo(topLeftX, topLeftY)
            newTabWindow.maximize()

    def _changeMouseDownState(self, button, state):
        self.allThreeMouseButtonsDown.update({button: state})
        if all(self.allThreeMouseButtonsDown.values()):
            pyautoguiHotkey("win", "alt", "s")
    def setMouseStateDown(self, event):
        button = event.num 
        self._changeMouseDownState(button, True)
    def setMouseStateUp(self, event):
        button = event.num 
        self._changeMouseDownState(button, False)
        
def createWindow(offsets, showClock=False):
    showClock = True if len(offsets) > 2 else False
    root = tk.Tk()
    app = FullscreenWindow(root, offsets[0], offsets[1], showClock)
    root.update_idletasks()
    root.overrideredirect(True)
    return root

def closeAllWindows(event=None):
    monitor1.quit() 
    monitor2.quit() 
    monitor3.quit() 

if __name__ == "__main__":
    if RUNNING_WINDOWS: # Minimizes the python cmd since it pops up above the clock when minimzing another window
        from pygetwindow import getWindowsWithTitle, Win32Window
        cmdWindow: Win32Window = getWindowsWithTitle("python.exe")[0]
        cmdWindow.minimize()

    # Create windows for all three monitors
    monitor1 = createWindow(MONITOR_1_POS)
    monitor2 = createWindow(MONITOR_2_POS)
    monitor3 = createWindow(MONITOR_3_POS)
    
    # Bind the Ctrl + W key combination to closeAllWindows function
    monitor1.bind_all("<Control-w>", closeAllWindows)
    monitor2.bind_all("<Control-w>", closeAllWindows)
    monitor3.bind_all("<Control-w>", closeAllWindows)

    # Run all windows
    def run_all():
        monitor2.mainloop()
        monitor3.mainloop()
    
    monitor1.after(0, run_all)
    monitor1.mainloop()
