from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Definir o caminho correto para o ChromeDriver
chrome_driver_path = 'C:/Users/nicol/OneDrive/Documentos/UniFECAF/5º Semestre/3. Quality Assurance/Projeto Final/SPRINT 2/projetoQA/chromedriver.exe'

# Configurar o Service do ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Inicializar o WebDriver com o serviço configurado
driver = webdriver.Chrome(service=service)

# Acessar o Instagram
driver.get("https://www.instagram.com/")

# Esperar alguns segundos para garantir que os elementos carreguem
time.sleep(10)

# Encontrar o campo de login e preencher
username = driver.find_element(By.NAME, "username")
username.send_keys("kkj.memes")

# Encontrar o campo de senha e preencher
password = driver.find_element(By.NAME, "password")
password.send_keys("palmeiras1914")

# Simular o clique no botão de login (usando o seletor CSS correto)
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Esperar alguns segundos para o login ser processado
time.sleep(20)

# Verificar se o login foi bem-sucedido (a URL da página após o login pode mudar)
if "accounts" in driver.current_url:
    print("Login realizado com sucesso!")
else:
    print("Falha no login.")

# Fechar o navegador
driver.quit()
