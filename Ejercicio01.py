from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Iniciar el navegador
driver = webdriver.Chrome()

# Ir a Bing en lugar de Google
driver.get("https://www.bing.com")
time.sleep(2)

# Buscar "Selenium IDE"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium IDE")
search_box.send_keys(Keys.RETURN)
time.sleep(3)  # Espera a que se carguen bien los resultados

# Obtener el primer enlace
first_result = driver.find_element(By.CSS_SELECTOR, "li.b_algo h2 a")

# Imprimir el primer enlace para verificar que es el oficial
print("Primer enlace encontrado:", first_result.get_attribute("href"))

# Comando personalizado: Verificar que el primer enlace sea el sitio oficial de Selenium IDE
expected_url = "https://www.selenium.dev/selenium-ide/"
actual_url = first_result.get_attribute("href")

if expected_url in actual_url:
    print("El sitio oficial de Selenium IDE aparece como el primer resultado.")
else:
    print("El sitio oficial NO aparece como el primer resultado.")

driver.quit()