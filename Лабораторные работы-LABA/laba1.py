#Лабороторная работа 1

# 4. Считать  английский текст из файла и вывести на экран слова,
# начинающиеся с гласных букв.


def function_words_vowels(file_words):
    vowels_words = []
    vowels_letter = ['a', 'e', 'i', 'o', 'u' 'y']
    read_text = file_words.read()
    for w in read_text.split():
        word_strip = w.lower().strip('.,)!&?:')
        if word_strip[0] in vowels_letter:
            vowels_words.append(word_strip)
    len_vowels_words_no_repeat = len(set(vowels_words))
    len_vowels_words_repeat = len(vowels_words)
    differens = len_vowels_words_repeat - len_vowels_words_no_repeat
    print(f'Количество слов начинающихся с гласной буквы,без повторений:{len_vowels_words_no_repeat}')
    print(f'Количество слов начинающихся с гласной буквы,без повторений:{len_vowels_words_repeat}')
    print(f'{differens}-повторящихся слов')
    for key, value in enumerate(set(vowels_words)):
        print(key + 1, value)


if __name__ == '__main__':
    with open('../english_text.txt', 'r') as file:
        function_words_vowels(file)
        print(__name__)
