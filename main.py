""" Main module """
from os import listdir
from os.path import isfile, join
import sys

onlyfiles = [f for f in listdir(sys.path[0]) if isfile(join(sys.path[0], f))]

name_files = []

def insert_in_a_string (source_str, insert_str, pos):
    return source_str[:pos] + insert_str + source_str[pos:]

for file in onlyfiles:
    full_name_list = file.split(".")
    name = full_name_list[0]
    name_files.append(name)
    
extrator_files = []

for file in name_files:
    if name_files.count(file) == 2:
        extrator_files.append(file)

# set é o nome em ingles de conjunto (elementos não se repetem)
set_extrator_files = set(extrator_files)

extrator_files_set = list(set_extrator_files)

for file_name in extrator_files_set:
    file_REF = sys.path[0]+"\\"+file_name+'.REF'
    file_TXT = sys.path[0]+"\\"+file_name+'.TXT'
    chars_count = []
    with open(file_REF, encoding="utf8") as f:
        for line in f:
            print(line[-4:].strip())
            char_count = line[-4:].strip() 
            chars_count.append(char_count)
    lines = []
    with open(file_TXT, encoding="utf8") as f:
        for line in f:
            lines.append(line.strip())
    lines_csv = []
    for line in lines:
        plus = 0
        for char_count in chars_count:
            line = insert_in_a_string(line ,";",int(char_count)+ plus)
            plus += 1
        lines_csv.append(line) 
    print(lines[0])
    print(lines_csv[0])
