import sys, os, time, datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'connection'))
from connect import *

# Функции для выполнения действий в Minecraft
def set_time(time):
    mc.postToChat(f"Установка времени суток: {time}")
    if time == "Утро":
        mc.setBlock(0, 0, 0, 6)  # Используйте блок с идентификатором 6 для установки утра
    elif time == "Вечер":
        mc.setBlock(0, 0, 0, 4)  # Используйте блок с идентификатором 4 для установки вечера
    elif time == "Ночь":
        mc.setBlock(0, 0, 0, 14)  # Используйте блок с идентификатором 14 для установки ночи
    else:
        print("Неверное время суток.")

def activate_rain():
    mc.postToChat("Активация дождя")
    mc.setRain(1)

def activate_storm():
    mc.postToChat("Активация шторма")
    mc.setRain(1)
    mc.setThunder(1)

# Главное меню
def main_menu():
    while True:
        print("\nВыберите действие:")
        print("1. Установить время суток 'Утро'")
        print("2. Установить время суток 'Вечер'")
        print("3. Установить время суток 'Ночь'")
        print("4. Активировать дождь")
        print("5. Активировать шторм")
        print("6. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == "1":
            set_time("Утро")
        elif choice == "2":
            set_time("Вечер")
        elif choice == "3":
            set_time("Ночь")
        elif choice == "4":
            activate_rain()
        elif choice == "5":
            activate_storm()
        elif choice == "6":
            break
        else:
            print("Неверный номер действия. Попробуйте еще раз.")

    print("Программа завершена.")

# Главная логика программы
if __name__ == "__main__":
    main_menu()
