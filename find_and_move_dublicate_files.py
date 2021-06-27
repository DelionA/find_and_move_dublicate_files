#
import os
import filecmp
import shutil

def create_files_dict():
    print('\nзапуск создания словаря файлов... ')
    for dirpath, dirnames,filenames in os.walk(path):
        for name in filenames:
            if name not in dict_files:
                dict_files[name] = list()
            dict_files[name].append(os.path.join(dirpath, name))
    print('\nсоздание словаря закончено...')
    files_count = len(dict_files)
    print(f'\nвсего найдено файлов...{files_count}')

def compared_two_files(file_1, file_2):
    return filecmp.cmp(file_1, file_2)

def match_conditions(file_1, file_2):
    if file_1 == file_2:
        return False    
    file_12 = file_1 + file_2
    file_21 = file_2 + file_1
    if file_12 in set_compared or file_21 in set_compared:
        return False
    set_compared.add(file_12)
    return True

def comparsion_file_list(file_list):     
    if len(file_list) == 1:
        return
    for i in file_list:
        file_1 = i
        for j in file_list:
            file_2 = j
            if match_conditions(file_1, file_2) and compared_two_files(file_1, file_2):
                set_subject_to_transfer.add(file_2)

def find_dublicate_files_func():
    for key in dict_files:
        comparsion_file_list(dict_files[key])
    files_to_transfer = len(set_subject_to_transfer)
    print(f'\nнужно переместить файлов...{files_to_transfer}')
    
def move_files_func(numerate=1):
    print('начинаем перемещение файлов...')
    for file_move in set_subject_to_transfer:
        print_func(file_move)
        print()
        new_file_name =  path_to_destination + str(numerate) + '_' + file_move.split('/')[-1]
        shutil.move(file_move, new_file_name)
        numerate += 1
    print('перемещение файлов законено...')

def print_func(data=''):
    print(data+'\r', end='')
#
path = '' # path source folder
path_to_destination = '' # path destination folder

dict_files = dict()
set_compared = set()
set_subject_to_transfer = set()
#
create_files_dict()
find_dublicate_files_func()
move_files_func()
