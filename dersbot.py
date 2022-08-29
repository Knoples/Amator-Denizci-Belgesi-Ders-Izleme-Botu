from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, datetime
import time
print("""
           https://github.com/Knoples
   ▄█    █▄     ▄██████▄     ▄████████         ▄██████▄     ▄████████  ▄█       ████████▄   ▄█  ███▄▄▄▄    ▄█   ▄███████▄  
  ███    ███   ███    ███   ███    ███        ███    ███   ███    ███ ███       ███   ▀███ ███  ███▀▀▀██▄ ███  ██▀     ▄██ 
  ███    ███   ███    ███   ███    █▀         ███    █▀    ███    █▀  ███       ███    ███ ███▌ ███   ███ ███▌       ▄███▀ 
 ▄███▄▄▄▄███▄▄ ███    ███   ███              ▄███         ▄███▄▄▄     ███       ███    ███ ███▌ ███   ███ ███▌  ▀█▀▄███▀▄▄ 
▀▀███▀▀▀▀███▀  ███    ███ ▀███████████      ▀▀███ ████▄  ▀▀███▀▀▀     ███       ███    ███ ███▌ ███   ███ ███▌   ▄███▀   ▀ 
  ███    ███   ███    ███          ███        ███    ███   ███    █▄  ███       ███    ███ ███  ███   ███ ███  ▄███▀       
  ███    ███   ███    ███    ▄█    ███        ███    ███   ███    ███ ███▌    ▄ ███   ▄███ ███  ███   ███ ███  ███▄     ▄█ 
  ███    █▀     ▀██████▀   ▄████████▀         ████████▀    ██████████ █████▄▄██ ████████▀  █▀    ▀█   █▀  █▀    ▀████████▀ 
                                                                      ▀   https://github.com/Knoples                                                 
""")
CBLUEB2 = '\33[94m'
CEND = '\033[0m'
print(CBLUEB2 + "OTOMATİK DERS İZLEME BOTUNA HOŞ GELDİNİZ " + CEND)
print(CBLUEB2 + "DERSLER OTOMATİK OLARAK İZLENECEKTİR. SÜRE DOLUNCA İLERİYE BASACAKTIR. LÜTFEN İŞLEM SIRASINDA KOMUT İSTEMİNİ KAPATMAYINIZ... !!! " + CEND)
print(CBLUEB2 + "HESABINIZA HİÇ GİRİŞ YAPMADAN BU BOT'U KULLANMAYINIZ. ÖNCELİKLE BİR KERE BİLE OLSA BOT'U AÇMADAN ÖNCE DERSİ BAŞLATIN. GERİSİ BENDE\n" + CEND)

kimlik = input("Giriş için TC Kimliğinizi giriniz: ")
sifre  = input("Giriş için şifrenizi giriniz: ")
driver=webdriver.Firefox()
driver.get("https://adbs.uab.gov.tr/login")
elem4 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/in-root/in-login/div/div[1]/div/div[1]/div/div/a"))).click()

elem1 = driver.find_elements(By.XPATH, "/html/body/div[1]/main/section[2]/form/fieldset/div[1]/div/input")
for chk in elem1:
    chk.click()
elem1[0].send_keys(kimlik)
elem2 = driver.find_elements(By.XPATH, "/html/body/div[1]/main/section[2]/form/fieldset/div[2]/div/input[1]")
for chk in elem2:
    chk.click()
elem2[0].send_keys(sifre)
elem3 = driver.find_elements(By.XPATH, "/html/body/div[1]/main/section[2]/form/div[2]/input[4]")
for chk in elem3:
    chk.click()
time.sleep(3)
elem5 = driver.find_elements(By.XPATH, "/html/body/div/div/div/div/button[1]")
for chk in elem5:
    chk.click()
time.sleep(1)
elem6 = driver.find_elements(By.XPATH, "/html/body/in-root/in-users/in-dashboard-layout/main/in-user-home/div/div[1]/div/ul/li[1]/a")
for chk in elem6:
    chk.click()
time.sleep(1)
elem7 = driver.find_elements(By.XPATH, "/html/body/in-root/in-users/in-dashboard-layout/main/in-educations/div/div/div[2]/div/div[2]/div[1]/span/in-loading-button/dx-button")
for chk in elem7:
    chk.click()
time.sleep(1)

driver.execute_script("window.scrollTo(0, 800);")
time.sleep(1)
elem8 = WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/in-root/in-users/in-dashboard-layout/main/in-education-single/div/div/div[2]/div/div[2]/div/ul/li[8]/in-loading-button/dx-button"))).click()

time.sleep(1)
elem9 = driver.find_elements(By.XPATH, "/html/body/div/div/div/div[3]/div/div[2]/div[1]")
for chk in elem9:
    chk.click()
time.sleep(1)

ksure = driver.find_element(By.CLASS_NAME,"mb-0").text
i=0
while(i<10):
    ksure = driver.find_element(By.CLASS_NAME,"mb-0").text

    date_string = ksure
    format = "%M:%S"
    date = datetime.strptime(date_string, format)
    bak = date.minute*60+date.second+5
    time.sleep(bak)
    driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(1)
    elem11=driver.find_elements(By.XPATH, "/html/body/in-root/in-users/in-dashboard-layout/main/in-lecture/div/div[1]/div/div[2]/span[2]/in-loading-button/dx-button")
    for chk in elem11:
      chk.click()

    i = i+0

print