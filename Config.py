# Add the third `, True` to any monitor to show the clock on that monitor. You can display the clock on none or all 3 - it's modular! 
MONITOR_1_POS = -1461, 561, True
MONITOR_2_POS = 437, 237
MONITOR_3_POS = 2742, 506, True

# Make sure your browser's exe is in your path or you can specify the full path
CMD_TO_OPEN_BROWSER = "start brave.exe" 

# If True, finds the monitor the mouse is on and opens a maximized browser there. If False, it uses the default behavior of the operating system.
ALWAYS_OPEN_BROWSER_MAXIMIZED_TO_MONITOR_AT_MOUSE_POS = True 

# Due to how the browser window is moved, it resizes the window making it as small as possible. This fixes that and makes it so it's always this size in Width, Height format.
WINDOWED_BROWSER_SIZE = 1200, 800 

# This is the new tab title for the browser you open, it's used to find the window and maximize it on the same monitor you double right click
NEW_TAB_TITLE = "New Tab"

# Set the clock to 24h or 12h format - set to False or True
CLOCK_24H = False 

# This is a hotkey that happens when you press all 3 buttons on the mouse (left, right, middle). By default it turns off all monitors via my Autohotkey script.
KEYS_TO_PRESS_WHEN_ALL_MOUSE_BUTTONS_DOWN = ["win", "alt", "s"]