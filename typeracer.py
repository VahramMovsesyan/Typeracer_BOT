import time
import pyautogui
from selenium import webdriver

# Enter typeracer.com
driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
driver.get("https://play.typeracer.com/")

# waiting for loading page than enter online room
time.sleep(3)
pyautogui.hotkey("Ctrl", "Alt", "I")

# graphing the text
time.sleep(2)
text = driver.find_element_by_class_name("gameView").text
text = text.split("\n")
# print(text[-3])

# waiting for start the game
time.sleep(15)

# start typing
pyautogui.typewrite(text[-3], interval=0.05)
# driver.quit()
