class method:
    def __init__(self):
        self.return_type = None
        self.method_name = None
        self.parameters = []
        self.start_line = None
        self.end_line = None


class myClass:
    def __init__(self, name):
        self.name = name
        self.listParents = []
        self.listMethods = []
        self.name_space = None


class classname:
    def __init__(self):
        self.listClasses = []
        self.listParents = []
        self.listMethods = []
        self.name_space = None

    def removeComment(self, name):
        pos_s = name.find("/*")
        pos_e = name.find("*/")
        if pos_s != -1 and pos_e != -1:
            name = name[:pos_s]+name[pos_e+2:]
        return name

    def append(self, name):
        c = myClass(self.removeComment(name))
        self.listClasses.append(c)

    def __str__(self):
        for class_name in self.listClasses:
            print(class_name.name)
        return ""
