class classname:
    def __init__(self):
        self.listClasses=[]
    def append(self,name):
        def removeComment(name):
            pos_s = name.find("/*")
            pos_e = name.find("*/")
            if pos_s != -1 and pos_e != -1:
                name = name[:pos_s]+name[pos_e+2:]
            return name
        self.listClasses.append(removeComment(name))
    def __str__(self):
        for name in self.listClasses:
            print (name)
        return ""
    

    