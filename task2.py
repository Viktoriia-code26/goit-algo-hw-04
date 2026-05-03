cats_file = 'cats_file.txt'

def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(',')

                if len(parts) != 3:
                    continue

                cat_id, name, age = parts

                cats_info.append({
                    "id": cat_id.strip(),
                    "name": name.strip(),
                    "age": age.strip()
                })

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []

    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []
    return cats_info

cats_info = get_cats_info(cats_file)
print(cats_info)