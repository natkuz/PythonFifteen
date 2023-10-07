# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
from sys import argv
from collections import namedtuple
import logging

FORMAT = '{asctime} {levelname} {name} {funcName} {msg}'
logging.basicConfig(format=FORMAT, filename='logfile.log', filemode='a', encoding='utf-8', level=logging.INFO,
                    style="{")
logger = logging.getLogger(__name__)

def dir_walker(path: str):
    WalkerDir = namedtuple('DIR', ['name', 'flag', 'parent'])
    WalkerFile = namedtuple('FILE', ['name', 'extension', 'flag', 'parent'])
    flag = 'child'
    root = path.split('\\')[-1]
    print(root)
    for path, dir_list, file_list in os.walk(path):
        for cur_dir in dir_list:
            print(WalkerDir(cur_dir, flag, path.split('\\')[-1]))
            re_msg = f'{cur_dir} -> {path} | "DIR"'
            logger.info(msg=re_msg)
        for cur_file in file_list:
            print(dir_list)
            if not file_list in dir_list:
                flag = 'root'
            else:
                flag = 'child'
            print(WalkerFile(cur_file.split('.')[0], cur_file.split('.')[1], flag, path.split('\\')[-1]))
            re_msg = f'{cur_file} -> {path} | "FILE"'
            logger.info(msg=re_msg)


if __name__ == '__main__':
    if len(argv) > 1:
        pprint(dir_walker(argv[1]))
    else:
        print("Нужен путь до директории")
