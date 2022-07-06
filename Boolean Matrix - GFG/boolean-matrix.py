#User function Template for python3


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    # code here 
    r=0
    c=0
    rl=len(matrix)  
    cl=len(matrix[0])
    for j in range(cl):
        if matrix[0][j]==1:
            r=1
    for i in range(rl):
        if matrix[i][0]==1:
            c=1
    for i in range(1,rl):
        for j in range(1,cl):
            if matrix[i][j]==1:
                matrix[0][j]=1
                matrix[i][0]=1
    for i in range(rl-1,0,-1):
        for j in range(cl-1,0,-1):
            if matrix[0][j]==1 or matrix[i][0]==1:
                matrix[i][j]=1
    if r:
        for i in range(cl):
            matrix[0][i]=1
    if c:
        for i in range(rl):
            matrix[i][0]=1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends