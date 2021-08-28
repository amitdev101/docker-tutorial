# import pyautogui
import shellit
import random, os, time

# os.environ['DISPLAY'] = ':0'


def random_number():
        num = random.randint(0,100)
        print("Hello i will call random number : ",num)

def main():
    random_number()
    while True:
        time.sleep(10)

if __name__=='__main__':
    main()