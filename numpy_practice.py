import numpy as np

arr1=np.arange(4)
arr2=np.zeros((4,4),dtype=float)
arr3=np.ones((3,3),dtype=str)

arr4=np.random.randint(0,10,(3,3))
arr5=np.random.normal(0,1,(3,3))
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)


arr6=np.array([5,6,7,8])

arr7=np.concatenate([arr1,arr6],axis=0)
print(arr7)
arr8=np.concatenate([arr1,arr6],axis=1)

print(arr8)