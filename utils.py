from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

TEMPO_ESPERA = 2.5

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    sleep(TEMPO_ESPERA)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    sleep(TEMPO_ESPERA)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_mensagem[1].click()
    sleep(TEMPO_ESPERA)
    for linha in mensagem.split('\n'):
        ActionChains(driver).send_keys(linha).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    sleep(TEMPO_ESPERA)
    ActionChains(driver).send_keys(Keys.RETURN).perform()
