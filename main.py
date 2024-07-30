#1807
import cv2
import numpy as np
import pyautogui
import time
from PIL import ImageGrab
from pynput import keyboard
import pygame


# Флаг для отслеживания состояния
active = False



pygame.mixer.init()


def locate_image_on_screen(template_path):
    # Снимок экрана
    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    # Шаблон изображения
    template = cv2.imread(template_path, 0)
    w, h = template.shape[::-1]

    # Поиск шаблона на экране
    res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.93

    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        return (pt[0] + w / 2, pt[1] + h / 2)
    return None


def click_on_image(image_path):
    location = locate_image_on_screen(image_path)
    if location:
        pyautogui.click(location)


def scenario1():
    time.sleep(1)
    click_on_image('visitsites.png')
    time.sleep(1)
    visitsiteswait = locate_image_on_screen('visitsiteswait.png')
    while visitsiteswait:
        time.sleep(0.2)
        visitsiteswait = locate_image_on_screen('visitsiteswait.png')
    if locate_image_on_screen('ohnosites.png'):
        click_on_image('back.png')
        backwait = locate_image_on_screen('backwait.png')
        while backwait:
            time.sleep(0.5)
            backwait = locate_image_on_screen('backwait.png')
        print("переход к следующему сценарию.")
        return
    time.sleep(3)
    click_on_image('gotosite.png')
    time.sleep(1)
    click_on_image('open.png')
    time.sleep(3)
    if locate_image_on_screen('stay30sec.png'):
        time.sleep(33)
    if locate_image_on_screen('stay60sec.png'):
        time.sleep(63)
    if locate_image_on_screen('stay90sec.png'):
        time.sleep(93)
    if locate_image_on_screen('stay120sec.png'):
        time.sleep(123)
    # pyautogui.hotkey('alt', 'tab')
    # pyautogui.click(270, 1060, button='left')
    if locate_image_on_screen('visitsitestrap.png'):
        click_on_image('visitsitestrap.png')
        time.sleep(1)
        if locate_image_on_screen('closeanyway.png'):
            click_on_image('closeanyway.png')
    if locate_image_on_screen('tgtray.png'):
        click_on_image('tgtray.png')
    else:
        click_on_image('tgtray2.png')
        time.sleep(1)
        click_on_image('skip.png')
    #else:
       # pyautogui.click(270, 1060, button='left')
        #click_on_image('skip.png')
    time.sleep(3)

    if not(locate_image_on_screen('clickbeeisopen.png')):
        click_on_image('clickbee.png')
    if locate_image_on_screen('congratulations.png'):
        pygame.mixer.music.load('beep.wav')
        pygame.mixer.music.play()

    if locate_image_on_screen('ohnosites.png'):
        click_on_image('back.png')

def scenario2():
    # Добавьте реализацию второго сценария здесь
    time.sleep(1)
    click_on_image('joinchannels.png')
    time.sleep(2)
    joinchannelswait = locate_image_on_screen('joinchannelswait.png')
    while joinchannelswait:
        time.sleep(0.2)
        joinchannelswait = locate_image_on_screen('joinchannelswait.png')
    if locate_image_on_screen('ohnochannels.png'):
        print("переход к следующему сценарию.")
        click_on_image('back.png')
        backwait = locate_image_on_screen('backwait.png')
        while backwait:
            time.sleep(0.5)
            backwait = locate_image_on_screen('backwait.png')
        return
    time.sleep(1)
    if locate_image_on_screen('jointhechannel.png'):
        click_on_image('jointhechannel.png')
    time.sleep(1)
    if locate_image_on_screen('isexpired.png'):
        click_on_image('ok.png')
        time.sleep(1)
        click_on_image('skip.png')
        return
    if locate_image_on_screen('requesttojoin.png'):
        click_on_image('requesttojoin.png')
        time.sleep(1)
        click_on_image('joined.png')
    if locate_image_on_screen('joinchannel.png'):
        click_on_image('joinchannel.png')
    if locate_image_on_screen('alreadyjoined.png'):
        click_on_image('clickbee.png')
        time.sleep(1)
        click_on_image('joined.png')
    if locate_image_on_screen('joingroup.png'):
        click_on_image('joingroup.png')
    time.sleep(0.3)
    if locate_image_on_screen('mute.png'):
        click_on_image('mute.png')
        time.sleep(0.3)
    click_on_image('clickbee.png')
    time.sleep(1)
    click_on_image('joined.png')
    time.sleep(1)
    if locate_image_on_screen('congratulations.png'):
        pygame.mixer.music.load('beep.wav')
        pygame.mixer.music.play()




def scenario3():
    # Добавьте реализацию третьего сценария здесь
    time.sleep(1)
    click_on_image('back.png')

    time.sleep(1)
    click_on_image('joinbots.png')
    time.sleep(1)
    joinbotswait = locate_image_on_screen('joinbotswait.png')
    while joinbotswait:
        time.sleep(0.2)
        joinbotswait = locate_image_on_screen('joinbotswait.png')
    if locate_image_on_screen('ohnobots.png'):

        click_on_image('back.png')
        backwait = locate_image_on_screen('backwait.png')
        while backwait:
            time.sleep(0.5)
            backwait = locate_image_on_screen('backwait.png')
        return

    time.sleep(2)
    click_on_image('startthebot.png')
    time.sleep(1)
    if locate_image_on_screen('joinchannel.png') or locate_image_on_screen('videochat.png'):
        click_on_image('clickbee.png')
        time.sleep(1)
        click_on_image('skip.png')
        return
    if locate_image_on_screen('unmute.png'):
        click_on_image('clickbee.png')
        time.sleep(1)
        click_on_image('skip.png')
        time.sleep(1)
        if locate_image_on_screen('skipohno.png'):
            click_on_image('back.png')
            backwait = locate_image_on_screen('backwait.png')
            while backwait:
                time.sleep(0.5)
                backwait = locate_image_on_screen('backwait.png')
        return
    if locate_image_on_screen('ok.png'):
        click_on_image('ok.png')
        time.sleep(1)
        click_on_image('3dots.png')
        click_on_image('3dots2.png')
        time.sleep(1)
        click_on_image('openbot.png')
        time.sleep(1)

    time.sleep(1)
    location = locate_image_on_screen('botrespond.png')
    location3 = locate_image_on_screen('botrespond3.png')
    if location:
        x, y = location
        pyautogui.click(x + 50, y, button='right')
        time.sleep(1)
        click_on_image('forward.png')
        time.sleep(1)
        click_on_image('clickbee2.png')
        time.sleep(1)
        click_on_image('started.png')
        time.sleep(3)
        pyautogui.press('enter')
    elif location3:
        x, y = location3
        pyautogui.click(x, y + 60, button='right')
        time.sleep(1)
        click_on_image('forward.png')
        time.sleep(1)
        click_on_image('clickbee2.png')
        time.sleep(1)
        click_on_image('started.png')
        time.sleep(1)
        pyautogui.press('enter')

    if locate_image_on_screen('start.png'):
        click_on_image('start.png')
        time.sleep(5)
    if locate_image_on_screen('youallowed.png'):
        click_on_image('writeamessage.png')
        pyautogui.typewrite('/start')
        time.sleep(0.5)  # Небольшая пауза перед нажатием Enter
        pyautogui.press('enter')
        time.sleep(5)

    location = locate_image_on_screen('botrespond.png')
    location3 = locate_image_on_screen('botrespond3.png')
    if location:
        x, y = location
        pyautogui.click(x + 50, y, button='right')
        time.sleep(1)
        click_on_image('forward.png')
        time.sleep(1)
        click_on_image('clickbee2.png')
        time.sleep(1)
        click_on_image('started.png')
        time.sleep(2)
        pyautogui.press('enter')
    elif location3:
        x, y = location3
        pyautogui.click(x, y + 60, button='right')
        time.sleep(1)
        click_on_image('forward.png')
        time.sleep(1)
        click_on_image('clickbee2.png')
        time.sleep(1)
        click_on_image('started.png')
        time.sleep(1)
        pyautogui.press('enter')

    if locate_image_on_screen('norespond.png') or locate_image_on_screen('norespond2.png'):
        click_on_image('clickbee.png')
        time.sleep(1)
        click_on_image('skip.png')
        time.sleep(2)
        if locate_image_on_screen('skipohno.png'):
            click_on_image('back.png')
            backwait = locate_image_on_screen('backwait.png')
            while backwait:
                time.sleep(0.5)
                backwait = locate_image_on_screen('backwait.png')
        return
    else:
        #pyautogui.click(790, 900, button='right')
        time.sleep(1)

    #location = locate_image_on_screen('botrespond.png')

    #time.sleep(1)
    click_on_image('forward.png')
    time.sleep(1)
    click_on_image('clickbee2.png')
    time.sleep(1)
    click_on_image('started.png')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    if locate_image_on_screen('skipohno.png'):
        click_on_image('back.png')
        backwait = locate_image_on_screen('backwait.png')
        while backwait:
            time.sleep(0.5)
            backwait = locate_image_on_screen('backwait.png')

        return
    time.sleep(1)

    if locate_image_on_screen('congratulations.png'):
        pygame.mixer.music.load('beep.wav')
        pygame.mixer.music.play()
        time.sleep(1)

def scenario4():
    # Добавьте реализацию четвертого сценария здесь
    time.sleep(1)
    click_on_image('more.png')
    time.sleep(1)
    click_on_image('viewposts.png')
    time.sleep(1)
    if locate_image_on_screen('ohnoposts.png'):
        click_on_image('back.png')
        return
    else:
        while(True):
            pygame.mixer.music.load('beep1.wav')
            pygame.mixer.music.play()
            time.sleep(1)

        time.sleep(10)
        click_on_image('watched.png')
        time.sleep(1)
        click_on_image('viewposts.png')
        time.sleep(1)
        click_on_image('back.png')
        backwait = locate_image_on_screen('backwait.png')
        while backwait:
            time.sleep(0.5)
            backwait = locate_image_on_screen('backwait.png')
        time.sleep(1)
def on_press(key):
    global active
    if key == keyboard.Key.space:
        active = not active
        print(f"{'Начало' if active else 'Остановка'} выполнения сценариев.")

def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    print("Нажмите ПРОБЕЛ, чтобы начать/остановить выполнение сценариев.")
    pygame.mixer.music.load('beep.wav')

    while True:
        if active:
            #scenario4()
            scenario1()
            scenario3()
            scenario2()
            time.sleep(1)
        else:
            time.sleep(1)


if __name__ == "__main__":
    main()
