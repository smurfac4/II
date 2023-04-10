import random
import time

def binary_search(data, elem):
    count = 0

    low = 0 #левый индекс
    high = len(data) - 1 #правый индекс

    while low <= high: #пока левый индекс = правый индекс
      
        middle = (low + high)//2 #обозначим середину
        count += 1
        if data[middle] == elem: # если элемент по середине , то это то что мы ищем 
            return middle , count 
        elif data[middle] > elem: #иначе если элемент > искомого переходим в правую часть
            high = middle - 1
        else:
            low = middle + 1 #иначе если элемент < искомого переходим в левую часть 

    return -1 , count #если не нашел возврат -1

# Получение размера массива от пользователя
n = int(input("Введите размер массива: "))

# Создание массива и заполнение его псевдослучайными числами
arr = []
for i in range(n):
    arr.append(random.randint(1, 100000))

# Сортировка массива
arr.sort()

# Вывод отсортированного массива
print("Отсортированный массив:", arr)

# Получение ключа от пользователя
x = int(input("Введите ключ для поиска: "))

# Поиск элемента в массиве и вывод результата

start_time = time.time() # Запускаем таймер для замера времени работы сортировки
index, count = binary_search(arr, x)
end_time = time.time() # Останавливаем таймер

if index == -1:
    print("Элемент не найден")
else:
    print("Элемент найден в позиции", index)
print("Количество операций сравнения:", count)
print("Время работы поиска:", end_time - start_time)