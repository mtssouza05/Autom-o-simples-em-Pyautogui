from ssl import AlertDescription
import pyautogui
import time

pyautogui.alert('Código vai começar')
pyautogui.PAUSE=0.5

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)

#pyautogui.write(endereço do drive)
pyautogui.press('enter')

pyautogui.hotkey('winleft', 'd')
#pyautogu.moveTo(x, y)
pyautogui.mouseDown()
#pyautogui.moveTo(x, y)

pyautogui.hotkey('alt', 'tab')
time.sleep(5)

pyautogui.alert(' O código terminou')

