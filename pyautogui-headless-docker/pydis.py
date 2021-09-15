from pyvirtualdisplay import Display
import pyautogui as pg
import webbrowser
import time

def main():
    disp = Display()
    disp.start()
    # display is active
    disp.stop()
    # display is stopped

def main2():
    # disp =  Display(visible=True,backend="xvfb",size = (1024,768))
    disp =  Display(visible=True)
    disp.start()
    print(disp.is_alive())
    pg.screenshot("its_1.png")
    webbrowser.open_new("http://www.google.com")
    name = "its_"
    count = 2
    while(True):
        time.sleep(5)
        filename = name+str(count)+".png"
        count+=1
        pg.screenshot(filename)
        print("screenshot done ", filename)
    
    

    

main2()