from Config import *

import tkinter as tk
from pyautogui import press as pyautoguiPress
from pyautogui import position as pyautoguiPosition
from screeninfo import get_monitors 
from datetime import datetime
from os import system, name
from time import sleep

RUNNING_WINDOWS = name == "nt"
ZERO_PAD_REMOVAL = "#" if RUNNING_WINDOWS else "-"

if RUNNING_WINDOWS:
    from pygetwindow import getWindowsWithTitle
    from pygetwindow import Win32Window

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

        self.root.state("zoomed")

        # Per-window key binding funcs
        self.root.bind("<Double-1>", self.closeWindow)
        self.root.bind("<Control-n>", lambda e: system(CMD_TO_OPEN_BROWSER))
        self.root.bind("<Double-3>", self.openBrowser)
        self.root.bind("<Double-2>", lambda e: pyautoguiPress("win"))

    def updateClock(self):
        format = f"%{ZERO_PAD_REMOVAL}H:%M:%S" if CLOCK_24H else f"%{ZERO_PAD_REMOVAL}I:%M:%S %p"
        now = datetime.now().strftime(format)
        self.clockLabel.config(text=now)
        self.clockUpdateID = self.root.after(1000, self.updateClock)  # Schedule next update

    def closeWindow(self, event):
        if self.clockUpdateID is not None:
            self.root.after_cancel(self.clockUpdateID) # Cancel the scheduled callback
        self.root.destroy()

    def getMonitorTopLeftAtMouse(self):
        curX, curY = pyautoguiPosition()
        for monitor in get_monitors():
            if monitor.x <= curX <= monitor.x + monitor.width and monitor.y <= curY <= monitor.y + monitor.height:
                return monitor.x, monitor.y
        return curX, curY # Failsafe to current mouse position

    def openBrowser(self, event):
        system(CMD_TO_OPEN_BROWSER)
        if RUNNING_WINDOWS:
            infLoopBreaker = 0
            while len(getWindowsWithTitle(NEW_TAB_TITLE)) == 0: # type: ignore
                infLoopBreaker += 1
                if infLoopBreaker > 5 / 0.1: # 5 seconds 
                    return 
                sleep(0.1)
            newTabWindow: Win32Window = getWindowsWithTitle(NEW_TAB_TITLE)[0] # type: ignore (pylance not smart enough to see RUNNING_WINDOWS check)
            newTabWindow.restore()
            topLeftX, topLeftY = self.getMonitorTopLeftAtMouse()
            newTabWindow.moveTo(topLeftX, topLeftY)
            newTabWindow.maximize()
        
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
        from pyautogui import getActiveWindow # type: ignore (pyautogui stubs don't have windows functions)
        cmdWindow = getActiveWindow()
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
