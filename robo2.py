from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email = "jocelinogg@yandex.com"
senha = "mailpass09"
destinatario = "jocelinogg@yandex.com"
assunto = "enviando ymail por robo"
mensagem = "A morte é triste, mas a vida é pior..."

driver = webdriver.Firefox(r"C:\Users\JocelinoFG\Desktop\Robos")

print("iniciando robo..")
print("Acessando yandexmail..")

url = "https://passport.yandex.com/auth/add?from=mail&origin=hostroot_homer_auth_L_com&retpath=https%3A%2F%2Fmail.yandex.com%2F%3Fuid%3D1170422679&backpath=https%3A%2F%2Fmail.yandex.com%3Fnoretpath%3D1"
driver.get(url)

print("Realizando login..")

#login
login = driver.find_element_by_name("login")
login.send_keys(email)
login.send_keys(Keys.RETURN)
time.sleep(5)

#senha
password = driver.find_element_by_id("passp-field-passwd")
password.send_keys(senha)
password.send_keys(Keys.RETURN)
time.sleep(7)

#abrir caixa de ymail
botao = driver.find_element_by_class_name("//div[@class='mail-ComposeButton-Wrap js-compose-button-container']")
botao.click()
time.sleep(5)

#destinatario

para = driver.find_element_by_xpath("//div[@class='composeYabbles']")
para.send_keys(destinatario)
para.send_keys(Keys.RETURN)
time.sleep(5)

#asssunto do email
titulo = driver.find_element_by_name("subject")
titulo.send_keys(assunto)
titulo.send_keys(Keys.RETURN)
time.sleep(5)

#mensagem


letter = driver.find_element_by_xpath("//div[@class='cke_wysiwyg_div cke_reset cke_enable_context_menu cke_editable cke_editable_themed cke_contents_ltr cke_htmlplaceholder']")
letter.send_keys(mensagem)
time.sleep(5)



driver.close()


#pagina util

#http://pythonclub.com.br/selenium-parte-1.html
