# ---
# Facebook'a asagida verilen username ve password'u vererek giris yapan script
# ---

from selenium import webdriver
from selenium.webdriver.common.by import By

# ---

username = "enescan58turko@hotmail.com"
password = "XYZ"


# Firefox WebDriver'ı başlat
my_web_driver = webdriver.Firefox()
my_web_driver.get('https://www.facebook.com/?locale=tr_TR')


my_web_driver.find_element(By.NAME, "email").send_keys(username)
my_web_driver.find_element(By.NAME, "pass").send_keys(password)
my_web_driver.find_element(By.NAME, "login").click()




# --- KAYNAKCA
# https://www.youtube.com/watch?v=doPo9q6on6c&t=206s


# from selenium import webdriver

# # GeckoDriver'ın dosya yolunu belirtin
# driver_path = '/path/to/geckodriver'

# # Firefox WebDriver'ı başlat
# driver = webdriver.Firefox(executable_path=driver_path)

# # Bir web sitesini aç
# driver.get('https://www.example.com')

# # Tarayıcıyı kapat
# driver.quit()