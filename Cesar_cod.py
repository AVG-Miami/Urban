const_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Прописные буквы
const_lower = 'abcdefghijklmnopqrstuvwxyz' # Строчные буквы
symbols=',.!"?:;\''
phrase_list = []
lenght_word = []
new_phrase =''

def find_word(phrase):
    global phrase_list
    word = ''
    word_2 = ''
    for i in phrase:
        if i == " ":
            phrase_list.append(word)
            lenght_word.append(len(word_2))
            word = ''
            word_2 = ''
            phrase_list.append(' ')
            lenght_word.append(0)
        else:
            word += i
            if i not in symbols:
                word_2 += i
    phrase_list.append(word)
    lenght_word.append(len(word_2))
# 'Day, mice. "Year" is a mistake!'
#  D—>G a—>d y—>b | (к индексу буквы D + длина слова этой буквы—>( 3+3 ))
# Output: 'Gdb, qmgi. "Ciev" ku b tpzahrl!'

def code_phrase():
    for i in range(len(phrase_list)):
        lenght_word_item = lenght_word [i]
        new_word=''
        for sym in phrase_list[i]:
            if sym in const_upper:
                # Смещаем позицию символа с строке на длинну слова
                pos = const_upper.index(sym)
                if (pos + lenght_word_item) >= len(const_upper): # Если смещение больше длинны набора символов то перемещаем на начало 
                    sym = const_upper[pos + lenght_word_item - len(const_upper)]
                else:
                    sym = const_upper[pos + lenght_word_item]
            if sym in const_lower:
                pos = const_lower.index(sym)
                if pos + lenght_word_item >= len(const_lower):
                    sym = const_lower[pos + lenght_word_item - len(const_lower)]
                else:
                    sym = const_lower[pos + lenght_word_item]
            new_word +=sym
        phrase_list[i] = new_word




phrase = input('Ведите фразу на английском языке:')

# Определяем слова их длину и заносим в список, не буквы учитываем с длинной 0
find_word(phrase)


print("Список слов разделенных пробелами", phrase_list)
print("Список длин слов (только буквы)", lenght_word)

# Кодируем символы
code_phrase()

print("Список кодированных слов", phrase_list)

for i in phrase_list:
    new_phrase += i

print("Старая строка       :", phrase)
print("Закодированая строка:", new_phrase)
