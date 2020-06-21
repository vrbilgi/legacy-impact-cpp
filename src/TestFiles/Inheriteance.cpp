#include <iostream>
 
using namespace std;
// Base class
class Shape2 {
   public:
      void setWidth2(int w) {
         width2 = w;
      }
      void setHeight2(int h) {
         height2 = h;
      }
      
   protected:
      int width2;
      int height2;
};

// Base class
class Shape {
   public:
      void setWidth(int w) {
         width = w;
      }
      void setHeight(int h) {
         height = h;
      }
      
   protected:
      int width;
      int height;
};

// Derived class
class Rectangle: public Shape {
   public:
      int getArea() { 
         return (width * height); 
      }
};

// Derived class
class Box : public Shape {
   public:
      int getArea() { 
         return (width * height); 
      }
};
// Derived class
class SecondBox :/*test*/ public Shape {
   public:
      int getArea() { 
         return (width * height); 
      }
};

// Derived class
class ThirdBox : public /*test*/ Shape {
   public:
      int getArea() { 
         return (width * height); 
      }
};

// Derived class
class FourthBox : public Shape /*test*/ {
   public:
      int getArea() { 
         return (width * height); 
      }
};

// Derived class
class FifthBox : public Shape 
{
   public:
      int getArea() { 
         return (width * height); 
      }
};

// Derived class
class SixthBox : 
public Shape 
{
   public:
      int getArea() { 
         return (width * height); 
      }
};

// Derived class
class SeventhBox : 
public 
Shape 
{
   public:
      int getArea() { 
         return (width * height); 
      }
};

// Derived class
class EighthBox : 
public 
Shape ,Shape2
{
   public:
      int getArea() { 
         return (width * height); 
      }
};

// Derived class
class NinethBox : 
public 
Shape ,/***/Shape2
{
   public:
      int getArea() { 
         return (width * height); 
      }
};


int main(void) {
   Rectangle Rect;
 
   Rect.setWidth(5);
   Rect.setHeight(7);

   // Print the area of the object.
   cout << "Total area: " << Rect.getArea() << endl;

   return 0;
}