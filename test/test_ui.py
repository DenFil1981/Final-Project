from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

driver = webdriver.Chrome(executable_path='path/to/chromedriver')

@allure.epic("market-delivery")
@allure.severity(severity_level='normal')
@allure.tittle("Заказ продуктов")
@allure.description("Заказываем товары на онлайн платформе")
@allure.feature('Тест 2')

#Авторизация

def test_login(driver):  # Передаем драйвер как параметр
    try:
        driver.get('https://market-delivery.yandex.ru/api/auth/login')

        with allure.step("Находим элементы и вводим данные"):
            username_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, 'username'))
            )
            username_field.send_keys('filinov@ymail.com')
            password_field = driver.find_element(By.NAME, 'password')
            password_field.send_keys('Qwertylas1902')
        with allure.step("Отправляем форму"):
            login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Войти")]')
            login_button.click()        
        with allure.step("Проверка успешного входа"):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "header") and contains(text(), "Корзина")]'))
            )
            assert "Добро пожаловать" in driver.page_source 
    finally:           
        with allure.step("Закрыть браузер"):
            driver.quit()
            
#Ввод названия товара в поисковой строке  

def test_search_product():
    try:
        driver.get('https://market-delivery.yandex.ru/kaluga?shippingType=delivery')  

        with allure.step("Находим поисковую строку"): 
            search_box = driver.find_element(By.NAME, 'Найти') 
        with allure.step("Вводим название товара"):
            product_name = 'Огурец'
            search_box.send_keys(product_name)        
        with allure.step("Отправляем форму"): 
            search_box.send_keys()    
        with allure.step("Проверяем наличие результатa"):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "product-card")]'))
            )
            assert product_name in driver.page_source
    finally:
        with allure.step("Закрыть браузер"):
            driver.quit()

#Покупка товара

def test_purchase_product():
       try:
           with allure.step("Открываю целевой сайт"):
               driver.get('https://market-delivery.yandex.ru/kaluga?shippingType=delivery')  
           with allure.step("Находим поисковую строку и ищем товар"):
               search_box = driver.find_element(By.NAME, 'Найти')  
               product_name = 'Огурец'
               search_box.send_keys(product_name)
           with allure.step("Находим и кликаем по продукту"):
               product_link = WebDriverWait(driver, 10).until(
               EC.element_to_be_clickable((By.LINK_TEXT, product_name))
               )
               product_link.click()
           with allure("Ждем загрузки страницы товара"):
               add_to_cart_button = WebDriverWait(driver, 10).until(
               EC.element_to_be_clickable((By.ID, 'de6d8ad7-57e5-47c1-82e1-6ceb9964a207')))  
           with allure("Добавляем товар в корзину"):
               add_to_cart_button = driver.find_element(By.ID, 'de6d8ad7-57e5-47c1-82e1-6ceb9964a207')  
               add_to_cart_button.click()
           with allure("Проверяем, что товар добавлен в корзину"):         
               cart_message = driver.find_element(By.CLASS_NAME, 'AppPopup_root AppPopup_defaultWidth AppPopup_isVisible')  
               assert "Товар добавлен в корзину" in cart_message.text, "Товар не был добавлен в корзину"
           with allure("Переход к корзине"):
               cart_button = driver.find_element(By.Button, 'UiKitButton_root UiKitButton_size-m UiKitButton_variant-action UiKitButton_shape-default DesktopHeader_headerItem')  
               cart_button.click()
           with allure("Ждем загрузки страницы корзины"):
               WebDriverWait(driver, 10).until(
               EC.visibility_of_element_located((By.CLASS_NAME, 'GoCheckoutDesktopLayout_content'))  
               )
           with allure.step("Проведение оформления заказа"):
               proceed_to_checkout_button = driver.find_element(By.ID, 'UiKitButton_root UiKitButton_size-l UiKitButton_variant-action UiKitButton_shape-default GoCheckoutDesktopPayOptions_payButton')  
               proceed_to_checkout_button.click()
           with allure.step("Заполнение информации для оформления заказа"):
           
               address_field = driver.find_element(By.ID, 'name')  
               address_field.send_keys('Центральная улица,134А')
               
               office_field = driver.find_element(By.NAME, 'id_5')  
               office_field.send_keys('MTC')

               comment_field = driver.find_element(By.NAME, 'comment')  
               comment_field.send_keys('Оставить у двери')

               payment_button = driver.find_element(By.ID, 'payment')  
               payment_button.click()

           with allure.step("Проверяем, что заказ успешно оформлен"):
               assert "Спасибо за покупку" in driver.page_source, "Заказ не завершен"            
       finally:
           with allure.step("Закрыть браузер"):
              driver.quit()
              
#Обратная связь              

def test_feedback():
    
    try:
        with allure.step("Переходим на страницу обратной связи"):
            driver.get("https://market-delivery.yandex.ru/")
        with allure.step("Здесь нужно выбрать элемент, который открывает форму обратной связи"):
            feedback_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "support-chat"))  
            )
            feedback_link.click()
        with allure.step("Заполняем форму обратной связи"):       
            email_field = driver.find_element(By.NAME, "email")  
            email_field.send_keys("filinov@ymail.com")   
            message_field = driver.find_element(By.NAME, "answer_long_text_10246894")  
            message_field.send_keys("Спасибо!")

        with allure.step("Нажимаем на кнопку отправки"):
            submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//g-button__tex[contains(text(), 'Отправить')]"))  
            )
            submit_button.click()
        with allure.step("Проверка успешной отправки"):
            success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "Спасибо! Постараемся решить проблему в течение 24 часов."))  
            )
            print(success_message.text)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        driver.quit()

#Акции и скидки
       
def test_discounts():
    try:
        with allure.step("Переходим на страницу акций"):
            driver.get("https://market-delivery.yandex.ru/retail/paterocka/catalog/44008?placeSlug=pyaterochka_vdnsa")
        with allure.step("Ждем, пока акционные элементы станут видимыми"):
            promotions_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Акции и скидки']"))
            )
        with allure.step("Теперь находим акционные товары"):
            promotion_items = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".UiKitRetailDesktopCategoryHeader_title UiKitText_root UiKitText_Title4 UiKitText_Bold UiKitText_Text"))
            )
        with allure.step("Проверяем, что акционные товары находятся на верхней позиции"):
            if promotion_items:
              print("Акционные товары:")
        for item in promotion_items:
            title = item.find_element(By.CSS_SELECTOR, ".DesktopGoodsList_list").text
            discount = item.find_element(By.CSS_SELECTOR, ".DesktopGoodsList_item").text
            print(f"{title} - {discount}")
        else:
            print("Нет актуальных акционных товаров")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        driver.quit()        

    

       
