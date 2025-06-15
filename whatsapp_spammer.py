import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Konfigurasi untuk Termux
os.environ['HOME'] = '/data/data/com.termux/files/home'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def whatsapp_spam():
    try:
        # Setup Chrome untuk Termux
        driver = webdriver.Chrome(executable_path='/data/data/com.termux/files/home/geckodriver/geckodriver',
                                 options=chrome_options)
        
        driver.get("https://web.whatsapp.com/")
        print("Buka WhatsApp di browser biasa dan scan QR code...")
        
        # Tunggu scan QR code
        wait = WebDriverWait(driver, 120)
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')))
        
        print("Berhasil login!")
        
        # Pilih chat terakhir
        last_chat = driver.find_element(By.XPATH, '(//div[contains(@class,"_2KKXC")])[last()]')
        last_chat.click()
        time.sleep(3)
        
        # Input box
        input_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        
        # Mulai mengirim pesan
        while True:
            msg = f"Pesan otomatis {random.randint(1000,9999)}"
            input_box.send_keys(msg)
            input_box.send_keys(Keys.ENTER)
            print(f"Pesan terkirim: {msg}")
            time.sleep(random.randint(5,15))  # Delay acak
            
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    whatsapp_spam()
