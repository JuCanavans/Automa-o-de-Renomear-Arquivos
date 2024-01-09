import os 
from time import sleep as slp
from tkinter import *
from tkinter import filedialog
from pathlib import Path
from pathlib import PurePosixPath
from pathlib import PurePath

#Iniciação do Sistema
def start():
    print('------------------------------------------------')
    print('### Sistema de Automação de renomear arquivos ###')
    print('------------------------------------------------')
    slp(2)

#Função para direcionar o caminho
def folder_path():
    file_path = filedialog.askdirectory()
    return file_path

#Função para renomear os arquivos 
def rename():
    start()

    print('Favor escolher diretorio...')
    file_path = folder_path()
    folder = file_path + '//'
    Path(folder).glob('')
    
    count = 1
    files_aqr = input('Digite o novo nome dos arquivos: ')

    for strcount, filename in enumerate(os.listdir(folder)):
        new_name = files_aqr + '-' + str(count) + PurePosixPath(filename).suffix
        old_name = folder + filename
        new_name = folder + new_name

        os.rename(old_name, new_name)
        count += 1

    print(os.listdir(folder))
rename()