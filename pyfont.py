#!/usr/bin/env python3

import os
import zipfile
import requests
from sys import argv
from re import search
from colors import colorize
from time import ctime

HELP = """
Try to access the dafont website and copy the download link
from any available font. And then run the python script like this:

python3 pyfont https://dl.dafont.com/dl/?f=flashlight

Or like this:

chmod +x pyfont

./pyfont https://dl.dafont.com/dl/?f=flashlight
"""


def validate_url(url_to_download):
    if not search(r"^https://dl.dafont.com/dl/\?f=.*?$", url_to_download):
        raise ValueError("Invalid URL")


def download_from_dafont(url_to_download):
    name_file = 'font_file.zip'
    r = requests.get(url_to_download)
    with open(name_file, 'wb') as f:
        f.write(r.content)


def extraction_from_zip():
    try:
        fzip = zipfile.ZipFile('font_file.zip')
        fzip.extractall('font_dir')
        fzip.close()
    except zipfile.BadZipfile:
        colorize("\nThere was an error in the download file.", color="red")
        os.remove('font_file.zip')
        exit()


def install_font():
    REGEX_TYPE_FONT = r"^.*?\.(otf|ttf|OTF|TTF)$"
    os.system('mkdir -p ~/.fonts')
    os.chdir('font_dir')
    for file in os.listdir():
        if search(REGEX_TYPE_FONT, file):
            cmd = "cp '{}' ~/.fonts 2> /dev/null".format(file)
            os.system(cmd)
            font_log(file)
            stat_f = os.stat(file)
            colorize(
                "\nMoving {} to directory ~/.fonts".format(file), color="blue")
            colorize("[{:.2f} KB]".format(
                stat_f.st_size / 1000), color="blue")
    colorize("\n[DONE]\n", color="green")
    os.chdir('..')


def delete_temp():
    os.remove('font_file.zip')
    os.system('rm -rf font_dir')
    os.system('fc-cache')


def font_log(font_name):
    os.chdir('..')
    if "font_list.txt" not in os.listdir():
        f = open("font_list.txt", "w")
        f.write("Lista de fontes instaladas no diretório ~/.fonts:\n")
        f.close()

    f = open("font_list.txt", "a")
    f.write("{}\t{}\n".format(ctime(), font_name))
    f.close()
    os.chdir('font_dir')

try:
    URL_TO_DOWNLOAD = argv[1]
    colorize("\t\t\tPYFONT 0.1\t\t\t", background="red")
    validate_url(URL_TO_DOWNLOAD)
    download_from_dafont(URL_TO_DOWNLOAD)
    extraction_from_zip()
    install_font()
    delete_temp()
except IndexError:
    colorize("\nError. No arguments passed to script.", color="red")
    colorize(HELP, color="green")
    exit()
except ValueError:
    colorize("\nError. Invalid URL passed to script.", color="red")
    colorize(HELP, color="green")
    colorize("\nGo to dafont.com and choose a font.\n", color="blue")
    
