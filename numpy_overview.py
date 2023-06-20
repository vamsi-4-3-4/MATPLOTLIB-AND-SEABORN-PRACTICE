import numpy as np
a=np.arange(40).reshape(8,5)
#8 ROWS AND 5 COLUMNS
print(a)
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[0][3])
print(a[0][4])
#INDEX ERROR STATEMENT
#print(a[0][5])
print("DATATYPE:",a.dtype)
print("NUMBER OF DIMENSIONS:",a.ndim)
print("SHAPE OF THE ARRAY:",a.shape)
print("TOTAL NUMBER ELEMENTS:",a.size)
#CREATING THE ARRAY WITH THE REQUIRED ELEMENTS
b=np.array([("APPLE","BOEING","COMPAQ","DELL"),("FOX","GOOGLE","HP","IPL")])
print("OUR ARRAY IS:\n",b)
#GENERATING NUMBERS USING THE ARANGE
numbers=np.arange(1,30,3)
print("GENERATED NUMBERS\n",numbers)

#GENERATE 50 NUMBERS BETWEEN 0-3
numbers_50_between_3_4=np.linspace(3,4,50)
print("50 NUMBERS BETWEEN 3-4\n",numbers_50_between_3_4)
#SHAPING THE ABOVE GENERATION
numbers_50_between_3_4=np.linspace(3,4,50).reshape(10,5)
print("50 NUMBERS BETWEEN 3-4\n",numbers_50_between_3_4)
#GENERATING RANDOM NUMBERS
random_numbers=np.random.rand(3,4,10)
print("GENERATED RANDOM NUMBERS:\n",random_numbers)
