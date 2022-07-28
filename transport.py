import time
import os
import os.path


time_out = "Время аренды вышло"
transport_block = "Отправка запроса на блокировку транспорта"

requests = True
while requests == True:
    transport_rental = {}
    electric_scooter = ['KUGOO X1', 'Xiaomi M365 Electric Scooter Pro', 'Xiaomi Mi Electric Scooter 1S', 'Ninebot KickScooter' 'F25 Halten Flash']
    bike = ['Adriatica' , 'AGang', 'Alpine Bike' ,'Altair' ,'Aspect']
    tenant_name = input("Введите ФИО арендатора :")
    choise = int(input("Выберите транспорт, который требуется сдать в аренду, введите 1(скутеры) или 2(велосипеды): "))
    if choise == 1:
        print(" В наличии доступны скутеры :", '\n' , electric_scooter, '\n')
        choise_model = int(input("Укажите модель, которую выбрал арендатор : "))
        if choise_model == 1:
            current_model = electric_scooter.pop(0)
            transport_rental[tenant_name] = current_model
            print(f"{tenant_name} выбрал скутер", current_model)
        elif choise_model == 2:
            current_model = electric_scooter.pop(1)
            transport_rental[tenant_name] = current_model
            print(f"{tenant_name} выбрал скутер", current_model)
        elif choise_model == 3:
            current_model = electric_scooter.pop(2)
            transport_rental[tenant_name] = current_model
            print(f"{tenant_name} выбрал скутер", current_model)
        elif choise_model == 4:
            current_model = electric_scooter.pop(3)
            transport_rental[tenant_name] = current_model
            print(f"{tenant_name} выбрал скутер", current_model)
        elif choise_model == 5:
            current_model = electric_scooter.pop(4)
            transport_rental[tenant_name] = current_model
            print(f"{tenant_name} выбрал скутер", current_model)
    else:
        print("Введено некорректное значение")
        break
        
    if choise == 2:
        print("В наличии доступны велосипеды: ", '\n', bike,'\n')
        choise_model = int(input("Укажите модель, которую выбрал арендатор : "))
        if choise_model == 1:
            current_model = bike.pop(0)
            transport_rental[tenant_name] = current_model
            print(f"{tenant_name} выбрал велосипед", current_model)
        elif choise_model == 2:
            current_model = bike.pop(1)
            transport_rental[tenant_name] = current_model
            print(f"{tenant_name} выбрал велосипед", current_model)
        elif choise_model == 3:
            current_model = bike.pop(2)
            transport_rental[tenant_name] = current_model
            print(f"{tenant_name} выбрал велосипед", current_model)
        elif choise_model == 4:
            current_model = bike.pop(3)
            transport_rental[tenant_name] = current_model
            print(f"{tenant_name} выбрал велосипед", current_model)
        elif choise_model == 5:
            current_model = bike.pop(4)
            transport_rental[tenant_name] = current_model
            print(f"{tenant_name} выбрал велосипед", current_model)
        else:
            print("Введено некорректное значение")
            break

    print("Введите время, на которое взяли транспорт : ")
    local_time = float(input())
    local_time = local_time * 60
    print(f"{transport_rental} взял на",  local_time, "секунд")
    time.sleep(3)
    print('Отправляю запрос на разблокировку транспорта')
    with open('request_for_transport_unlocking.txt','w+')as file:
        file.write('request for transport unlocking')

    time.sleep(3)
    try:
        file_path = os.path.exists('answer_unblocking_transport.txt')
        if file_path == True:
            file = open('answer_unblocking_transport.txt')
            content = file.read()
            print(content)
            file.close()
            os.remove('answer_unblocking_transport.txt')
            break
        else:
            print("Ответный Файл не найден, ожидаю")
            print("Проверьте связь с транспортом")
            requests == False
            time.sleep(30)
    except FileNotFoundError:
        print("Проверьте связь с транспортом")
    time.sleep(local_time)
    print(time_out)

    over_time = input("Требуется продление аренды? y/n ")
    if over_time == 'y':
        print("Введите время в минутах , на которое был взят транспорт в аренду")
        local_time = float(input())
        print(f"{transport_rental} взял на",  local_time, "секунд")
    else:
        print(transport_block)
        time.sleep(3)
        print("Запрос отправлен, ожидаю ответ от устройства")
        with open('request_for_transport_location.txt', 'w+') as file:
            file.write('location of transport')
        time.sleep(3)
        print("Ожидние ответа")
        time.sleep(3)
    file =  open('answer_for_ransport_location.txt')
    content = file.read()
    print("Ответ получен", content," транспорт остановлен и заблокирован")
    file.close()
    os.remove('answer_for_ransport_location.txt')

input()

            


