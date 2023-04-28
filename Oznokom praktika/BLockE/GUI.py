
from Parsing import *
from tkinter import *
import tkinter.ttk as ttk
import datetime


#изменение размера окна
def on_tab_selected(event):
    selected_tab = event.widget.nametowidget(event.widget.select())
    if selected_tab == tab2:
        window.geometry("450x250")
    elif selected_tab == tab1:
        window.geometry("450x150")

def btn_convertation():
    value1 = str(spisok_valut1.get())
    value2 = str(spisok_valut2.get())
    values = (value1,value2)
    #получить их рубелвое отношение 
    get_currency_val(values)
    print(get_currency_val(values))
    # #формула нахождения валюты из 1 в другую 

    # #вернуть в label_valut

    return 0

window = Tk() # при создании объекта класса Tk запускается итерпритарор базоваого окна приложения
window.title("Конвертер Валют")
window.geometry("450x150")


tab_control = ttk.Notebook(window) #Управление вкладками

###################### Первая вкладка ######################
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text = "Калькулятор валют")

#список валюты верх
now = datetime.datetime.now()
date_str = now.strftime("%d/%m/%Y")

spisok_valut1 = ttk.Combobox(tab1)
spisok_valut1["values"] = get_list_with_currency(date_str) #список валют
spisok_valut1.grid(column=0, row=0 , padx=10,pady=10)

#список валюты низ
spisok_valut2 = ttk.Combobox(tab1)
spisok_valut2["values"] = get_list_with_currency(date_str) # сюда надо залить список из валют
spisok_valut2.grid(column=0, row=1 , padx=10,pady=10)

#Окно ввода кол-ва валюты


vvod_valut = Entry(tab1)
vvod_valut.grid(column=1, row=0 , padx=10,pady=10)

#кнопка конвертировать 
btn_convertation = Button(tab1, text="Конвертировать" , command = btn_convertation)
btn_convertation.grid(column = 2, row = 0, padx=10,pady=10)

#вывод переведенной валюты
label_valut = Label(tab1 , text = "Переведенное")
label_valut.grid(column = 1 , row= 1 , padx=10,pady=10)










































###################### Вторая вкладка ######################
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text = "Динамика курса")
tab_control.add(tab2)

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

tab_control.bind("<<NotebookTabChanged>>", on_tab_selected) # изменение размер 
tab_control.pack(expand = True, fill = BOTH)


window.mainloop()#запуск
