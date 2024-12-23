import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

user_data_dir = "C:/Users/"seu_usuario"/AppData/Local/Google/Chrome/User Data"
profile_dir = "DEFAULT"

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
chrome_options.add_argument(f"profile-directory={profile_dir}")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    print('Abrindo o zap')
    driver.get('https://web.whatsapp.com/')
    time.sleep(15)
    
    contato = '' #Nome do contato
    palavras = 'mano' #Mensagem para enviar
    #da para fazer uma lista com as palavras tbm, por isso foi usafo o for na linha 39
  
    print("Selecionando o  contato...")
    contato_xpath = f'//*[@id="side"]//span[contains(text(), "{contato}")]'
    contato_selecionado = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, contato_xpath))
    )
    contato_selecionado.click()
    print("Contato selecionado!")

    for p in palavras:
        print('Enviando mensagem..')
        message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'
        message_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, message_box_xpath))
        )
        #time.sleep(5)
    
        message_box.click()
        message_box.send_keys(palavras)
        message_box.send_keys(Keys.RETURN)
    print("Mensagem enviada com sucesso!")
    time.sleep(5)
except Exception as e:
    print(f"Ocorreu um erro: {e.with_traceback}")
