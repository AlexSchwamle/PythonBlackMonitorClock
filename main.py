import tkinter as tk
from datetime import datetime

class FullscreenWindow:
    def __init__(self, root, x, y, width, height, show_clock=False):
        self.root = root
        self.show_clock = show_clock

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
        self.root.after(1000, self.update_clock)

    def close_window(self, event):
        self.root.destroy()

def create_window(x, y, width, height, show_clock=False):
    root = tk.Tk()
    app = FullscreenWindow(root, x, y, width, height, show_clock)
    root.update_idletasks()
    root.overrideredirect(True)
    return root

if __name__ == "__main__":
    # Adjust these values to your screen resolution
    screen_width = 1920  
    screen_height = 1080

    # Create windows for all three monitors
    left_screen = create_window(-1063, 505, screen_width, screen_height)
    top_screen = create_window(90, -559, screen_width, screen_height)
    right_screen = create_window(927, 523, screen_width, screen_height, show_clock=True)
    
    # Run all windows
    def run_all():
        top_screen.mainloop()
        right_screen.mainloop()
    
    left_screen.after(0, run_all)
    left_screen.mainloop()
