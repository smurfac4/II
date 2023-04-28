import urllib.request
import xml.dom.minidom
import datetime

#получение названия валют на определенный день
def get_list_with_currency(date):
    #date = "06/01/2023" #самая первая рабочая дата 06/01/1993
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}"
    response = urllib.request.urlopen(url)
    dom = xml.dom.minidom.parse(response) #получение DOM (файл как дерево тегов) структуры файла
    dom.normalize()
    nodeArray = dom.getElementsByTagName("Valute")  #получение элементов с этим тегом
    
    result_list = []
    for node in nodeArray:
        name = node.getElementsByTagName("Name")[0].childNodes[0].nodeValue
        result_list += [name] 
    return result_list

    # childList = node.childNodes # получение дочерних элементов
    # for child in childList:
    #     print(child.nodeName) #имя узла
    #     print(child.childNodes[0].nodeValue) #получение значения узла

def btn_convertation():
    value1 = str(spisok_valut1.get())
    value2 = str(spisok_valut2.get())
    values = [value1,value2]
    #получить их рубелвое отношение 
    get_currency_val(values)
    print(get_currency_val(values))
    # #формула нахождения валюты из 1 в другую 

    # #вернуть в label_valut


def get_currency_val(names):
    print (names)
    now = datetime.datetime.now()
    date_str = now.strftime("%d/%m/%Y")
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_str}"
    response = urllib.request.urlopen(url)
    dom = xml.dom.minidom.parse(response) #получение DOM (файл как дерево тегов) структуры файла
    dom.normalize()

    valutes = dom.getElementsByTagName('Valute')
    for valute in valutes:
        name = valute.getElementsByTagName("Name")[0].childNodes[0].nodeValue
        value = valute.getElementsByTagName("Value")[0].childNodes[0].nodeValue
        if name == names:
            print(f"Значение {name} равно {value}")
            return value