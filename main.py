from Config import *

import tkinter as tk
from datetime import datetime
from os import system

class FullscreenWindow:
    def __init__(self, root, x, y, showClock=False):
        self.root = root
        self.showClock = showClock
        self.clockUpdateID = None  # Track the after callback ID

        # Set window size and position
        self.root.geometry(f'+{x}+{y}')
        self.root.configure(background='black')
        
        if self.showClock:
            # Create and place the clock label
            self.clockLabel = tk.Label(self.root, font=('Helvetica', 48), fg='gray10', bg='black')
            self.clockLabel.place(relx=0.5, rely=0.5, anchor='center')
            self.updateClock()

        self.root.state("zoomed")

        # Bind double-click event to close the window
        self.root.bind('<Double-1>', self.closeWindow)
        self.root.bind("<Control-n>", lambda e: system(CMD_TO_OPEN_BROWSER))
        self.root.bind("<Double-3>", lambda e: system(CMD_TO_OPEN_BROWSER))

    def updateClock(self):
        now = datetime.now().strftime('%H:%M:%S')
        self.clockLabel.config(text=now)
        self.clockUpdateID = self.root.after(1000, self.updateClock)  # Schedule next update

    def closeWindow(self, event):
        if self.clockUpdateID is not None:
            self.root.after_cancel(self.clockUpdateID) # Cancel the scheduled callback
        self.root.destroy()

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
    # Create windows for all three monitors
    monitor1 = createWindow(MONITOR_1_POS)
    monitor2 = createWindow(MONITOR_2_POS)
    monitor3 = createWindow(MONITOR_3_POS)
    
    # Bind the Ctrl + W key combination to closeAllWindows function
    monitor1.bind_all('<Control-w>', closeAllWindows)
    monitor2.bind_all('<Control-w>', closeAllWindows)
    monitor3.bind_all('<Control-w>', closeAllWindows)

    # Run all windows
    def run_all():
        monitor2.mainloop()
        monitor3.mainloop()
    
    monitor1.after(0, run_all)
    monitor1.mainloop()
