#include "iostream"
using namespace std;

class myClass{
public:
void setpVar(int pvar){pVar = pvar;}
void setpfvar(int pfvar){this.pfvar = pfvar;}
void setplvar(long plvar){
    this.plvar = plvar;
    }

private: 
    int piVar;
    float pfvar;
    long plvar;
    std::string myString; 

}