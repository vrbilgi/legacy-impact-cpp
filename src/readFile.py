import os
from Class import *
from Comments import *
c = classname()
multiliencomment=[]
def mainloop(line):
    # print("FULL LINE = ",line)
    class_find = 0 
    multiline_c = 0
    while(class_find>=0):
        # print("\n\n")
        # print(class_find)
        # print(line[class_find:])
        class_find = line.find("class ",class_find)
        # print("class_find=",class_find)
        if class_find ==-1:
            break
        open_semicolon = line.find(";",class_find)
        open_brases = line.find("{",class_find)
        # print("class_find=",class_find)
        # print("open_semicolon=",open_semicolon)
        # print("open_brases=",open_brases)
        # print("line=",line[class_find:open_brases])
        # print("line",line[class_find:open_semicolon])

        if open_semicolon > open_brases:
            if open_brases!=-1:
                c.append(line[class_find+5:open_brases].strip())
                class_find = open_brases
            else: 
                tmp = line[class_find+5:open_semicolon].strip()
                open_space = tmp.find(" ")
                if open_space ==-1:
                    c.append(line[class_find+5:open_semicolon].strip())
                class_find = open_semicolon
        else:
            tmp = line[class_find+5:open_semicolon].strip()
            open_space = tmp.find(" ")
            if open_space == -1:
                c.append(line[class_find+5:open_semicolon].strip())
            class_find = open_semicolon
  
def readFile(newfile):
    full_file = ""
    try:
        with open(newfile, 'r', encoding='utf-8',errors='ignore') as infile:
            multi_comment_start = False
            for line in infile:
                if multi_comment_start:
                    pos = line.find("*/")
                    if pos!=-1:
                        pos_end = line.find("*/")

                        full_file = full_file +" "+ line[pos+2:].rstrip()
                        multi_comment_start = False 
                        continue 
                    else:
                        continue

                pos = line.find("//")
                if pos!=-1:
                    full_file = full_file +" "+ line[:pos].rstrip()
                    continue
                pos = line.find("/*")
                if pos!=-1:
                    pos_end = line.find("*/")
                    if pos_end!=-1:
                        full_file = full_file +" "+ line[:pos].rstrip()+line[pos_end+2:].rstrip()
                        multi_comment_start = False 
                        continue
                    full_file = full_file +" "+ line[:pos].rstrip()
                    multi_comment_start = True 
                    continue
                if line.startswith("//")==False:
                    full_file = full_file +" "+ line.rstrip()

        return full_file
    except Exception as e: 
        print(e)
        print("File Name =",newfile)
        #'utf-8' codec can't decode byte 0x95 in position 4072: invalid start byte
        import sys
        sys.exit()

def readFolder(foldername):
    print("readfoldername",foldername)
    for root, dirs, files in os.walk(foldername, topdown = False):
        for name in files:
            if name[-3:]=="cpp" or name[-3:] =="hpp":
                print(os.path.join(root, name))
                line = readFile(os.path.join(root, name))
                mainloop(line)
def main():
    # readFolder("/Users/vrbilgi/Documents/Schedule/SKD/src/command/publication")
    readFolder("/Users/vrbilgi/Project/FindClass/src/TestFiles")
if __name__ == '__main__':
    main()
    print("=============")
    print(c)
    print("=============")

   
#include <iostream>using namespace std;class Shape2 {   public:      void setWidth2(int w) {         width2 = w;      }      void setHeight2(int h) {         height2 = h;      }   protected:      int width2;      int height2;};class Shape {   public:      void setWidth(int w) {         width = w;      }      void setHeight(int h) {         height = h;      }   protected:      int width;      int height;};class Rectangle: public Shape {   public:      int getArea() {         return (width * height);      }};