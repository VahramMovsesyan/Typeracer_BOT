import time
import pyautogui
from selenium import webdriver

# Enther typeracer.com
driver = webdriver.Chrome("C:\\Program Files (x86)\\chromedriver.exe")
driver.get("https://play.typeracer.com/")

# waitting for loadding page than enter online room
time.sleep(3)
pyautogui.hotkey("Ctrl", "Alt", "I")

# grapping the text
time.sleep(2)
text = driver.find_element_by_class_name("gameView").text
text = text.split("\n")
# print(text[-3])

# waitting for start the game
time.sleep(15)

# typing
pyautogui.typewrite(text[-3], interval=0.05)
# driver.quit()
