text = input("Введите текст: ")
text = text.lower()
for t in ["!", "?", ",", "."]:
    text = text.replace(t, "")
print(text)


wl = text.split()


ue = set(wl)


ce = len(ue)

print("Количество уникальных слов:", ce)

word_frequency = {




}



for x in text.split():
    if x in word_frequency:
        word_frequency[x] +=1
    else:
        word_frequency[x] = 1
print(word_frequency)

