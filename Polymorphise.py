#1st Ques
'''
class Dog():
    def Sound(self):
        print("Dog make's sound")

class Cat():
    def Sound(self):
        print("Cat catch fish")


D1=Dog()

C1=Cat()



D1.Sound()
C1.Sound()
'''

'''
#2nd Ques

Num=50
print("Integer:",Num)

Fornt="Python"
print("String:",Fornt)
print("length of string:",(Fornt))

Order=[1,2,],[3,4,5]
print("List:",Order)

'''


'''
#3rd ques
def Display(data):
    
    if isinstance(data,int):
        print("integer")
    
    elif isinstance(data,str):
        print("string")
    
    else:
         print("floot")
Display(988498)
Display("PYthon")
Display(5.35)

        
'''
#forLoop method 
#4th ques
'''
class car:
    def move(self):
        print("The Car Is Moveing")

class bike():
    def move(self):
        print("The Bike Is Rash Riding")

class truck():
   def move(self):
      print("truck is moveing forward")

a =[bike(),car(),truck()]

for i in a:

 i.move()

'''

'''
#Class method 
#5th Ques

class Employee:
    def _get_salary(self):
        print("When my Salary credied !")

class Manager():
    def _get_salary(self):
        print("Your salary now credit")

        
E= Employee()
M=Manager()

E._get_salary()
M._get_salary()

'''


#6th question
'''
class Airport:
    def move(self):
        print("Airindia Is Ready to takeoff")

class Airindia():
    def move(self):
        print("Flight takeoff")

class Landed(Airport):
   def Chennai(self):
      print("Air india landed")

Airport =[Airport(),Airindia(),Landed()]

for a in Airport:
    a.move()

'''



'''
#7th Question
class A:
    def Show(self):
        print("A")

class B(A):
    def Show(self):
        print("B!")

A1=A()

obj=B()

#
obj.Show()
A1.Show()

'''

#8th Ques

'''
class Parant:
    def Father(self):
        print("Father's Bike")

class Son(Parant):
    def Kiran(self):
       super().Father()
       print("Son's Cycle")
       
S=Son()

S.Kiran()
'''

'''
#9th Ques
 

 
def add(a,b,c=0):
 
  return a+b+c

print(add(1,2))
print(add(4,5,7))
'''
''''
#10th Ques 

def add(a,b,c=0):
 
  return a+(b*c)

print(add(1,2))
print(add(4,5,7))
'''


#example of Abstraction qus

''''
from abc import ABC ,abstractmethod
class lap(ABC):
  @abstractmethod
  def screen(self):
    pass
  def mouse(self):
    pass
class org(lap):
  def screen(self):
    print("app,network")
  def mouse(self):
    print('light')
or1=org()
or1.screen()
or1.mouse()
'''






#practice

from abc import ABC ,abstractmethod
class Model:
  def IP20(self):
    pass
  class Mobile:
    def Iphone20(self):
      pass

class Lunch(Model):
  def Features(self):
    print("Nightcamera,Fast Speed ,sou:dollby atoms")
 
  def Date(self):
    print("Iphone 20 Lunching in 20th Feb ")

#object

'''

L=Lunch()
L.Features()
L.Date()
'''






numbers=0
while (numbers<10):
 
 print("tnskill")


 numbers+=1 

if numbers==5:
     break 