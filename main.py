from Config import *

import tkinter as tk
from datetime import datetime

class FullscreenWindow:
    def __init__(self, root, x, y, show_clock=False):
        self.root = root
        self.show_clock = show_clock
        self.clock_update_id = None  # Track the after callback ID

        # Set window size and position
        self.root.geometry(f'+{x}+{y}')
        self.root.configure(background='black')
        
        if self.show_clock:
            # Create and place the clock label
            self.clock_label = tk.Label(self.root, font=('Helvetica', 48), fg='gray', bg='black')
            self.clock_label.place(relx=0.5, rely=0.5, anchor='center')
            self.update_clock()

        self.root.state("zoomed")

        # Bind double-click event to close the window
        self.root.bind('<Double-1>', self.close_window)

    def update_clock(self):
        now = datetime.now().strftime('%H:%M:%S')
        self.clock_label.config(text=now)
        self.clock_update_id = self.root.after(1000, self.update_clock)  # Schedule next update

    def close_window(self, event):
        if self.clock_update_id is not None:
            self.root.after_cancel(self.clock_update_id) # Cancel the scheduled callback
        self.root.destroy()

def create_window(offsets, show_clock=False):
    root = tk.Tk()
    app = FullscreenWindow(root, offsets[0], offsets[1], show_clock)
    root.update_idletasks()
    root.overrideredirect(True)
    return root

def close_all_windows(event=None):
    left_screen.quit() 
    top_screen.quit() 
    right_screen.quit() 

if __name__ == "__main__":
    # Create windows for all three monitors
    left_screen = create_window(left_screen_middle)
    top_screen = create_window(top_screen_middle)
    right_screen = create_window(right_screen_middle, show_clock=True)
    
    # Bind the Ctrl + W key combination to close_all_windows function
    left_screen.bind_all('<Control-w>', close_all_windows)
    top_screen.bind_all('<Control-w>', close_all_windows)
    right_screen.bind_all('<Control-w>', close_all_windows)

    # Run all windows
    def run_all():
        top_screen.mainloop()
        right_screen.mainloop()
    
    left_screen.after(0, run_all)
    left_screen.mainloop()
