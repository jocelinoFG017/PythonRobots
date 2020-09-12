from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email = "jocelinogg@yandex.com"
senha = "mailpass09"
destinatario = "jocelinogg@yandex.com"
assunto = "enviando ymail por robo"
mensagem = "A morte é triste, mas a vida é pior..."

driver = webdriver.Firefox("")

print("iniciando robo..")
print("Acessando yandexmail..")

url = ""
driver.get(url)

print("Realizando login..")

#login
login = driver.find_element_by_name("")
login.send_keys(email)
login.send_keys(Keys.RETURN)
time.sleep(5)

#senha
password = driver.find_element_by_name("")
password.send_keys(senha)
password.send_keys(Keys.RETURN)
time.sleep(5)

#abrir caixa de ymail
botao = driver.find_element_by_xpath("")
botao.click()
time.sleep(5)

#(destinatario

para  = driver.find_element_by_xpath("")
para.send_keys(destinatario)
para.send_keys(Keys.RETURN)
time.sleep(5)

#asssunto do email
titulo = driver.find_element_by_xpath("")
titulo.send_keys(assunto)
titulo.send_keys(Keys.RETURN)
time.sleep(5)

#mensagem

letter = driver.find_element_by_xpath("")
letter.send_keys(mensagem)
time.sleep(5)



driver.close()
