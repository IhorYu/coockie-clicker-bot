import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("/Users/ihor/Documents/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(5)
time_out = time.time() + 60 * 5
buy_time = time.time() + 5

lang_choice = driver.find_element(By.XPATH, '//*[@id="langSelect-RU"]')
lang_choice.click()
time.sleep(5)
got_it = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
got_it.click()

cookie = driver.find_element(By.CSS_SELECTOR, '#bigCookie')

while time.time() < time_out:

    cookie.click()

    if time.time() > buy_time:
        unlocked_upgrades = driver.find_elements(
            By.CSS_SELECTOR, '.crate.upgrade.enabled')

        if len(unlocked_upgrades) > 0:
            id = (len(unlocked_upgrades) - 1)

            buy_upgrade = driver.find_element(
                By.CSS_SELECTOR, f'#upgrade{id}.crate.upgrade.enabled')

            buy_upgrade.click()

        unlock_items_prices = driver.find_elements(
            By.CSS_SELECTOR, '.product.unlocked.enabled span.price')

        unlock_items_prices = [int(price.text.replace(",", ""))
                               for price in unlock_items_prices]

        try:
            id = unlock_items_prices.index(max(unlock_items_prices))

            buy_item = driver.find_element(
                By.CSS_SELECTOR, f'#product{id}.product.unlocked.enabled')

            buy_item.click()

            buy_time = time.time() + 5
        except:
            continue

cookie_per_sec = driver.find_element(By.CSS_SELECTOR, '#cookies div')
per_sec = cookie_per_sec.text.replace("per second : ", "")
print(f"cookies/second: {per_sec}")
time.sleep(5)
driver.quit()
