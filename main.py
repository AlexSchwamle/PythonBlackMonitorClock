import tkinter as tk
from datetime import datetime

class FullscreenWindow:
    def __init__(self, root, screen_id, show_clock=False):
        self.root = root
        self.screen_id = screen_id
        self.show_clock = show_clock

        # Get screen width and height
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # Create a fullscreen window
        self.root.attributes('-fullscreen', True)
        self.root.configure(background='black')
        
        if self.show_clock:
            self.clock_label = tk.Label(self.root, font=('Helvetica', 48), fg='gray', bg='black')
            self.clock_label.pack(anchor='center')
            self.update_clock()

        # Bind double-click event to close the window
        self.root.bind('<Double-1>', self.close_window)
        
    def update_clock(self):
        now = datetime.now().strftime('%H:%M:%S')
        self.clock_label.config(text=now)
        self.root.after(1000, self.update_clock)

    def close_window(self, event):
        self.root.destroy()

def create_window(screen_id, show_clock=False):
    root = tk.Tk()
    app = FullscreenWindow(root, screen_id, show_clock)
    root.mainloop()

if __name__ == "__main__":
    # Create black screen on left monitor
    left_screen = tk.Tk()
    left_app = FullscreenWindow(left_screen, 1)
    
    # Create black screen on top monitor
    top_screen = tk.Tk()
    top_app = FullscreenWindow(top_screen, 2)
    
    # Create clock display on right monitor
    right_screen = tk.Tk()
    right_app = FullscreenWindow(right_screen, 3, show_clock=True)
    
    # Run all windows
    left_screen.mainloop()
    top_screen.mainloop()
    right_screen.mainloop()
