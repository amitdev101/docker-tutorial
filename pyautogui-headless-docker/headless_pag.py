from pyvirtualdisplay.display import Display
disp = Display(visible=True, size=(1366, 768), backend="xvfb", use_xauth=True)
disp.start()

import Xlib.display
import pyautogui
pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])