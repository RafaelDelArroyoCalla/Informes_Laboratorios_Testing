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

results = driver.find_elements(By.CSS_SELECTOR, "a")


print("Enlaces encontrados:")
for result in results:
    href = result.get_attribute("href")
    if href:
        print(href)


found = any("selenium.dev/selenium-ide" in result.get_attribute("href") if result.get_attribute("href") else False for result in results)

if found:
    print("Sitio oficial encontrado.")
else:
    print("Sitio oficial NO encontrado.")

driver.quit()
