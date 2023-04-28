
from tkinter import *
import tkinter.ttk as ttk
import urllib.request
import xml.dom.minidom
import xml.etree.ElementTree as ET
import datetime

def get_currency_val(currency_name) :
    # получаем текущую дату
        now = datetime.datetime.now()
        date_str = now.strftime("%d/%m/%Y")
        # формируем URL для запроса
        url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_str}"
        # отправляем GET-запрос
        response = urllib.request.urlopen(url)
        # парсим XML-документ
        tree = ET.parse(response)
        # получаем корневой элемент дерева
        root = tree.getroot()
        # итерируемся по всем элементам <Valute> и ищем нужную валюту
        for valute in root.iter('Valute'):
            name = valute.find('Name').text
            value_str = valute.find('Value').text.replace(',', '.')
            if name == currency_name:
                print (value_str)
                return value_str
        # если валюта не найдена, возвращаем None
        return None

get_currency_val('Фунт стерлингов Соединенного королевства')