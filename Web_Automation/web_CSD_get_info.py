import requests                 # Requests HTTP Library
from bs4 import BeautifulSoup   # bs4 içerisindeki BeautifulSoup class'ını içeri aktarır
# ---

# Sayfayı indir
req_get = requests.get("https://csystem.org/") 
req_get.raise_for_status()                              # Denetle sorun var mı?

# Kaynağını verip bir html parser soup yarat?
soup = BeautifulSoup(req_get.text, 'html.parser')
div_elements = soup.findAll("div" , attrs = {'class': 'element element_3 excerpt_read_more'})           # Sitede okumak istediğin div'i ver, bütün bu başlıktakileri alsın

# İçeriğini HTML'den arındırıp text bas
for divs in div_elements:
    text = divs.get_text(strip=True)
    print(text)




# import requests
# from bs4 import BeautifulSoup

# # Milliyet döviz sayfasının URL'si
# url = 'https://www.milliyet.com.tr/ekonomi/doviz-kurlari/'

# # Sayfayı indir
# response = requests.get(url)
# response.raise_for_status()  # Sayfanın doğru indirildiğini kontrol et

# # BeautifulSoup ile HTML'i parse et
# soup = BeautifulSoup(response.text, 'html.parser')

# # Dolar/TL kurunu içeren elementi bul
# dolar_tl_element = soup.find('div', {'class': 'dl-horizontal'})
# dolar_tl = dolar_tl_element.find_all('span')[1].text.strip()  # Buradaki 1 index'i ilgili değeri verir

# print(f"Dolar/TL kuru: {dolar_tl}")
