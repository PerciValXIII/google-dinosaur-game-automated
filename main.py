from PIL import Image, ImageGrab
import pyautogui
import time
import numpy as np


def hit(key):
    pyautogui.keyDown(key)


def isCollide(data):
    for i in range(200, 350):
        for j in range(645, 700):
            if(data[i, j] >= 172):
                return True

    return False


if __name__ == '__main__':

    print("Dino game about to start in 3 secs ....")
    time.sleep(3)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if(isCollide(data)):
            hit('up')

    # image.show()
