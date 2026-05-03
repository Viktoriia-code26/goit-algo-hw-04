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
                    salary = float(parts[1])
                    total += salary
                    count += 1
                except ValueError:
                    continue

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return 0, 0

    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

    average = round(total / count, 2) if count > 0 else 0
    return total, average


total, average = total_salary(salary_path)

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
