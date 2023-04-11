"""
Создать производный от Item класс Food. Новые поля: масса блюда, время приготовления, состав блюда (список
    ингредиентов). Определить конструктор, с вызовом родительского конструктора. Определить функции изменения
    времени приготовления, добавления, удаления и изменения списка ингредиентов. Переопределить метод
    преобразования в строку для печати основной информации (название, масса, цена, время приготовления).

"""


from Item import Item

class Food(Item): #производный класс от Item
    def __init__(self, name, price, weight, preparation_time, ingredients = {}):
        super().__init__(name, price) #наследование из родительского класса name и price
        self.weight = weight #масса блюда
        self.preparation_time = preparation_time #время приготовления
        self.ingredients = ingredients # состав блюда

    def change_preparation_time(self, new_time): # меняем время приготовления
        self.preparation_time = new_time

    def add_ingredient(self, name : str , weight : int): #добавляем ингридиент 
        if name is self.ingredients:
            self.ingredients[name] += weight
        else:
            self.ingredients[name] = weight

    def remove_ingredient(self, name, weight = None): #удалить ингредиент 
        if name in self.ingredients: #eсли этот ингридент существует
            if weight == None: #если в параметр ничего не передали уничтожает
                del self.ingredients[name]
            elif self.ingredients[name] <= weight: # если кол-во ингр. <= кол-ву удалений
                del self.ingredients[name] # удаляем ингридиент
            else:
                self.ingredients[name] -= weight #удаляем кол-во ингредиентов

    def change_ingredient(self, old_name, new_name): #меняет название ингредиента
        if old_name in self.ingredients: #если он есть 
            self.ingredients[new_name] = self.ingredients.pop(old_name)

    def print_ingredients(self): #напечатать все ингредиенты 
        print("Ингредиенты:")
        for name, numbers in self.ingredients.items():
            print(f"{name}: {numbers} грамм")

    def __str__(self): #вывод
        return f"{self.name} - {self.weight} грамм - {self.price:.2f} Р - {self.preparation_time} сек"
    
    def change_all(self,name: str, price: int, weight: int, preparation_time: int, ingredients: dict ):
        self.name = name #имя
        self.price = price #цена
        self.weight = weight #масса блюда
        self.preparation_time = preparation_time #время приготовления
        self.ingredients = ingredients # состав блюда
