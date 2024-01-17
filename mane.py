text = input("Введите текст: ")  # запрашиваю у пользователя текст
text = text.lower()  # перевожу текст в нижний регистр
punctuation = [".", ",", "!", "?"]  # список знаков препинания
for i in punctuation: # перебираем список
    if i in text: # проверяем знаки препинания в тексте
        text = text.replace( i,"") # заменили 1 из знаков препинания на пустое место
words = text.split()  # обработанный список слов
print("words=")
print(words)
print(".")
word_frequency = {}  # пустой словарь
for i in words: # перебераем элементы списка
    if i in word_frequency: # проверяем есть ли в словаре word_frequency слово i из списка words
        word_frequency [i] += 1 # если условие верно (слово i есть в словаре word_frequency), то увеличиваем значение частоты для слова i на 1
    else:   # если условие неверно (слово i нету в словаре  word_frequency)
        word_frequency[i] = 1 # добавляем слово i в словарь (word_frequency) и присваеваем значение частоты для слова i (word_frequency[i]) в 1
print("Частота слов:") # выводится "частота слов"
for word, frequency in word_frequency.items(): # разбиваем слово на ключ и значение, разбиваем словарь на элементы (на ключ и значение) ключ-это слово из списка words
    print(f"{word}: {frequency}") # выводит ключ и значение
print("Количество разных слов:",len(set(words))) # считаем сколько уникальных слов ввёл пользователь и выводим их
