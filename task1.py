
'''
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

1)Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
2)Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
3)Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
4)Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.

'''

from itertools import count

salary_path = 'salary_file.txt'

def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                
                if len(parts) != 2:
                    continue
                try:
                    salary = int(parts[1])
                    total += salary
                    count += 1
                except ValueError:
                    continue
    
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return 0, 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0, 0
    
    average = round(total / count, 2) if count > 0 else 0
    return total, average, count

total, average, count = total_salary(salary_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
print(f"Кількість записів: {count}")