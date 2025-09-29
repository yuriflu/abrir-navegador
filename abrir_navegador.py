from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = "C:/Users/aluno/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(driver_path)

options = webdriver.ChromeOptions()
prefs = {
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True,
    "download.default_directory": "C:/Users/aluno/Downloads"
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://ead.unieuro.edu.br/login/index.php")

usuario = "seu_usuario"
senha = "sua_senha"

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(usuario)
driver.find_element(By.ID, "password").send_keys(senha)
driver.find_element(By.ID, "loginbtn").click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Projetos"))).click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "course-content")))

try:
    link_pdf = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "globo.pdf"))
    )
    link_pdf.click()
    print("Download iniciado: globo.pdf")
except:
    print("Arquivo 'globo.pdf' não encontrado.")

time.sleep(5)
driver.quit()
