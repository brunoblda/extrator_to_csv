""" Main module """
from os import listdir
from os.path import isfile, join
import csv
import os

def insert_in_a_string(source_str, insert_str, pos):
    """ Insere uma string em uma outra string pelo index"""
    return source_str[:pos] + insert_str + source_str[pos:]

def heading_list_to_text(list_heading):
    """ Tranforma uma lista de strings em uma grande string"""
    text = "".join(list_heading)
    return text

def dict_rows(list_heading, list_data):
    """ Cria o dicionario para inclusão dos dados e do header do arquivo csv"""
    list_rows = []
    for data_row in list_data:
        data_row_list = data_row[0].split(",")
        dict_row = {}
        for iteration, data_row in enumerate(data_row_list):
            dict_row[list_heading[iteration]] = data_row
        list_rows.append(dict_row)
    return list_rows

def separate_orgao_matricula(rows_list):
    """ Cria as colunas de orgao e matricula a partir da coluna GR-MATRICULA"""
    row_test = rows_list[0]
    headings_new = []
    heading_matricula = 'GR-MATRICULA                            N'
    if heading_matricula in row_test:
        headings_new.append('ORGAO                                   N')
        headings_new.append('MATRICULA                               N')
        for data_row in rows_list:
            data_row[headings_new[0]] = data_row.get(
                heading_matricula)[:5]
            data_row[headings_new[1]] = data_row.get(
                heading_matricula)[5:]
    return (headings_new, rows_list)

directory = os.getcwd()

onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]

name_files = []

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
    file_REF = directory+"\\"+file_name+'.REF'
    file_TXT = directory+"\\"+file_name+'.TXT'
    chars_count = []
    headings = []

    with open(file_REF, encoding="utf8") as f:
        for line in f:
            char_count = line[-4:]
            chars_count.append(char_count.strip())
            heading = line[:41]
            headings.append(heading.strip())
    lines = []

    with open(file_TXT, encoding="utf8") as f:
        for line in f:
            lines.append(line.strip())
    lines_csv = []

    for line in lines:
        PLUS = 0
        CHAR_INDEX = 0
        for i in range(len(chars_count)-1):
            char_count = chars_count[i]
            CHAR_INDEX += int(char_count) + PLUS
            line = insert_in_a_string(line, ",", CHAR_INDEX)
            PLUS = 1
        line = [line]
        lines_csv.append(line)

    with open(file_name + ".csv", "w", encoding="utf8", newline="") as result_file:
        rows = dict_rows(headings, lines_csv)
        (extend_heading, org_mat_rows) = separate_orgao_matricula(rows)
        headings[1:1] = extend_heading
        fieldnames = headings
        writer = csv.DictWriter(result_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in org_mat_rows:
            writer.writerow(row)
