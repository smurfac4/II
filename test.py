# import traceback
# def anagram_difference(words):
#      total_diff = 0
#      for char in set(''.join(words)): # проходимся по каждому уникальному символу всех слов
#          char_count = [word.count(char) for word in words] #количество вхождений символа в каждом слове
#          total_diff += sum([abs(count - sum(char_count) // len(words)) for count in char_count]) #количество изменений, необходимых для того, чтобы превратить все слова в анаграммы.
#      return total_diff

# print(anagram_difference(["abc", "ab", "a"]))
# print(anagram_difference(["mouse", "house", "hose", "host"]))


A = ["abc", "ab", "a"]
print(len(A))