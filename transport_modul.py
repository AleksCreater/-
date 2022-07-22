import time
import os
import os.path

def unblocking_transport():
    try:
        file_path = os.path.exists('request_for_transport_unlocking.txt')
        if file_path == True:
            file = open('request_for_transport_unlocking.txt')
            content = file.read()
            print(content)
            file.close()
            os.remove('request_for_transport_unlocking.txt')
            with open('answer_unblocking_transport.txt','w+') as file:
                file.write('Транспорт разблокирован')
    except FileNotFoundError:
        print("Ответный Файл не найден, ожидаю")

def transport_location():
    file_path_1 = os.path.exists('request_for_transport_location.txt')
    if file_path_1 == True:
        file = open('request_for_transport_location.txt')
        content = file.read()
        print(content)
        file.close()
        os.remove('request_for_transport_location.txt')
        with open('answer_for_ransport_location.txt', 'w+') as file:
            file.write('Текущие координаты')
        

monitoring = True
while monitoring == True:
    unblocking_transport()
    transport_location()



input()
    



    

