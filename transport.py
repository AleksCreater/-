import time
import os

time_out = "Время аренды вышло"
transport_block = "Отправка запроса на блокировку транспорта"
transport_rental = {}
electric_scooter = ['KUGOO X1', 'Xiaomi M365 Electric Scooter Pro', 'Xiaomi Mi Electric Scooter 1S', 'Ninebot KickScooter' 'F25 Halten Flash']
bike = ['Adriatica' , 'AGang', 'Alpine Bike' ,'Altair' ,'Aspect']
tenant_name = input("Введите ФИО арендатора :")
choise = int(input("Выберите транспорт, который требуется сдать в аренду, введите 1 или 2: "))
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

print("Введите время, на которое взяли транспорт : ")
local_time = float(input())
local_time = local_time * 60
print(f"{transport_rental} взял на",  local_time, "секунд")

time.sleep(local_time)
print(time_out)

over_time = input("Требуется продление аренды? y/n ")
if over_time == 'y':
    print("Введите время в минутах , на которое был взят транспорт в аренду")
    local_time = float(input())
else:
    print(transport_block)
    time.sleep(3)
    print("Запрос отправлен, ожидаю ответ от устройства")
    with open('query_transport_locally.txt', 'w') as file:
        file.write('location of transport')
    time.sleep(3)
    #Имитация работы документооборота с транспортом. Имитация прочтения запроса сервером и его удаления
    os.remove('query_transport_locally.txt')
    print("Ожидние ответа")
    #Имитация документооборота получения ответа от транспорта. Получение файла
    time.sleep(3)
    file =  open('reply_transport_locally.txt', 'w')
    file.write('Ekaterinburg, Tatichewa, 24')
    file.close()
    print("Ответ получен", file.read()," транспорт остановлен и заблокирован")


            


