# loops 

a=input("entere your name").split(" ")
for i in range (0,len(a)):
    print(a[i])

while
n=int(input("enter n: "))
i=1
while i<n:
    print(i)
    i+=1
    
# string


list
a=[2,'abc',7.9]
print(a)
for i in range(len(a)):
    print(a[i])
for i in a:
    print(i)

# list Comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# methods -- append(), insert(),remove(),pop(),clear(),sort(), count(),sorted(), reverse()

tuple
my_tuple = (1, 2, 3)
for i in my_tuple:
    print(i)

# index, count

# Dictionay
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "Hyderabad"
}
print(my_dict.items())      #return the items
for i in my_dict:         #return the keys
    print(my_dict)
for key, value in my_dict.items():
    print(key, value)

# methods -- update(),pop(),clear(),setdefault()

set
my_set = set([1, 2, 3, 4])
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union:        {1, 2, 3, 4, 5}
print(a & b)   # Intersection: {3}
print(a - b)   # Difference:   {1, 2}
print(a ^ b)   # Sym. Diff:    {1, 2, 4, 5}
for i in my_set:
    print(i)


a=int(input("enter values:"))
b=float(input("enter b value:"))
print(round(a+b))
print(a/b)
print(f"{a+b:,.2f}")

# command line argumets
import sys
import cowsay
if len(sys.argv)<2:
    print("to few")
elif len(sys.argv)>2:
    print("many")
print("hello, myname is ",sys.argv[1])
  
if len(sys.argv) < 2:
    sys.exit("too few")
for arg in sys.argv[1: ]:
    print(arg)


import requests
import json
if len(sys.argv)!=2:
    # cowsay.cow("hello, "+sys.argv[1])
    sys.exit()
response=requests.get("htttps://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])
print(response.json()) 
o=response.json()
for result in o["result"]:
    print(result["trackName"])

# pytest-----------
import math
def test_cal():
    num=2
    assert num*num==4
def test_call():
    num=3
    assert num+num==6

# test function----------
import tables as t
r=t.print_tables(10)
r1=list(r)
def test_resutl():
    assert len(r1) is 10
def test_type():

# files------------/
name=input("enter text:")
f=open("filespra.txt","r+")
print(f.read())
f.write(f"{name}")
print(f.tell())#tell the position of cursor
f.seek(0)  #move the cursor particular position

# with------ 
text=input("enter text:")
with open("filespra.txt","r+") as file:
    # file.write(text)
    lines=file.readlines()
for line in lines:
    name,value=line.rstrip().split(",")
    print("hello" ,value)
with open("student.csv") as f:
    for line in f:
        name,house=line.rstrip().split(",")
        print(name)

# csv-----------
import csv
students=[]
with open("student.csv") as f:
    reader=csv.reader(f)
    for name, home in reader:
        students.append({"name":name, "home":home})
for student in sorted(students, key=lambda student:student["name"]):
    print(f"{student['name']} is form {student['home']}")


# filter(function, list) condition true return 
l=[1,2,3,4,5,6]
print(list(filter(lambda x:x%2==0,l)))
names=['car','bike','','','van']
print(list(filter(None,names)))
# map() each value have output
t=(1,2,4,5)
print(tuple(map(lambda x:x*x ,t)))
# reduce() single output

from functools import reduce
def add_all(a,b):
    return a+b
nums=[3,5,3,6]
sum=reduce(add_all, nums)
print(sum)

# Generator return multiple statemetns at a time
def f1():
    for i in range(5):
        yield i
result=f1()
# print(result.__next__())
for i in result:
    print(i)


