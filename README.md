# Triple Monitor Black Background
Uses Python with TKinter to open a pure black background on a triple monitor setup with one monitor having a 24h clock showing `HH:MM:SS`. 

Hotkeys:
- If you double click any of the windows, it will close that singular window.
- If you press `Ctrl` + `W` on any of the three windows **3 times**, it will close all three windows immediately.
- If you press `Ctrl` + `N` it will open a new tab page in the browser set in `Config.py`. Can also run any arbitrary command if you really wanted to. Defaults to Brave.
    - If you double right click any window it will also open the browser.

## Installation
1. [Install Python](https://docs.anaconda.com/miniconda/)
2. Setup `Config.py` to have the approximate middle of your monitors for each one.
    - Adding `, True` to any or all of the monitors will show a clock on that monitor.
    - I just use ipython and run `from pyautogui import position` and then call `position()` to get the x and y coordinates. Could also run Windows Spy with AutoHotkey and use the `Screen` coordinates.
3. Run start.bat or use [my other repo of my various autohotkey scripts](https://github.com/AlexSchwamle/AutoHotkeyHotfixes) and press `Windows key` + `Shift` + `D` as a hotkey.