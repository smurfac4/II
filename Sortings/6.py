def find_substring(s: str, p: str):
    n, m = len(s), len(p)
    cmp_count, shift_count = 0, 0
    print (f"Количество символов в тексте(с пробелами):{len(s)}")
    for i in range(n):
        j = 0 #сброс счетчика до 0
        cmp_count += 1 # +1 сравнение
        while j < m and s[i+j] == p[j]:
            j += 1
            cmp_count += 1 # +1 сравнение
        shift_count += 1 # +1 сдвиг 
        if j == m:
            print(f"Количество операций посимвольного сравнения: {cmp_count}")
            print(f"Количество сдвигов подстроки: {shift_count}")
            return i
    print(f"Количество операций посимвольного сравнения: {cmp_count}")
    print(f"Количество сдвигов подстроки: {shift_count}")
    print(f"Всего: {shift_count+cmp_count}")
    return -1

with open("file1.txt", "r", encoding="utf-8") as f:
    text = f.read()
    pattern = str(input("Введите текст: "))
    index = find_substring(text, pattern)
    if index != -1:
        print(f"Подстрока найдена в позиции {index}")
    else:
        print("Подстрока не найдена")