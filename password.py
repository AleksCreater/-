import random
import string
import time

def generation_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    print(rand_string)

print("Генерирую пароль... ")
time.sleep(3)
print("Почти готово... ")
time.sleep(3)
print("Ваш пароль... ")
time.sleep(3)
generation_random_string(16)
input("Нажмите ENTER чтобы выйти : ")
    
    
