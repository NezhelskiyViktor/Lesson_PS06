import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


# Инициализируем браузер
driver = webdriver.Chrome()


# В отдельной переменной указываем сайт, который будем просматривать
url = "https://www.divan.ru/category/podvesnye-svetilniki"
driver.get(url)   # Открываем веб-страницу
time.sleep(10)   # Задаём 10 секунд ожидания, чтобы веб-страница успела прогрузиться

# Находим все карточки товаров с помощью названия класса
electrical_goods = driver.find_elements(By.CSS_SELECTOR, "div.lsooF")  # Названия классов берём с кода сайта

electrical_goods_data = []   # Создаём список, в который потом всё будет сохраняться
# Перебираем коллекцию товаров
for good in electrical_goods:
   try:
       name = good.find_element(By.CSS_SELECTOR, "a.ui-GPFV8.qUioe.ProductName.ActiveProduct span[itemprop='name']").text
   except:
       print("произошла ошибка при парсинге name")
   try:
       price = good.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute("content")
   except:
       print("произошла ошибка при парсинге price")
   try:
       link = good.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute("href")
   except:
       print("произошла ошибка при парсинге url")

   # Вносим найденную информацию в список
   electrical_goods_data.append([name, price, link])

# Закрываем подключение браузер
driver.quit()
# Прописываем открытие нового файла, задаём ему название и форматирование
with open("hh.csv", 'w',newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    writer = csv.writer(file)
    # Создаём заголовок таблицы
    writer.writerow(['Название товара', 'Цена', 'Ссылка на карточку товара'])
    # Прописываем использование списка как источник для записи таблицы
    writer.writerows(electrical_goods_data)

