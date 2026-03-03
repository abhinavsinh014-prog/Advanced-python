# from numpy import *

# list_1 = [1, 2, 3, 4]
# list_2 = [5, 6, 7, 8]
# list_3 = [9, 10, 11, 12]

# max = array([list_1, 
#                     list_2,
#                          list_3])
# print("Numpy multi dimensional array in python\n",
#       max)
# print('array shape  :',max.shape)

# var = "john cena"

# bash = fromiter(var,dtype='U2')
# print("fromiter",bash)

import numpy as np

nam = np.arange(1, 20 , 2, 
          dtype = np.int16)

print(nam)


cam = np.empty([4, 3],
         dtype = np.int32,
         order = 'f')

print(cam)