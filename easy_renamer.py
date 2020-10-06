#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os

from click._compat import raw_input

path_to_rename = raw_input('Введите путь для переименования: ')
prefix_for_dir = raw_input('Введите префикс для каталогов: ')
prefix_for_file = raw_input('Введите префикс для файлов: ')


def easy_renamer():
    """ Эта функция обрезает названия шары с которой
    были скачаны файлы, если в имени файлов и папок
    присутствует её название.
    """
    for dir_path, dir_names, file_names in os.walk(path_to_rename, topdown=False):
        os.chdir(dir_path)
        for d in dir_names:
            if d.startswith(prefix_for_dir[:3]):
                new_dir_name = d.replace(prefix_for_dir + ' ', '', 1)
                print(d, '==>', new_dir_name)
                os.rename(d, new_dir_name)
        for d in file_names:
            if d.startswith(prefix_for_file[:3]):
                new_file_name = d.replace(prefix_for_file + ' ', '', 1)
                print(d, '==>', new_file_name)
                os.rename(d, new_file_name)


if __name__ == '__main__':
    easy_renamer()

