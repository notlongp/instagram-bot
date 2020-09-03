from selenium import webdriver
import time
from instaBot import *

bot = instagramBot('YOUR.USERNAME', 'YOUR.PASSWORD')
bot.findPersonDM('PERSON.HANDLE')
time.sleep(2)
bot.DM('Hello')

# while True:
#     bot.DM('whats up')

# bot.Like()
# while True:
#     bot.Like()

