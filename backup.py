#!/usr/bin/env python3
import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"/home/adwiz/Python"']  #, '/home/adwiz/PycharmProjects']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = '/home/adwiz/tmp'  # Подставьте тот путь, который вы будете использовать.
# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%d-%m-%Y')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')
# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0:  # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
    comment.replace(' ', '_') + '.zip'
# 4. Именем для bzip-архива служит текущая дата и время.
target = today + os.sep + time.strftime('%d.%m.%Y-%H%M%S') + '.tar.bz2'
# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today)  # создание каталога
    print('Каталог успешно создан', today)
# 5. Используем команду "zip" для помещения файлов в zip-архив
bzip_command = "tar -cvf {0} {1} -j".format(target, ' '.join(source))
# Запускаем создание резервной копии
if os.system(bzip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
