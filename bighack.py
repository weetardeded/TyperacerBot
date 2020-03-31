from selenium import webdriver
from time import sleep
import bot_func as bf
from PIL import Image

wd = webdriver.Chrome("C:\\Users\\USERNAME\\Desktop\\typeracer bot\\chromedriver.exe")
wd.get("https://play.typeracer.com/")

text = bf.getRaceText(wd)
print("RACE TEXT: " + text)

bf.waitForGameToStart(wd, text)


sleep(100)
wd.quit()