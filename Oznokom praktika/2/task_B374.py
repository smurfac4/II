# Написать функцию anagram_difference, на вход которой дан список слов и которая
# определяет сколько всего букв нужно удалить из всех слов, чтобы они все являлись
# анаграммами (каждое слово получалось перестановкой букв другого)
#
# Пример:
# anagram_difference["hello", "hola", "allo"] ==> 7 (["lo", "ol", "lo"]

import traceback


def anagram_difference(words):
    # Тело функции
    return 0


# Тесты
try:
    assert anagram_difference(["abc", "ab", "a"]) == 3
    assert anagram_difference(["hello", "hola", "allo"]) == 7
    assert anagram_difference(["cat", "dog", "mouse"]) == 11
    assert anagram_difference(["mouse", "house", "hose", "host"]) == 10
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
