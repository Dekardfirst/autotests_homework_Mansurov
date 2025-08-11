# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import os.path
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

sbis_url = 'https://sbis.ru/'
download_dir = os.path.dirname(os.path.abspath(__file__))

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

try:
    driver.get(sbis_url)
    sleep(1)

    download_local_versions = driver.find_element(By.CSS_SELECTOR, 'a[href="/download"]')
    driver.execute_script("arguments[0].scrollIntoView();", download_local_versions)
    sleep(1)
    download_local_versions.click()
    sleep(1)

    select_sabe_decktop = driver.find_element(By.XPATH, "//div[@class='controls-TabButton__caption' and text()='Saby Desktop']")
    select_sabe_decktop.click()
    sleep(1)

    select_os_windows = driver.find_element(By.CSS_SELECTOR, 'a[href="https://update.saby.ru/SabyDesktop/master/win32/saby-setup.exe"]')
    select_os_windows.click()
    sleep(2)

    filename = "saby-setup.exe"
    filepath = os.path.join(download_dir, filename)

    start_time = time.time()
    while not os.path.exists(filepath):
        time.sleep(1)
        if time.time() - start_time > 120:
            raise TimeoutError("Файл не скачался за 120 секунд")

    file_size_bytes = os.path.getsize(filepath)
    file_size_mb = file_size_bytes / (1024 * 1024)
    print(f"Размер скачанного файла: {file_size_mb:.2f} MB")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
