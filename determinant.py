import numpy as np
import sys

sys.setrecursionlimit(10000000)

matrix = []

def determinant(A):
    m, n = A.shape
    print(m, n)
    if n == 2:
        d = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
        return d
    else:
        d = 0
        for i in range(0, n):
            A_temp = A
            A_temp = np.delete(A_temp, obj=0, axis=0)
            A_temp = np.delete(A_temp, obj=i, axis=1)
            print(d)
            d = (d + ((-1)**(1+(i+1))) * (A[1][i] * determinant(A_temp)))
            print(d)
        return d 

  
def user_input(m, n):
    if m != n:
        print('matrix is not square, Determinant Does not exist')
    else:    
        print("Enter the entries rowwise:")
        for i in range(m):
            a =[]
            for j in range(n):      
                a.append(int(input()))
            matrix.append(a)  
        A = np.array(matrix)      
        d = determinant(A)
        print(f"Determinant of matrix is: {d}")


  



m = int(input("Enter the number of rows:"))
n = int(input("Enter the number of columns:"))
user_input(m, n)


    