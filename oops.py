# class
class car:
    print("this is car")
    def display(self):
        a,b=10,23
        print(a,b)
obj=car()
obj.display()

#__init__
class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        print("this is init")
    def display(self):
        print(self.brand,self.price)
m=mobile("redmi",12200)
m.display()

# @property
class Student:
    def __init__(self,name,num):
        if not name:
            raise ValueError("missing name")
        self.name=name
        self.house=house
    def __str__(self):
        return f"{self.name} from {self.house}"
    @property
    def house(self):
        return self.house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor","Hfflepff", "Ravenclaw","Slyther"]:
            raise ValueError("invalid house")
def main():
    student=get_student()
    student.house="Number Four, Privet Drive"
    print(student)

def get_student():
    name=input("Name: ")
    house= input("House: ")

if __name__ == "__main__":
    main()



#single inheritance
class parent:
    def fun1(self):
        print("this is parent class")
class child(parent):
    def fun2(self):
        print("this is child")
c=child()
c.fun1()

# multilevel
class parent:
    def fun1(self):
        print("this is parent class")
class child(parent):
    def fun2(self):
        print("this is child")
class grandchild(child):
    def fun3(self):
        print("this is grandchild")
c=grandchild()
c.fun1()
c.fun2()


# hierarchical 
class parent:
    def fun1(self):
        print("this is parent class")
class child(parent):
    def fun2(self):
        print("this is child")
class child2(parent):
    def fun3(self):
        print("this is grandchild")
c=child()
c1=child2()
c.fun1()
c1.fun1()


# multiple inheritance
class father:
    def fun(self):
        print("this is father class")
class mother:
    def fun1(self):
        print("the is mother class")
class child(father,mother):
    def fun3(self):
        print("this is child")
c=child()
c.fun()
c.fun1()

#super keyword
class A:
    def __init__(self):
        print("this os class A")
    def fun1(self):
        print("this is father class")
class B(A):
    def __init__(self):
        print("this is class b")
        super().__init__()
    def fun2(self):
        print("this is mother class")
b=B()


# polymorphism

#mehod overloading
# same class
# same function or method names
# different parameters
class A:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=2):
        return a+b
obj=A()
print(obj.sum(3,5))

#mehod over-riding
# same class
# same function or method names
# different parameters
class parent:
    def method1(self):
        print("thid is parent")
class child(parent):
    def method1(self):
        print("child class")
    
c=child()
c.method1()






# #encapsulation
# class demo:
#     def __init__(self,a,b):
#         self.__a=a  #private
#         self._b=b   #protected
# class demo2(demo):
#     def output(self):
#         print(self._b)
# d=demo2(3,7)
# d.output()




# abstraction
from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("this is concrete method")
class B(A):
    def method1(self,name):
        self.name =name
        return self.name
    
b=B()
print(b.method1("abstract mehtod"))
