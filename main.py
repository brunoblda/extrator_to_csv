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
    float_data = []
    for heading_element in list_heading:
        if "-VA-" in heading_element:
            float_data.append(heading_element)
    for data_row in list_data:
        data_row_list = data_row[0].split(",")
        dict_row = {}
        for iteration, data_row in enumerate(data_row_list):
            if list_heading[iteration] in float_data:
                dict_row[list_heading[iteration]] = float(data_row)/100
            else:
                dict_row[list_heading[iteration]] = data_row
        list_rows.append(dict_row)
    return list_rows

def separate_orgao_matricula(rows_list):
    """ Cria as colunas de orgao e matricula a partir da coluna GR-MATRICULA"""
    row_test = rows_list[0]
    headings_new = []
    # Separa orgao e servidor
    headings_new_serv = []
    heading_matricula_serv = 'GR-MATRICULA'
    if heading_matricula_serv in row_test:
        headings_new_serv.append('ORGAO_SERV')
        headings_new_serv.append('MATRICULA_SERV')
        for data_row in rows_list:
            data_row[headings_new_serv[0]] = data_row.get(
                heading_matricula_serv)[:5]
            data_row[headings_new_serv[1]] = data_row.get(
                heading_matricula_serv)[5:]
    # Separa orgao, servidor e pensionista
    headings_new_pens = []
    heading_matricula_pens = 'GR-MATR-BENEF-PENSAO-SERVIDOR'
    if heading_matricula_pens in row_test:
        headings_new_pens.append('ORGAO_SERV_PENS')
        headings_new_pens.append('MATRICULA_SERV_PENS')
        headings_new_pens.append('MATRICULA_PENS')
        for data_row in rows_list:
            data_row[headings_new_pens[0]] = data_row.get(
                heading_matricula_pens)[:5]
            data_row[headings_new_pens[1]] = data_row.get(
                heading_matricula_pens)[5:12]
            data_row[headings_new_pens[2]] = data_row.get(
                heading_matricula_pens)[12:]
    headings_new.extend(headings_new_serv)
    headings_new.extend(headings_new_pens)
    return (headings_new, rows_list)

if __name__ == '__main__':

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
                heading = line[:40]
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
                # Verifica a um indicativo de float 09,2
                if char_count.isdigit():
                    CHAR_INDEX += int(char_count) + PLUS
                else:
                    list_char_count = char_count.split(",")
                    char_count_intern = int(list_char_count[0]) + int(list_char_count[1])
                    CHAR_INDEX += int(char_count_intern) + PLUS

                line = insert_in_a_string(line, ",", CHAR_INDEX)
                PLUS = 1
            line = [line]
            lines_csv.append(line)

        with open(file_name + ".csv", "w", encoding="utf8", newline="") as result_file:
            rows = dict_rows(headings, lines_csv)
            (extend_heading, org_mat_rows) = separate_orgao_matricula(rows)
            headings[0:0] = extend_heading
            fieldnames = headings
            writer = csv.DictWriter(result_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in org_mat_rows:
                writer.writerow(row)
