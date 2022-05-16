files_path = 'ta_hw1/name_files/'

with open('ta_hw1/names.txt') as f:
    for line in f:
        fname, lname = line.strip().lower().split(" ")
        file_name = lname + '_' + fname + '_' + '01_hw_it116.txt'
        open(files_path + file_name, 'w')
