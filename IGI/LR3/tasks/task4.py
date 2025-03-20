"""
Выполнил Малиновский Илья, группа 353502
Вариант 19
Задание 4
Подсчёт количества слов, начинающихся или заканчивающихся
на гласную букву, в тексте. Нахождение количества каждого
символа в тексте. Вывод в алфавитном порядке слов, идущих
после запятой.
11.02.2025
"""


def is_vowel(char):
    """Проверяет, является ли символ гласной буквой"""
    return char in "aeiouyAEIOUY"


def split_words(text):
    """Разбивает текст на слова по пробелам и запятым"""
    words = []
    word = ""
    for char in text:
        if char.isalpha() or char == "-":
            word += char
        elif word:
            words.append(word)
            word = ""
    if word:
        words.append(word)
    return words


def count_vowel_words(words):
    """Считает слова, начинающиеся или заканчивающиеся на гласную"""
    count = 0
    for word in words:
        if is_vowel(word[0]) or is_vowel(word[-1]):
            count += 1
    return count


def count_character_frequencies(text):
    """Считает частоту каждого символа в тексте"""
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq


def get_words_after_comma(text):
    """Возвращает слова после запятых, в алфавитном порядке"""
    parts = text.split(",")
    words_after_comma = []

    for part in parts[1:]:
        word = ""
        for char in part:
            if char.isalpha() or char == '-':
                word += char
            else:
                if word:
                    break
        if word:
            words_after_comma.append(word)

    return sorted(words_after_comma)


def task_4():
    text = (
        "So she was considering in her own mind, as well as she could, "
        "for the hot day made her feel very sleepy and stupid, "
        "whether the pleasure of making a daisy-chain would be worth the "
        "trouble of getting up and picking the daisies, when suddenly a "
        "White Rabbit with pink eyes ran close by her."
    )
    words = split_words(text)
    vowel_word_count = count_vowel_words(words)
    char_frequencies = count_character_frequencies(text)
    sorted_words_after_comma = get_words_after_comma(text)

    print(
        "Число слов, начинающихся или заканчивающихся на гласную: "
        f"{vowel_word_count}"
    )
    print("Частота символов:")
    for char, count in sorted(char_frequencies.items()):
        print(f"'{char}': {count}")
    print(
        "Слова после запятой в алфавитном порядке: :"
        f"{sorted_words_after_comma}"
    )
