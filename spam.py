import pyautogui, time
time.sleep(5)
file = open('spam.txt', 'r', encoding='utf-8' )
for row in file:
  pyautogui.typewrite(row)
  pyautogui.press('enter')
  time.sleep(0.1)