def get_cats_info(path: str) -> list:
    # створюємо порожній словник та порожній список для майбутнього списку словників
    dictt = {}
    list_dict = []
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
                for line in file:
                    # Прибираємо зайві пробіли з рядків та розділяємо значення рядка по ',' на 3 рядка (id, name, age)
                    id, name, age = line.strip().split(',')
                    # Додаємо у створений вище словник ключі та значення з обробленого файлу по кожному коту
                    dictt.update({"id": id, "name": name, "age": age})
                    # Додаємо у створений вище список - словники даних по кожному коту
                    list_dict.append(dictt)
    # Виконуємо обробку винятків (помилок)
    except FileNotFoundError:
            print(f"Відсутній файл у вказаному шляху {path}.")
    except Exception as e:
            print(f"Сталася помилка при читанні файлу: {e}")
    return list_dict
         

print(get_cats_info("c:/Users/User/Desktop/GOIT/My_repo/First_repo/goit-pycore-hw-04/task2/cats.txt"))
