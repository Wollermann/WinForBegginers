import os
from unidecode import unidecode

#Получаем имя пользователя для непосредственной работы с директориями пользователя
user = os.getlogin()
dirs = [f'C:/Users/{user}/Desktop/', 'C:/Users/Public/Desktop/']

#Основной цикл
while True:
    request = input('Введите команду: ')

    #Команда 'Открой'
    if request[0:request.find(' ')].lower() == 'открой':
        prog1 = request[request.find(' ') + 1:]
        prog2 = unidecode(request[request.find(' ') + 1:])
        #Проверяем в каждой директории
        for dir in dirs:
            #Находим расширение файла
            for obj in os.listdir(dir):
                if os.path.splitext(obj)[0] == prog1 or os.path.splitext(obj)[0] == prog2:
                    exp = os.path.splitext(obj)[1]
                    break
            #Запускаем, если файл существует. ТРЕБУЕТ БОЛЬШОЙ ОПТИМИЗАЦИИ
            if f'{prog1}{exp}' in os.listdir(dir) or f'{prog2}{exp}' in os.listdir(dir):
                try:
                    os.startfile(f'{dir}{prog1}{exp}')
                except:
                    os.startfile(f'{dir}{prog2}{exp}')
                break


    #Команда 'Помощь' (по командам бота)
    elif request.lower() == 'помощь':
            pass








    else:
        print('Неизвестная команда')
