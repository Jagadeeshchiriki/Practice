import numpy as np
print(np.__version__)
a=np.array([[10,20],[2,3]])
print(a[1][0])


# asarray(input,datatype,order=c,f)
a=[[10,20],[30,40]]
b=np.asarray(a,dtype=float,order="F")
print(b)
# using the nditer method to print the asarray method
for i in np.nditer(b):
    print(i)

# when you have a bytes, bytearray, or other buffer object.
# a consider a buffer then using the 'b' infront the string
a=b"welcome to numpy"
c=np.frombuffer(a,dtype="S1",count=10,offset=4)
print(c)

# Creates an array from any iterable, like a list, generator, or range.
c=np.fromiter(a,dtype="S1")
print(c)

# intializing array

# zeros() filling all values with zeros
a=np.zeros([2,3])
print(a)

# ones() filling all values with ones
a=np.ones([2,3])
print(a)

# eye() filling all diagnol values with ones in square matrix
a=np.eye(2)
print(a)

# full(dimention, element)
a=np.full(4,2)
print(a)

# random.rand(dimention)
a=np.random.rand(5,10)
print(a)

# array operations ----
# accessing and slicing operations
# cop(),view(),sort(),reshape(),append(),insert(),delete(),concatenate(),stak(),vstack(),hstac(),split(),where(),searchsorted()

a=np.array([2,3,4,5,6,10,29])
print(a[2:5])
print(a[1:5:2])

# a[row,columsl]
a=np.a00y(10,20)
print(a[1,0:2])


# arange(start,end,step)
a=np.arange(10,70,10)
print(a)

a=a.reshape(2,3)
print(a)

# linespace(start,stop,step,edpoint=t,f)
a=np.linspace(10,90,10,endpoint=False,retstep=True,dtype=int)
print(a)

# logspace(10,20,5,base)
a=np.logspace(10,20,5)
print(a)

a=([[10,30,50],[23,12,19]])
a=np.sort(a,axis=0)
print(a)