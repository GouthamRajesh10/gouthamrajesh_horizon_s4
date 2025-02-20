import matplotlib.pyplot as plt
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def neighbour(index,arr1,arr2):
    arr=[]
    for i in range(len(arr1)):
       arr.append(distance(arr1[index],arr2[index],arr1[i],arr2[i]))
    print(arr)
    small=min([num for num in arr if num > 0])
    return arr.index(small)

def remove(arr, index):
    if 0 <= index < len(arr):
        return arr[:index] + arr[index+1:]
    else:
        print("Index out of bounds")
        return arr

print("Enter The X axis points")
x=list(map(int, input("Enter the numbers:").split()))
print("Enter the Y axis points")
y=list(map(int, input("Enter the numbers:").split()))
while(sum(1 for i in x if i > 1) > 1):
    plt.plot(x, y, color='r', marker='o', label="Data Points")       
    i1=int(input("Enter the indices to be connected: "))
    i2=neighbour(i1,x,y)
    print(i2)
    plt.plot([x[i1], x[i2]], [y[i1], y[i2]], color='b', linestyle='--', label="Nearest Neighbor")
    plt.show()
    x=remove(x,i1);
    y=remove(y,i1);
    

