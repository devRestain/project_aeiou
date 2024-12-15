import json


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def add_json(file_path: str, key: str, new_value: list):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    data[key] = data[key] + new_value

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
