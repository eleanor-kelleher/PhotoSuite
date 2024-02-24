import os
from os.path import isfile, join
import shutil
import yaml

from PIL import Image


def get_date_taken(path):
    exif = Image.open(path).getexif()
    if not exif:
        raise Exception('Image {0} does not have EXIF data.'.format(path))
    date = exif[306].split(" ")[0]  # EXIF data index corresponding to date & time taken
    return date.replace(":", "-")


if __name__ == '__main__':
    with open("config.yml", 'r') as stream:
        conf = yaml.safe_load(stream)

    directory_list = list()
    for root, dirs, files in os.walk(conf['sd_card_path'], topdown=False):
        for name in dirs:
            directory_list.append(os.path.join(root, name))

    for src_directory in directory_list:
        files = [f for f in os.listdir(src_directory) if isfile(join(src_directory, f))]
        print(f"Importing from {src_directory}")
        for file in files:
            photo_date = get_date_taken(f"{src_directory}\{file}")
            year_dir_path = f"{conf['photographs_path']}\{photo_date.split('-')[0]}"
            if not os.path.exists(year_dir_path):
                os.mkdir(year_dir_path)
            if not os.path.exists(f"{year_dir_path}\{photo_date}"):
                os.mkdir(f"{year_dir_path}\{photo_date}")
            shutil.copyfile(f"{src_directory}\{file}", f"{year_dir_path}\{photo_date}\{file}")
            print(f"  -> {year_dir_path}\{photo_date}\{file}")
