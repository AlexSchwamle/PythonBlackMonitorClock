# Triple Monitor Black Background
Uses Python with TKinter to open a pure black background on a triple monitor setup with one monitor having a 24h clock showing `HH:MM:SS`. 

Hotkeys:
- If you double click any of the windows, it will close that singular window.
- If you press `Ctrl` + `W` on any of the three windows **3 times**, it will close all three windows immediately.

## Installation
1. [Install Python](https://docs.anaconda.com/miniconda/)
2. Setup `Config.py` to have the approximate middle of your monitors for each one, setting right_screen_middle to the monitor you want the clock to be on. I just use ipython and call `import pyautogui` and `pyautogui.position()` to get the x and y coordinates. Could also run Windows Spy with AutoHotkey and use the `Screen` coordinates.
3. Run start.bat or use [my other repo of my various autohotkey scripts](https://github.com/AlexSchwamle/AutoHotkeyHotfixes) and press `Windows key` + `Shift` + `D` as a hotkey.