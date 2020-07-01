import unittest
from readFile import *
class Test(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        pass
    # def test_1(self):
    #     readFolder("TestFiles")

    def test_2(self):
        res =" #include <iostream>  using namespace std;  class Shape2 {    public:       void setWidth2(int w) {          width2 = w;       }       void setHeight2(int h) {          height2 = h;       }     protected:       int width2;       int height2; };   class Shape {    public:       void setWidth(int w) {          width = w;       }       void setHeight(int h) {          height = h;       }     protected:       int width;       int height; };   class Rectangle: public Shape {    public:       int getArea() {          return (width * height);       } };   class Box : public Shape {    public:       int getArea() {          return (width * height);       } };  class SecondBox : public Shape {    public:       int getArea() {          return (width * height);       } };   class ThirdBox : public Shape {    public:       int getArea() {          return (width * height);       } };   class FourthBox : public Shape {    public:       int getArea() {          return (width * height);       } };   class FifthBox : public Shape {    public:       int getArea() {          return (width * height);       } };   class SixthBox : public Shape {    public:       int getArea() {          return (width * height);       } };   class SeventhBox : public Shape {    public:       int getArea() {          return (width * height);       } };   class EighthBox : public Shape ,Shape2 {    public:       int getArea() {          return (width * height);       } };   class NinethBox : public Shape ,Shape2 {    public:       int getArea() {          return (width * height);       } };   int main(void) {    Rectangle Rect;     Rect.setWidth(5);    Rect.setHeight(7);      cout << \"Total area: \" << Rect.getArea() << endl;     return 0; }"
        line = readFile("TestFiles/Inheriteance.cpp")
        self.assertEqual(res,line)

    def test_2(self):
        res =" #include <iostream>  using namespace std;  class Shape2 {    public:       void setWidth2(int w) {          width2 = w;       }       void setHeight2(int h) {          height2 = h;       }     protected:       int width2;       int height2; };   class Shape {    public:       void setWidth(int w) {          width = w;       }       void setHeight(int h) {          height = h;       }     protected:       int width;       int height; };   class Rectangle: public Shape {    public:       int getArea() {          return (width * height);       } };   class Box : public Shape {    public:       int getArea() {          return (width * height);       } };  class SecondBox : public Shape {    public:       int getArea() {          return (width * height);       } };   class ThirdBox : public Shape {    public:       int getArea() {          return (width * height);       } };   class FourthBox : public Shape {    public:       int getArea() {          return (width * height);       } };   class FifthBox : public Shape {    public:       int getArea() {          return (width * height);       } };   class SixthBox : public Shape {    public:       int getArea() {          return (width * height);       } };   class SeventhBox : public Shape {    public:       int getArea() {          return (width * height);       } };   class EighthBox : public Shape ,Shape2 {    public:       int getArea() {          return (width * height);       } };   class NinethBox : public Shape ,Shape2 {    public:       int getArea() {          return (width * height);       } };   int main(void) {    Rectangle Rect;     Rect.setWidth(5);    Rect.setHeight(7);      cout << \"Total area: \" << Rect.getArea() << endl;     return 0; }"
        line = readFile("TestFiles/Inheriteance.cpp")
        self.assertEqual(res,line)
        class_name = classname()
        mainloop(line,class_name)
        length = len(class_name.listClasses)
        self.assertEqual(12,length)

    def test_3(self):
        res =" class myClass_1; class myClass_2 how are you; class myClass_22 how ; class myClass_23 how;  class myClass_3 ; class myClass_33    ; class myClass_4 ; class myClass_5;"
        line = readFile("TestFiles/TestClass.cpp")
        self.assertEqual(res,line)

    def test_33(self):
        res =" class myClass_1; class myClass_2 how are you; class myClass_22 how ; class myClass_23 how;  class myClass_3 ; class myClass_33    ; class myClass_4 ; class myClass_5;"
        line = readFile("TestFiles/TestClass.cpp")
        self.assertEqual(res,line)
        class_name = classname()
        mainloop(line,class_name)
        length = len(class_name.listClasses)
        self.assertEqual(5,length)







    def test_4(self):
        res=" NGI_LOG_DEBUG(\"Original Flight period to get booking class filter for ASM TIM Wdc: \" << ioScheduleChange.getFlightPeriod()->shortDump()); NGI_LOG_DEBUG(\"Flight period to get booking class filter for ASM TIM Wdc: \" << theNewFlightPeriod.shortDump()); NGI_LOG_DEBUG(\"Selected booking class filters:\");"
        line = readFile("TestFiles/TestFallClass.cpp")
        self.assertEqual(res,line)
    def test_44(self):
        res=" NGI_LOG_DEBUG(\"Original Flight period to get booking class filter for ASM TIM Wdc: \" << ioScheduleChange.getFlightPeriod()->shortDump()); NGI_LOG_DEBUG(\"Flight period to get booking class filter for ASM TIM Wdc: \" << theNewFlightPeriod.shortDump()); NGI_LOG_DEBUG(\"Selected booking class filters:\");"
        line = readFile("TestFiles/TestFallClass.cpp")
        self.assertEqual(res,line)
        class_name = classname()
        mainloop(line,class_name)
        length = len(class_name.listClasses)
        self.assertEqual(1,length)





    def test_5(self):
        res=" class TestTestCalss : public COM::Abstract {   friend class CoverTestTestCalss;   friend class CoverTestClass2 ; };  } "
        line = readFile("TestFiles/TestFriendClass.cpp")
        self.assertEqual(res,line)

    def test_55(self):
        res=" class TestTestCalss : public COM::Abstract {   friend class CoverTestTestCalss;   friend class CoverTestClass2 ; };  } "
        line = readFile("TestFiles/TestFriendClass.cpp")
        self.assertEqual(res,line)
        class_name = classname()
        mainloop(line,class_name)
        length = len(class_name.listClasses)
        self.assertEqual(3,length)




    def test_6(self):
        res="  DequeueAction Test_Calss::dequeueCallback(Message& msg) {     try   {     std::string theMessageAsString;     }   NGI_SUPERCATCH_ACT_L(\"unexpected exception in first callback\", _aSC = NULL;                        return DequeueAction::MOVE_TO_EXCEPTION_QUEUE;); }"
        line = readFile("TestFiles/TestMultiline.cpp")
        self.assertEqual(res,line)
 
    def test_66(self):
        res="  DequeueAction Test_Calss::dequeueCallback(Message& msg) {     try   {     std::string theMessageAsString;     }   NGI_SUPERCATCH_ACT_L(\"unexpected exception in first callback\", _aSC = NULL;                        return DequeueAction::MOVE_TO_EXCEPTION_QUEUE;); }"
        line = readFile("TestFiles/TestMultiline.cpp")
        self.assertEqual(res,line)
        class_name = classname()
        mainloop(line,class_name)
        length = len(class_name.listClasses)
        print(class_name)
        self.assertEqual(0,length)



    def test_7(self):
        res="   #include <iostream> #include <vector>  using namespace std;  int main() { 	vector<int> g1;  	for (int i = 1; i <= 5; i++) 		g1.push_back(i);  	cout << \"Output of begin and end: \"; 	for (auto i = g1.begin(); i != g1.end(); ++i) 		cout << *i <<;  	return 0; }"
        line = readFile("TestFiles/comments.cpp")
        self.assertEqual(res,line)
 
    def test_77(self):
        res="   #include <iostream> #include <vector>  using namespace std;  int main() { 	vector<int> g1;  	for (int i = 1; i <= 5; i++) 		g1.push_back(i);  	cout << \"Output of begin and end: \"; 	for (auto i = g1.begin(); i != g1.end(); ++i) 		cout << *i <<;  	return 0; }"
        line = readFile("TestFiles/comments.cpp")
        self.assertEqual(res,line)
        class_name = classname()
        mainloop(line,class_name)
        length = len(class_name.listClasses)
        print(class_name)
        self.assertEqual(0,length)




    def test_8(self):
        res="                                "
        line = readFile("TestFiles/comments.hpp")
        self.assertEqual(res,line)

    def test_88(self):
        res="                                "
        line = readFile("TestFiles/comments.hpp")
        self.assertEqual(res,line)
        class_name = classname()
        mainloop(line,class_name)
        length = len(class_name.listClasses)
        self.assertEqual(0,length)



    def test_9(self):
        res=" #include \"iostream\" using namespace std;  class myClass{ public: void setpVar(int pvar){pVar = pvar;} void setpfvar(int pfvar){this.pfvar = pfvar;} void setplvar(long plvar){     this.plvar = plvar;     }  private:     int piVar;     float pfvar;     long plvar;     std::string myString;  }"
        line = readFile("TestFiles/class_method/Test.hpp")
        self.assertEqual(res,line)

    def test_99(self):
        res=" #include \"iostream\" using namespace std;  class myClass{ public: void setpVar(int pvar){pVar = pvar;} void setpfvar(int pfvar){this.pfvar = pfvar;} void setplvar(long plvar){     this.plvar = plvar;     }  private:     int piVar;     float pfvar;     long plvar;     std::string myString;  }"
        line = readFile("TestFiles/class_method/Test.hpp")
        self.assertEqual(res,line)
        class_name = classname()
        mainloop(line,class_name)
        length = len(class_name.listClasses)
        self.assertEqual(1,length)



if __name__ == '__main__':
    unittest.main()
