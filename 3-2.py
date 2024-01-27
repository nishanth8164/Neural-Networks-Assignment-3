import numpy as np #importing numpy library
vec=np.arange(1,21,dtype=float) #creating a numpy vector with arange function
print(vec)
vec=vec.reshape(4,5)#reshaping the vector with reshape() function
print(vec)
vec=np.where(np.isin(vec,vec.max(axis=1)),0,vec)#finding the max values in row and replacing them with zero using np.where() and np.max() function
vec
