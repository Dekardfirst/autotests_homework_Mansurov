# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

LOGIN = "nyaa"
PASSWORD = "nyaanyaanyaa123"

fix_sbis = "https://fix-online.sbis.ru/"

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get(fix_sbis)
    sleep(1)

    # Авторизация
    login = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
    assert login is not None, "Полe логина не найдено"
    login.send_keys(LOGIN, Keys.ENTER)
    sleep(2)

    password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
    assert password is not None, "Поле пароля не найдено"
    password.send_keys(PASSWORD, Keys.ENTER)
    sleep(5)

    # Переход в реестр Контакты
    first_click_contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"] [data-qa="NavigationPanels-Accordion__title"]')
    assert first_click_contacts is not None, "Поле Контакты не найдено"
    first_click_contacts.click()
    sleep(1)
    contacts_page = driver.find_element(By.CLASS_NAME, 'NavigationPanels-SubMenu__headTitle')
    assert contacts_page is not None, "Поле Контакты не найдено"
    contacts_page.click()
    sleep(3)

    # Отправка сообщения себе
    add_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    assert add_button is not None, "Кнопка Добавить отсутствует"
    add_button.click()
    sleep(1)

    text_place = driver.find_element(By.CSS_SELECTOR, '[templatename="Addressee/popup:Stack"] [type="text"]')
    text_place.send_keys('Ишова Наталия')
    sleep(1)
    search_user = driver.find_element(By.CSS_SELECTOR, '[data-qa="item"] [class="msg-addressee-selector__addressee"]')
    search_user.click()
    sleep(1)

    text = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    text.send_keys("Сообщение себе", Keys.ENTER)
    sleep(1)

    send_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    send_button.click()
    sleep(1)

    # Поиск сообщения в реестре
    message = driver.find_elements(By.CSS_SELECTOR, '[data-qa="item"] .msg-entity-text')
    message_found = False
    for msg in message:
        if msg.text == "Сообщение себе":
            message_found = True
            break
    assert message_found, "Сообщение не найдено"

    # Удаление сообщения
    for i in message:
        if i.text == "Сообщение себе":
            action_chains = ActionChains(driver)
            action_chains.move_to_element(i).perform()
            sleep(1)
            delete = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
            delete.click()
            sleep(1)
            break

    # Проверка удаления
    message_after_delete = driver.find_elements(By.CSS_SELECTOR, '[data-qa="item"] .msg-entity-text')
    message_found = False
    for msg in message_after_delete:
        if msg == "Сообщение себе":
            message_found = True
            break

    assert not message_found, "Сообщение с текстом 'Сообщение себе' есть в реестре"

    print("Тест прошел успешно")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()