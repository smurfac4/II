"""

Создать класс Menu. Поля: название ресторана, адрес, список экземпляров класса Drink, список экземпляров класса Food. Определить конструктор. Переопределить метод преобразования
    в строку для печати всей информации о меню (с использованием переопределения в классах Drink и Food).
    Переопределить методы получения количества пунктов меню функцией len, получения напитка/блюда по индексу,
    изменения по индексу, удаления по индексу (пусть вначале идут индексы напитков, затем горячих блюд).
    Переопределить операции + и - для добавления или удаления пункта меню. Добавить функцию создания txt-файла
    и записи всей информации в него (в том числе списков ингредиентов напитков и блюд).

"""

from Drink import Drink
from Food import Food


class Menu(Drink,Food):
    #конструктор класса
    def __init__(self, restaurant_name: str, address: str, drinks: list, foods: list):
        self.restaurant_name = restaurant_name
        self.address = address
        self.drinks = drinks
        self.foods = foods

    #вывод информации о ресторане
    def __str__(self):
        menu_str = f"\nРесторан: {self.restaurant_name}\nАдрес: {self.address}\n\nНапитки:\n"
        for i in self.drinks:
            menu_str += f"{self.drinks.index(i)+1} {Drink.vivod(i)} \n"
        menu_str += "\nБлюда:\n"
        for i in self.foods:
            menu_str += f"{self.foods.index(i)+1+len(self.drinks)} {Food.vivod(i)} \n"
        return menu_str

    #Вывод количества позициЙ меню
    def __len__(self):
        return len(self.drinks) + len(self.foods)

    #получение объекта по индексу
    def get_index(self, index: int):
        index -= 1
        if  0 <= index < len(self.drinks):
            return print(f"{index+1} {Drink.vivod(self.drinks[index])}")
        elif 0 <= index < len(self.drinks) + len(self.foods): 
            return print(f"{index+1} {Food.vivod(self.foods[index - len(self.drinks)])}")
        else:
            return None
        
    def change_by_index(self, index: int ,name , price, volume, menu_category_preparation_time, ingredients):
        index -= 1
        if  0 <= index < len(self.drinks): # Если напиток
            return Drink.change_all(self.drinks[index],name,price,volume,menu_category_preparation_time,ingredients)
        elif 0 <= index < len(self.drinks) + len(self.foods):   #если еда
            return Food.change_all(self.foods[index - len(self.drinks)] ,name, price, volume, menu_category_preparation_time, ingredients)
        else:
            return None
        
    #Удалить по индексу
    def remove_obj(self, index):
        index -= 1
        if  0 <= index < len(self.drinks): # Если напиток
            del self.drinks[index]
        elif 0 <= index < len(self.drinks) + len(self.foods): #если еда
            del self.foods[index - len(self.drinks)]
        else:
            return None

    def __add__(self, item): # +=
        if isinstance(item, Drink):
            self.drinks.append(item)
        elif isinstance(item, Food):
            self.foods.append(item)
        else:
            raise TypeError("Меню можно пополнить только напитками или блюдами")
        return self

    def __sub__(self, item): # -= 
        if isinstance(item, Drink):
            self.drinks.remove(item)
        elif isinstance(item, Food):
            self.foods.remove(item)
        else:
            raise TypeError("Из меню можно удалить только напитки или блюда")
        return self

    def save_to_file(self, file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"Ресторан: {self.restaurant_name}\nАдрес: {self.address}\n\n")
            f.write("Напитки:\n")
            for drink in self.drinks:
                f.write(f"{self.drinks.index(drink)+1} {Drink.vivod(drink)} \n")
            f.write("\nБлюда:\n")
            for food in self.foods:
                f.write(f"{self.foods.index(food)+1+len(self.drinks)} {Food.vivod(food)} \n")