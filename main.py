import os
import pathlib


def get_folder_number(dir: str, base_dir_path: str):
    return dir.split(f"{str(base_dir_path)}\\")[1].split(" ", 1)[0]


def get_folder_title(dir: str, base_dir_path: str):
    return dir.split(f"{str(base_dir_path)}\\")[1].split(" ", 1)[1]


def rename_file(original_path: str, new_name: str, num: int):
    if not os.path.isdir(original_path):
        file_type = original_path.rsplit('.', 1)[1]
        filepath = original_path.rsplit('\\', 1)
        if "ini" not in filepath[1]:
            new_filename = f"{new_name}_{str(num)}.{file_type}"
            if filepath[1] != new_filename:
                os.rename(original_path, f"{filepath[0]}\\{new_filename}")
                print(f"  - {filepath[1]} -> {new_filename}")


if __name__ == '__main__':
    base_dir_path = str(pathlib.Path(__file__).parent.parent.resolve())
    for file in os.listdir(base_dir_path):
        dir = os.path.join(base_dir_path, file)
        if os.path.isdir(dir):
            folder_number = get_folder_number(dir, base_dir_path)
            if folder_number.isdigit() and int(folder_number) > 0:
                folder_title = get_folder_title(dir, base_dir_path)
                print(f"\nIn {dir}, renaming:")
                for i, filename in enumerate(os.listdir(dir)):
                    try:
                        rename_file(f"{dir}\{filename}", "IBB_" + folder_title.replace(" ", ""), i + 1)
                    except FileExistsError as e:
                        break
