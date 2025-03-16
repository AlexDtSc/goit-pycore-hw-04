def total_salary(path: str):
    total_salary = 0           # задаємо змінну для майбутньої агрегації суми зарплати
    counter_developers = 0     # задаємо змінну для підрахунку кількості розробників-працівників 
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Прибираємо зайві пробіли з рядків та розділяємо значення рядка по ',' на 2 рядка (person, salary)
                    person, salary = line.strip().split(",")
                    total_salary += int(salary)
                    counter_developers += 1
                # Обробка помилки некоректного значення: якщо рядок складається не з двох частин або зарплата не є числом, пропускаємо цей рядок
                except ValueError:
                    print(f"Помилка в рядку: {line.strip()}")
                    continue

        if counter_developers == 0:
            return 0, 0  # Якщо немає розробників в файлі
        
        average_salary = total_salary / counter_developers
        return total_salary, average_salary
    # Обробка помилки якщо файл відсутній
    except FileNotFoundError:
        print(f"Відсутній файл у вказаному шляху {path}.")
        return 0, 0
    # Обробка інших видів помилок
    except Exception as e:
        print(f"При обробці файлу відбулася наступна помилка : {e}")
        return 0, 0

# Приклад використання функції:
total, average = total_salary("c:/Users/User/Desktop/GOIT/My_repo/First_repo/goit-pycore-hw-04/task1/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")




