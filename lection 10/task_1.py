# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string

def generate_random_name():
    """
    Генератор двух случайных слов из латинских букв
    """
    while True:
        len_word1 = random.randint(1, 15)
        len_word2 = random.randint(1, 15)

        word1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_word1))
        word2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_word2))

        yield f"{word1} {word2}"

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
