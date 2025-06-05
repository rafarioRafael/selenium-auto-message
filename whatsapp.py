import csv
import json
import random
import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

#keeping the data (cookies, cache, etc.) from the browser

options = Options()
options.add_argument("--user-data-dir=C:/selenium/whatsapp_profile")
options.add_argument("--profile-directory=Default")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def choose_message(path_json="frases/goodnight.json"):
    with open(path_json, encoding='utf-8') as file:
        dados = json.load(file)
        return random.choice(dados["frases"])

def load_contacts(path_csv="contatos.csv"):
    contatos = []
    with open(path_csv, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for linha in reader:
            contatos.append(linha['nome'])
    return contatos

def search_contact(contato):
    print("Buscando contato...")

    try:
        # Localiza e clica na caixa de busca
        search_box_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, search_box_xpath))
        )
        search_box.clear()
        search_box.click()
        time.sleep(1)
        search_box.send_keys(contato)
        time.sleep(2)

        # Clica no contato encontrado
        contato_xpath = f'//span[@title="{contato}"]'
        contato_selecionado = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, contato_xpath))
        )
        time.sleep(2)
        contato_selecionado.click()
        print("Contato selecionado!")

        return True
    except Exception as e:
        print(f"Contato '{contato}' não encontrado ou não foi possível clicar.")
        return False
    
def night_routine():
    contatos = load_contacts() #Nome do contato
    for contato in contatos:
        mensagem = choose_message() 
        print(f"Enviando para {contato}: {mensagem}")

        if search_contact(contato):
            try:
                #Enviando mensagem
                message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p'
                message_box = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, message_box_xpath))
                )
                message_box.click()
                message_box.send_keys(mensagem)
                message_box.send_keys(Keys.RETURN)
                time.sleep(2)
            except Exception as e:
                print(f"Erro ao enviar mensagem para {contato}: {e}")
        else:
            print(f"Pulo o contato {contato} pois não foi possível localizá-lo.")
    print("Rotina terminada.")

try:
    print('Abrindo o zap')
    driver.get('https://web.whatsapp.com/')
    time.sleep(15)

    schedule.every().day.at("22:37").do(night_routine)
    #schedule.every(1).minutes.do(night_routine)


    print("aguardando horario...")
    while True:
        schedule.run_pending()
        time.sleep(1)

except Exception as e:
    print(f"Ocorreu um erro: {e.with_traceback}")

