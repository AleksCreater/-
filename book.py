import time

book = []
reader = []

book_name = input("Введите название книги : ")
reader_name = input("Введите фамилию я имя читателя : ")
over = "Необходимо уточнить, требуется ли продлить прокат книги "

print("Укажите время, насколько взяли книгу : ")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)

print(over)


book.append(book_name)
reader.append(reader_name)
