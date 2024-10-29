import os

import shutil

import utils


def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
        return None


def get_dst_dir_for_raws(conf):
    return os.path.join(*[utils.get_dst_dir(), conf['photo_dir_year'], conf['photo_dir_date_name']])


if __name__ == '__main__':
    conf = utils.get_config()
    jpg_folder = get_dst_dir_for_raws(conf)
    raw_folder = os.path.join(jpg_folder, 'RAWs')

    raw_delete_folder = os.path.join(raw_folder, "DELETE")
    if not os.path.exists(raw_delete_folder):
        os.mkdir(raw_delete_folder)

    size_saved = 0
    num_of_images = 0

    for raw_file in os.listdir(raw_folder):
        raw_file_path = os.path.join(raw_folder, raw_file)
        if os.path.isfile(raw_file_path):
            raw_file_name, raw_file_type = raw_file.split('.')
            if raw_file_type == 'CR3':
                # If JPG does not exist, move the RAW file to a DELETE folder
                matching_jpg_path = find_file(f'{raw_file_name}.JPG', jpg_folder)
                if not matching_jpg_path:
                    print(f'Moving {raw_file} to DELETE folder')
                    num_of_images += 1
                    size_saved += os.path.getsize(raw_file_path)
                    shutil.move(raw_file_path, os.path.join(raw_delete_folder, raw_file))

    print(f'Moved {num_of_images} RAW files ({utils.convert_size(size_saved)}) for deletion.')










