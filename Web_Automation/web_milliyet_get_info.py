import requests                 # Requests HTTP Library
from bs4 import BeautifulSoup   # bs4 içerisindeki BeautifulSoup class'ını içeri aktarır
# ---


# Sayfayı indir
req_get = requests.get("https://www.milliyet.com.tr/ekonomi/") 
req_get.raise_for_status()                                                                              # Denetle sorun var mı?

# Kaynağını verip bir html parser soup yarat?
soup = BeautifulSoup(req_get.text, 'html.parser')

elements_kur_tipi   = soup.findAll("span" , attrs = {'class': 'currency__text'})                        # Sitede okumak istediğin span'i ver, bütün bu başlıktakileri alsın
elements_kur_degeri = soup.findAll("span" , attrs = {'class': 'currency__value__text'})                 # Sitede okumak istediğin span'i ver, bütün bu başlıktakileri alsın


# İçerisinde dövizlerin olacağı bir liste yaratılır. Bu listenin içeriği kur değeri, ulaşımı ise kur ismidir
list_ekonomi = {}

# HTML temizlenir ve liste doldurulur
for idx in range(len(elements_kur_tipi)):
    text_kur_tipi   = elements_kur_tipi[idx].get_text(strip=True)
    text_kur_deger  = elements_kur_degeri[idx].get_text(strip=True)
    
    
    list_ekonomi[text_kur_tipi] = text_kur_deger
    
    print( idx, text_kur_tipi, list_ekonomi[text_kur_tipi] )

