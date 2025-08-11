# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/'
driver.maximize_window()

try:
    driver.get(sbis_site)
    sleep(1)

    contacts_button = driver.find_element(By.CSS_SELECTOR, "a[href='/contacts']")
    assert contacts_button is not None, "Не найден элемент 'Контакты'"
    contacts_button.click()
    sleep(1)

    tensor_banner = driver.find_element(By.CSS_SELECTOR, "img[alt='Разработчик системы Saby — компания «Тензор»']")
    assert tensor_banner is not None, "Не найден баннер 'Тензор'"
    tensor_banner.click()
    sleep(1)

    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url.startswith(tensor_site), "Не удалось перейти на сайт Тензора"
    sleep(1)

    power_in_people_block = driver.find_element(By.CLASS_NAME, 'tensor_ru-Index__block4-bg')
    driver.execute_script("arguments[0].scrollIntoView();", power_in_people_block)
    sleep(1)
    assert power_in_people_block.is_displayed(), "Блок 'Сила в людей' не найден или не отображается"

    about_page = driver.find_element(By.CLASS_NAME, 'tensor_ru-Index__block4-bg [href="/about"]')
    assert about_page is not None, "Не найдена кнопка Подробнее"
    about_page.click()
    sleep(1)
    assert driver.current_url == 'https://tensor.ru/about', "Не верный URL после перехода в Подробнее"

    print("Тест успешно пройден")
finally:
    driver.quit()