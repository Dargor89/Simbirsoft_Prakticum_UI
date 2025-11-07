import random
from faker import Faker

fake = Faker()

"""Генерируем случайные 10 чисел"""
def generate_post_code():
    post_code = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    return post_code

"""Преобразуем числа в буквы для first_name"""
def generate_name_from_post_code(post_code):
    # Разбиваем на двузначные числа
    digits = [int(post_code[i:i+2]) for i in range(0, 10, 2)]
    # Преобразуем в буквы (a-z)
    name = ''.join([chr((digit % 26) + 97) for digit in digits])
    return name

def generate_last_name():
    return fake.last_name() #Случайно сгенерированная фамилия