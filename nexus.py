#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os
from click._compat import raw_input

# path = raw_input('Введите путь для копирования в репозиторий: ')
# repo_name = raw_input('Введите название репозитория: ')
path = '/home/adwiz/tmp/kub'
repo_name = 'mpgu_static'


def repo_copier():
    """
    Эта функция копирует артефакты в репозиторий.
    """
    for dir_path, dir_names, file_names in os.walk(path, topdown=False):
        os.chdir(dir_path)
        for d in file_names:
            os.system(f'curl -v -u admin:bmV4dXMtYWRtaW4= --upload-file {d} http://inf-o-nexus-p3.gu.local:8081/repository/{repo_name}{dir_path}/{d}')
            # os.system(f'curl get http://ya.ru/{repo_name}{dir_path}/')
            # print(f'curl -v -u admin:bmV4dXMtYWRtaW4= --upload-file {d} http://inf-o-nexus-p3.gu.local:8081/repository/{repo_name}{dir_path}/')


if __name__ == '__main__':
    repo_copier()
