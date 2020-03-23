import os
from unidecode import unidecode
import webbrowser

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

    #команда "горячие клавиши"
    elif request[:request.find(' ')].lower() == "горячие":
        print("Список горячих клавиш для Windows 10: ",
            "ctrl + C - скопировать текст",
            "ctrl + V - вставить скопированный текст",
            "ctrl + shift + esc - диспетчер задач",
            'win + R - служба "Выполнить"',
            "win + I - открывает окно параметров",
            "alt + enter - свойства выбронного элемента",
            "Больше информации вы можете узнать тут: https://g-ek.com/sochetaniya-klavish-dlya-kalkulyatora-v-windows-10",
            sep="\n")

    #команда для открытия веб-страниц(браузер=default)
    elif request.lower() == "открой сайт":
        url = input("Укажите адрес страницы: ")
        webbrowser.open(url)

    #команда для поиска в интернете(браузер=default)
    elif request[:request.find(' ')].lower() == "поиск":
        webbrowser.open("https://www.google.ru/")

    #Команда 'Помощь' (по командам бота)
    elif request.lower() == 'помощь':
            pass








    else:
        print('Неизвестная команда')
