import requests                 # Requests HTTP Library
from bs4 import BeautifulSoup   # bs4 içerisindeki BeautifulSoup class'ını içeri aktarır
from selenium import webdriver
# ---

# GeckoDriver'ın dosya yolunu belirtin
driver_path = 'C:/Users/enesc/Masaüstü/Python/Web_Test/eklenti'
# "C:/Users/enesc/Masaüstü/Python/Web_Test/eklenti/geckodriver.exe"

# Firefox WebDriver'ı başlat
my_web_driver = webdriver.Firefox()
my_web_driver.get('https://csystem.org/')







# from selenium import webdriver

# # GeckoDriver'ın dosya yolunu belirtin
# driver_path = '/path/to/geckodriver'

# # Firefox WebDriver'ı başlat
# driver = webdriver.Firefox(executable_path=driver_path)

# # Bir web sitesini aç
# driver.get('https://www.example.com')

# # Tarayıcıyı kapat
# driver.quit()