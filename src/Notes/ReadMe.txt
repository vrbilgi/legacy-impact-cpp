1: Errors: #'utf-8' codec can't decode byte 0x95 in position 4072: invalid start byte
First:with open(newfile, 'r', encoding='utf-8') as infile:
Sol:with open(newfile, 'r', encoding='utf-8',errors='ignore') as infile:

2: This parameter is used in  
    self.maxDiff = None
    self.assertEqual(res,line)
3: if some big string comparision is failing in asserEqual comparision
   Then write a for loop and compare the char by char :)    
 
