from tkinter import *
import tkinter.ttk as ttk
import urllib.request
import xml.dom.minidom
import xml.etree.ElementTree as ET
import datetime

class Window:
    def __init__(self):
        self.window = Tk() # при создании объекта класса Tk запускается итерпритарор базоваого окна приложения
        self.window.title("Конвертер Валют")
        self.window.geometry("450x150")
        self.tab_control = ttk.Notebook(self.window) #Управление вкладками

class Tab1(Window):            
    def __init__(self):
        super().__init__()
        self.tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab, text = "Калькулятор валют")

        #список валюты верх
        self.spisok_valut1 = ttk.Combobox(self.tab)
        self.spisok_valut1["values"] = get_list_with_currency() #список валют
        self.spisok_valut1.grid(column=0, row=0 , padx=10,pady=10)

        #список валюты низ
        self.spisok_valut2 = ttk.Combobox(self.tab)
        self.spisok_valut2["values"] = get_list_with_currency() # сюда надо залить список из валют
        self.spisok_valut2.grid(column=0, row=1 , padx=10,pady=10)

        #Окно ввода кол-ва валюты

        vvod_valut = Entry(self.tab)
        vvod_valut.grid(column=1, row=0 , padx=10,pady=10)

        #кнопка конвертировать 
        btn_convertation = Button(self.tab, text="Конвертировать", command = self.btn_convertation_func )
        btn_convertation.grid(column = 2, row = 0, padx=10,pady=10)

        #вывод переведенной валюты
        label_valut = Label(self.tab , text = "Переведенное")
        label_valut.grid(column = 1 , row= 1 , padx=10,pady=10)
    
    def btn_convertation_func(self):
        value1 = str(self.spisok_valut1.get())
        value2 = str(self.spisok_valut2.get())
        #получить их рублевые значения 
        value1 = self.get_currency_val(value1)
        value2 = self.get_currency_val(value2)
        # #формула нахождения валюты из 1 в другую 

        # #вернуть в label_valut
    def get_currency_val(currency_name, self) :

    # получаем текущую дату
        currency_name = str(currency_name)
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
            if name == self:
                value_str = valute.find('Value').text.replace(',', '.')
                print (value_str)
                return float(value_str)
        # если валюта не найдена, возвращаем None
        return None


class Tab2(Tab1):
    def __init__(self):
        super().__init__()
        tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(tab2, text = "Динамика курса")

        #label Валюта
        currency_label = ttk.Label(tab2, text="Валюта")
        currency_label.grid(column=0, row=0, padx=10, pady=10)

        #Выбор самой валюты список
        currency_list = ttk.Combobox(tab2, values=["Евро", "Доллар"])
        currency_list.grid(column=0, row=1, padx=10, pady=10)

        #Кнопка построить график
        build_button = ttk.Button(tab2, text="Построить график")
        build_button.grid(column=0, row=4, padx=10, pady=10)

        #label Период
        period_label = ttk.Label(tab2, text="Период")
        period_label.grid(column=1, row=0, padx=10, pady=10)

        #Radiobutton Неделя, Месяц, Квартал, Год 

        #значение неделя(0) , месяц(1) , квартал(2) , год(4)
        period_var = IntVar()
        period_var.set(0)


        radiobutton_week = ttk.Radiobutton(tab2, text="Неделя" , variable = period_var , value = 0)
        radiobutton_week.grid(column=1, row=1, padx=10, pady=10)

        radiobutton_month = ttk.Radiobutton(tab2, text="Месяц", variable = period_var, value = 1)
        radiobutton_month.grid(column=1, row=2, padx=10, pady=10)

        radiobutton_quarter = ttk.Radiobutton(tab2, text="Квартал", variable = period_var, value = 2)
        radiobutton_quarter.grid(column=1, row=3, padx=10, pady=10)

        radiobutton_year = ttk.Radiobutton(tab2, text="Год", variable = period_var, value = 3)
        radiobutton_year.grid(column=1, row=4, padx=10, pady=10)


        #label Выбор периода
        period_label = ttk.Label(tab2, text="Выбор периода")
        period_label.grid(column=2, row=0, padx=10, pady=10)

        #combobox выбора периода (для недели месяца квартала и года сделать свои value)
        period_list = ttk.Combobox(tab2, values=["2020", "2019"])
        period_list.grid(column=2, row=4, padx=10, pady=10)
        self.tab_control.pack(expand = True, fill = BOTH)
        self.window.mainloop()#запуск
 

def get_list_with_currency():
            #date = "06/01/2023" #самая первая рабочая дата 06/01/1993
            now = datetime.datetime.now()
            date_str = now.strftime("%d/%m/%Y")
            url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_str}"
            response = urllib.request.urlopen(url)
            dom = xml.dom.minidom.parse(response) #получение DOM (файл как дерево тегов) структуры файла
            dom.normalize()
            nodeArray = dom.getElementsByTagName("Valute")  #получение элементов с этим тегом
            result_list = []
            for node in nodeArray:
                name = node.getElementsByTagName("Name")[0].childNodes[0].nodeValue
                result_list += [name]
            return result_list






if __name__ == '__main__':
    Tab2()