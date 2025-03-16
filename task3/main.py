# from pathlib import Path
# dir = Path(__file__).parent

import sys
import os
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True) # дозволяє автоматично скинути кольори після кожного використання

def print_directory_structure(directory_path, indent=0):
    '''Функція для рекурсивного обходу директорії та виведення її структури'''
    try:
        # Перевірка чи існує директорія
        directory = Path(directory_path)
        if not directory.exists():
            print(Fore.RED + f"Помилка: Шлях {directory_path} не існує.")
            return
        # Перевірка чи є директорія саме директорією чи іншим об'єктом (файлом наприклад)
        if not directory.is_dir():
            print(Fore.RED + f"Помилка: {directory_path} не є директорією.")
            return # return у цих випадках використовується для того, щоб припинити виконання функції та не виконувати подальші операції, якщо вхідні умови не відповідають очікуванням (наприклад, директорія не існує або не є директорією). Тобто, функція не продовжить виконуватися, якщо не пройде ці перевірки.

        # Виведення поточної директорії
        print(Fore.CYAN + ' ' * indent + f"[{directory.name}]") # CYAN бірюзовий колір для папок [picture] та [Logo], коли вони виводяться по ходу виконання коду як поточна директорія
        
        # Перебір вмісту директорії (складових структурних елементів поточної директорії - її піддиректорій та файлів)
        for item in directory.iterdir():
            if item.is_dir():
                # Виведення директорії синім кольором
                print(Fore.BLUE + ' ' * (indent + 2) + f"[{item.name}]")
                print_directory_structure(item, indent + 4)  # Рекурсивний виклик для піддиректорії
            else:
                # Виведення файлів зеленим кольором
                print(Fore.GREEN + ' ' * (indent + 2) + item.name)
    except PermissionError:
        print(Fore.RED + f"Помилка: немає доступу до директорії {directory_path}.")
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Будь ласка, вкажіть шлях до директорії як аргумент командного рядка.")
    else:
        directory_path = sys.argv[1]
        print_directory_structure(directory_path)

# print(len(sys.argv))
# print(sys.argv)

print_directory_structure("c:/Users/User/Desktop/GOIT/My_repo/First_repo/goit-pycore-hw-04/task3/picture")

# print(type(print_directory_structure("c:/Users/User/Desktop/GOIT/My_repo/First_repo/goit-pycore-hw-04/task3/picture")))