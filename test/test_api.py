from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import pytest
from time import sleep
#import pytest
#import allure

browser = webdriver.Chrome()

# @allure.epic("market-delivery")
# @allure.severity('normal')
# @allure.tittle("Заказ продуктов")
# @allure.description("Заказываем товары на онлайн платформе")
# @allure.feature('Тест 1')

#Авторизация на сайте доставки

def test_yandex_delivery_auth():
    #with allure.step("URL для авторизации"):
        browser.get = "https://passport.yandex.ru/auth/list"  
        click_button = browser.find_element(By.CSS_SELECTOR, 'href[class="AuthAccountListItem"]' )
        click_button.click()
        sleep(20)
        
    #with allure.step("Учетные данные для тестирования"):
       #payload = {
       # "username": "filinov@ymail.com",  
       # "password": "Qwertylas1902"   
    #}
    #with allure.step("Выполняем POST запрос для авторизации"):
       #response = requests.post(browser, json=payload)
    #with allure.step("Проверяем статус код для успешной авторизации"):
        #assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    #with allure.step("Проверяем наличие токена или информации о пользователе в ответе"):
       # data = response.json()
        #assert "token" in data, "Response does not contain authentication token"

#Выбор магазина из списка на сайте доставки 

# def test_get_store_list():
#     with allure.step("URL конечной точки для получения списка магазинов"):
#         url = "https://market-delivery.yandex.ru/web-api/seo-meta-tags?longitude=37.744810136380565&latitude=55.713863149339026&url=https%3A%2F%2Fmarket-delivery.yandex.ru%2Fretail%2Fpaterocka%3FplaceSlug%3Dpyaterochka_9f5p4&lang=ru&asset=desktop&serviceBrand=dc"  # Замените на актуальный путь к API
#     with allure.step("Выполняем GET запрос для получения списка магазинов"):
#         response = requests.get(url)
#     with allure.step("Проверяем статус код для успешного ответа"):
#         assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
#     with allure.step("Проверяем, что данные в ответе не пустые"):
#         data = response.json()
#         assert len(data) > 0, "Store list is empty"
#     with allure.step("Например, выбираем первый магазин для дальнейшего теста"):
#         store_id = data[0]['id']
#         assert store_id
#         return store_id

# def test_select_store():
#     with allure.step("Получаем ID магазина из предыдущего теста"):
#         store_id = test_get_store_list()  
#     with allure.step("URL конечной точки для выбора магазина"): 
#         select_store_url = f"https://market-delivery.yandex.ru/api/select_store/retail/moscow/paterocka?placeSlug=pyaterochka_gsqra"
#     with allure.step("Выполняем POST запрос для выбора магазина"):
#         response = requests.post(select_store_url)
#     with allure.step("Проверяем статус код для успешного выбора"):
#         assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
#     with allure.step("Дополнительная проверка наличия информации о выбранном магазине"):
#         data = response.json()
#         assert data['selected_store'] == store_id, "Selected store ID does not match" 

# #Ввод названия товара в строке поиска

# def test_product_search():
#     with allure.step("URL конечной точки для поиска товара"):
#         url = "https://market-delivery.yandex.ru/api/v1/menu/search"
#     with allure.step("Название товара для поиска"): 
#         query = "Огурец Global Village среднеплодный гладкий"  
#         params = {
#             "query": query,
# #             "count": 1  
# #     }
#     with allure.step("Выполняем GET запрос для поиска товара"):
#         response = requests.get(url, params=params)
#     with allure.step("Проверяем статус код для успешного ответа"):
#         assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
#     with allure.step("Проверяем, что данные в ответе корректные"):
#         data = response.json()
#     with allure.step("Проверяем наличие ключа 'value' в ответе"):
#         assert 'value' in data, "Response does not contain 'value' key"
#     with allure.step("Проверяем, что возвращается хотя бы один товар в списке"): 
#         assert len(data['value']) > 0, "No products found in the search results"

# def search_product(query):
#     with allure.step("URL конечной точки для поиска товара"):
#         url = "https://market-delivery.yandex.ru/api/v1/menu/search"  

#         params = {
#             "query": query,
#             "count": 10  
#     }
# #     with allure.step("Выполняем GET запрос для поиска товара"):
#         response = requests.get(url, params=params)
#     with allure.step("Проверяем статус код для успешного ответа"):
#         assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
#     with allure.step("Проверяем, что данные в ответе корректные"):
#         data = response.json()
#         assert 'value' in data, "Response does not contain 'value' key"
#         assert len(data['value']) > 0, "No products found in the search results"    
#         return data['value']

# #Выбор продукта из списка при поиске

# def test_select_product_from_search():
#     url = f"https://market-delivery.yandex.ru/api/v1/products/{'94246b3b-205e-40cd-a85a-31ba25012e6d'}"
#     query = "Огурец Global Village среднеплодный гладкий"  
#     products = search_product(query)
#     with allure.step("Выбираем первый продукт из списка"):
#         selected_product = products[0]
#         product_id = selected_product['id']
#         print(f"selected_product id: {'94246b3b-205e-40cd-a85a-31ba25012e6d'}")
#     with allure("Выполняем GET запрос для получения деталей продукта"):
#         response = requests.get(product_id)
#     with allure("Проверяем статус код для успешного ответа"):
#         assert response.status_code == 200
#     with allure.step("Проверяем, что данные в ответе логичны"):
#         details = response.json()
#         assert details['id'] == product_id
#         assert 'name'   
#         print('name')        

# #Название QWERTY в поле ввода при поиске товара  

# def test_search_product_qwerty():
#     with allure.step("URL конечной точки для поиска товара"):
#         url = "https://market-delivery.yandex.ru/api/v1/menu/search"  
#     with allure.step("Название товара для поиска"):
#         query = "QWERTY"
#         params = {

#             "query": query,
#             "count": 1 
#     }
#     with allure.step("Выполняем GET запрос для поиска товара"):
#         response = requests.get(url, params=params)
#     with allure.step("Проверяем статус код для успешного ответа"):
#         assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
#     with allure.step("Проверяем, что данные в ответе корректные"):
#         data = response.json()
#         assert 'products' in data, "Response does not contain 'products' key"
#         assert len(data['products']) > 0, "No products found in the search results"


