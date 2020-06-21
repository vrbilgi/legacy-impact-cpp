Errors: #'utf-8' codec can't decode byte 0x95 in position 4072: invalid start byte
First:with open(newfile, 'r', encoding='utf-8') as infile:
Sol:with open(newfile, 'r', encoding='utf-8',errors='ignore') as infile: