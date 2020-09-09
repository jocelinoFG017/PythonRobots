from selenium import webdriver
# from selenium.webdriver.commom.keys import Keys
import time

print("Begin robot.....\n")

driver = webdriver.Firefox(r"C:\Users\JocelinoFG\Desktop\Robos")

driver.get("https://registro.br/")
time.sleep(8) # dormindo
driver.close()
